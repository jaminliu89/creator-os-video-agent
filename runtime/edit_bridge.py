from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from runtime.providers import BaseProvider, ExternalActionRequired


class ChatCutExternalMCPProvider(BaseProvider):
    """Agent-neutral file bridge for ChatCut MCP execution.

    The Video Agent owns request/result semantics. A host Agent (Codex, Claude,
    Hermes, Pi, WorkBuddy, etc.) may fulfill the request using whichever ChatCut
    MCP surface it has. No ChatCut tool names are embedded here.
    """

    provider_id = "chatcut-mcp"
    capabilities = {"media_import", "transcript_edit", "timeline_edit", "captions", "motion_graphics", "export", "verification"}
    editable_output = True

    def __init__(self, provider_surface: str = "desktop_local_mcp"):
        self.provider_surface = provider_surface

    @staticmethod
    def _operation_capability(capability: str) -> str:
        mapping = {
            "trim": "timeline_edit",
            "concat": "timeline_edit",
            "transcript_edit": "transcript_edit",
            "subtitle_burn": "captions",
            "captions": "captions",
            "motion_graphics": "motion_graphics",
            "media_import": "media_import",
            "export": "export",
            "verification": "verification",
        }
        return mapping.get(capability, "timeline_edit")

    def _paths(self, project_root: Path, job_id: str) -> tuple[Path, Path]:
        root = Path(project_root) / "external" / "chatcut"
        root.mkdir(parents=True, exist_ok=True)
        return root / f"{job_id}.request.json", root / f"{job_id}.result.json"

    def _artifact_inputs(self, project_root: Path, job: Dict[str, Any]) -> list[dict[str, Any]]:
        manifest_path = Path(project_root) / "evidence" / "manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {"artifacts": []}
        known = {a.get("artifact_id"): a for a in manifest.get("artifacts", [])}
        items = []
        for ref in job.get("input_refs", []):
            artifact = known.get(ref, {})
            items.append({"artifact_id": ref, "uri": artifact.get("uri", ref), "checksum": artifact.get("checksum")})
        if not items:
            items.append({"artifact_id": "project:source", "uri": "input/source.mp4", "checksum": None})
        return items

    def _request(self, project_root: Path, job: Dict[str, Any]) -> Dict[str, Any]:
        requirements = job.get("requirements") or {}
        capabilities = requirements.get("capabilities") or ["timeline_edit"]
        operations = [
            {
                "operation_id": f"{job['job_id']}:op:{index + 1}",
                "capability": self._operation_capability(capability),
                "time_range": None,
                "parameters": {"source_capability": capability},
            }
            for index, capability in enumerate(capabilities)
        ]
        if requirements.get("verification_required", True) and not any(op["capability"] == "verification" for op in operations):
            operations.append({"operation_id": f"{job['job_id']}:verify", "capability": "verification", "time_range": None, "parameters": {}})
        return {
            "version": "1.0",
            "request_id": f"request:{job['job_id']}",
            "job_id": job["job_id"],
            "project_ref": str(Path(project_root).resolve()),
            "provider_surface": self.provider_surface,
            "input_artifacts": self._artifact_inputs(project_root, job),
            "operations": operations,
            "requirements": {
                "editable_output": True,
                "verification_required": requirements.get("verification_required", True),
                "preview_required": requirements.get("preview_required", True),
                "approval_required": requirements.get("approval_required", False),
            },
            "intent_refs": job.get("intent_refs", []),
            "approval_policy": {"destructive_changes": "review_required"},
        }

    def execute(self, job: Dict[str, Any], project_root: Path) -> Dict[str, Any]:
        request_path, result_path = self._paths(project_root, job["job_id"])
        request = self._request(project_root, job)
        request_path.write_text(json.dumps(request, ensure_ascii=False, indent=2), encoding="utf-8")

        if not result_path.exists():
            raise ExternalActionRequired(
                provider_id=self.provider_id,
                request_path=str(request_path.relative_to(project_root)),
                result_path=str(result_path.relative_to(project_root)),
                message="ChatCut MCP request is ready for an external host Agent",
            )

        result = json.loads(result_path.read_text(encoding="utf-8"))
        if result.get("version") != "1.0" or result.get("request_id") != request["request_id"] or result.get("job_id") != job["job_id"]:
            raise RuntimeError("ChatCut result does not match request identity")
        if result.get("status") != "succeeded":
            raise RuntimeError(f"ChatCut external result status={result.get('status')}")
        verification = result.get("verification") or {}
        if request["requirements"]["verification_required"] and verification.get("status") not in {"pass", "warning"}:
            raise RuntimeError("ChatCut result failed required verification")
        artifacts = result.get("artifacts") or []
        if not any(a.get("editable") is True and a.get("kind") in {"editable_project", "timeline"} for a in artifacts):
            raise RuntimeError("ChatCut result missing editable project/timeline artifact")

        normalized = []
        for artifact in artifacts:
            normalized.append({
                "artifact_id": artifact["artifact_id"],
                "kind": artifact["kind"],
                "uri": artifact["uri"],
                "producer_job": job["job_id"],
                "provider": self.provider_id,
                "qa_status": "pass" if verification.get("status") == "pass" else "warning",
                "checksum": artifact.get("checksum"),
                "metadata": {**(artifact.get("metadata") or {}), "editable": artifact.get("editable", False), "provider_surface": result.get("provider_surface", self.provider_surface)},
            })
        return {
            "status": "ok",
            "artifacts": normalized,
            "editable": True,
            "verification": verification,
            "intent_refs": result.get("intent_refs", []),
            "warnings": result.get("warnings", []),
            "external_result": str(result_path.relative_to(project_root)),
        }

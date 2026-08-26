from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


class ProviderUnavailable(RuntimeError):
    pass


class ExternalActionRequired(RuntimeError):
    def __init__(self, provider_id: str, request_path: str, result_path: str, message: str = "external provider action required"):
        super().__init__(message)
        self.provider_id = provider_id
        self.request_path = request_path
        self.result_path = result_path


class BaseProvider:
    provider_id = "base"
    capabilities: set[str] = set()
    editable_output = False

    def can_handle(self, job: Dict[str, Any]) -> bool:
        requirements = job.get("requirements") or {}
        required = set(requirements.get("capabilities", []))
        if not required.issubset(self.capabilities):
            return False
        if requirements.get("editable_output") is True and not self.editable_output:
            return False
        return True

    def execute(self, job: Dict[str, Any], project_root: Path) -> Dict[str, Any]:
        raise NotImplementedError


class FixtureFFmpegProvider(BaseProvider):
    provider_id = "ffmpeg"
    capabilities = {"media_probe", "trim", "concat", "audio_mux", "subtitle_burn", "transcode", "assemble", "transcript_edit"}

    def execute(self, job: Dict[str, Any], project_root: Path) -> Dict[str, Any]:
        artifacts = []
        for output_ref in job.get("output_refs", []):
            safe = output_ref.replace(":", "-")
            target = Path(project_root) / "artifacts" / f"{safe}.json"
            payload = {"job_id": job["job_id"], "provider": self.provider_id, "output_ref": output_ref}
            target.write_text(json.dumps(payload, indent=2), encoding="utf-8")
            artifacts.append({"artifact_id":output_ref,"kind":job["kind"],"uri":str(target.relative_to(project_root)),"producer_job":job["job_id"],"provider":self.provider_id,"qa_status":"pass","metadata":{"fixture":True}})
        return {"status":"ok","artifacts":artifacts,"fixture":True}


class FixtureDirectorProvider(BaseProvider):
    provider_id = "ai-director-engine"
    capabilities = {"perception", "semantic_direction", "director_ir", "intent_qa"}

    def execute(self, job: Dict[str, Any], project_root: Path) -> Dict[str, Any]:
        target = Path(project_root) / "state" / "director-ir.json"
        payload = {"schema_version":"1.0","source":{"type":"transcript","path":"input/transcript.md","duration":1.0,"language":"zh"},"segments":[{"id":"seg-1","start":0.0,"end":1.0,"transcript":"测试逐字稿。","narrative_function":"exposition","director_intent":"preserve_clarity","confidence":0.8,"rationale":"fixture-provider"}]}
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return {"status":"ok","artifacts":[{"artifact_id":"state:director-ir","kind":"director_ir","uri":"state/director-ir.json","producer_job":job["job_id"],"provider":self.provider_id,"qa_status":"pass","metadata":{"fixture":True}}],"fixture":True}


class FixtureMotionRuntimeProvider(BaseProvider):
    provider_id = "motion-runtime-remotion"
    capabilities = {"motion_graphics", "kinetic_text", "video_layer", "audio_layer", "deterministic_render"}
    editable_output = True

    def execute(self, job: Dict[str, Any], project_root: Path) -> Dict[str, Any]:
        target = Path(project_root) / "artifacts" / "motion-render.mp4.fixture"
        target.write_text("fixture motion render", encoding="utf-8")
        return {"status":"ok","artifacts":[{"artifact_id":"artifact:motion-render","kind":"video","uri":"artifacts/motion-render.mp4.fixture","producer_job":job["job_id"],"provider":self.provider_id,"qa_status":"pass","metadata":{"fixture":True}}],"fixture":True}


class CapabilityRouter:
    def __init__(self, providers: List[BaseProvider]):
        self.providers = {p.provider_id: p for p in providers}

    def candidates(self, job: Dict[str, Any]) -> List[BaseProvider]:
        ordered_ids: list[str] = []
        preferred = job.get("preferred_provider")
        if preferred: ordered_ids.append(preferred)
        ordered_ids.extend(job.get("fallback_providers") or [])
        ordered: List[BaseProvider] = []; seen: set[str] = set()
        for provider_id in ordered_ids:
            if provider_id in seen: continue
            seen.add(provider_id); provider = self.providers.get(provider_id)
            if provider and provider.can_handle(job): ordered.append(provider)
        for provider in self.providers.values():
            if provider.provider_id in seen: continue
            if provider.can_handle(job): ordered.append(provider); seen.add(provider.provider_id)
        return ordered

    def resolve(self, job: Dict[str, Any]) -> BaseProvider:
        candidates = self.candidates(job)
        if candidates: return candidates[0]
        requirements = job.get("requirements") or {}
        raise ProviderUnavailable(f"No provider satisfies {job['job_id']} capabilities={requirements.get('capabilities', [])} editable_output={requirements.get('editable_output', False)}")


def fixture_router() -> CapabilityRouter:
    return CapabilityRouter([FixtureFFmpegProvider(), FixtureDirectorProvider(), FixtureMotionRuntimeProvider()])

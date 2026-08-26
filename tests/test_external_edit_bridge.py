import json
from pathlib import Path

from jsonschema import validate

from runtime.edit_bridge import ChatCutExternalMCPProvider
from runtime.pipeline import PipelineRunner
from runtime.providers import CapabilityRouter


def pipeline_fixture():
    return {
        "version": "1.0",
        "project_id": "editable-demo",
        "jobs": [{
            "job_id": "edit-001",
            "kind": "edit",
            "needs": [],
            "input_refs": ["artifact:normalized-source"],
            "output_refs": ["artifact:editable-project"],
            "preferred_provider": "chatcut-mcp",
            "fallback_providers": [],
            "requirements": {
                "capabilities": ["transcript_edit", "captions"],
                "editable_output": True,
                "verification_required": True,
            },
            "intent_refs": ["director:seg-1"],
        }],
    }


def test_chatcut_external_handoff_waits_then_resumes(tmp_path):
    schema_root = Path("schemas")
    request_schema = json.loads((schema_root / "edit-provider-request.v1.schema.json").read_text())
    result_schema = json.loads((schema_root / "edit-provider-result.v1.schema.json").read_text())

    evidence_dir = tmp_path / "evidence"; evidence_dir.mkdir(parents=True)
    (evidence_dir / "manifest.json").write_text(json.dumps({
        "version":"1.0","project_id":"editable-demo","events":[],"artifacts":[{
            "artifact_id":"artifact:normalized-source","kind":"video","uri":"artifacts/normalized-source.mp4","checksum":"sha256:fixture","producer_job":"ingest-001","provider":"ffmpeg","qa_status":"pass","metadata":{}
        }],"provider_failovers":[],"external_handoffs":[]
    }), encoding="utf-8")

    router = CapabilityRouter([ChatCutExternalMCPProvider()])
    first = PipelineRunner(pipeline_fixture(), tmp_path, router)
    state = first.run()
    assert state["status"] == "blocked"
    assert state["jobs"]["edit-001"]["status"] == "waiting_external"

    request_path = tmp_path / "external/chatcut/edit-001.request.json"
    result_path = tmp_path / "external/chatcut/edit-001.result.json"
    request = json.loads(request_path.read_text(encoding="utf-8"))
    validate(request, request_schema)
    assert request["provider_surface"] == "desktop_local_mcp"
    assert request["requirements"]["editable_output"] is True
    assert {op["capability"] for op in request["operations"]} >= {"transcript_edit", "captions", "verification"}

    result = {
        "version":"1.0",
        "request_id":request["request_id"],
        "job_id":"edit-001",
        "provider":"chatcut",
        "provider_surface":"desktop_local_mcp",
        "status":"succeeded",
        "artifacts":[
            {"artifact_id":"artifact:editable-project","kind":"editable_project","uri":"external/chatcut/project.chatcut","editable":True,"checksum":None,"metadata":{"timeline_preserved":True}},
            {"artifact_id":"artifact:edit-preview","kind":"preview_video","uri":"external/chatcut/preview.mp4","editable":False,"checksum":None,"metadata":{}}
        ],
        "verification":{"status":"pass","checks":[{"check":"timeline-readable","status":"pass","evidence":"project opened"}]},
        "intent_refs":["director:seg-1"],
        "warnings":[],
        "downgrades":[]
    }
    validate(result, result_schema)
    result_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    resumed = PipelineRunner(pipeline_fixture(), tmp_path, router)
    assert resumed.resume_external("edit-001") == 1
    state2 = resumed.run()
    assert state2["status"] == "succeeded"
    attempts = state2["jobs"]["edit-001"]["attempts"]
    assert attempts[0]["status"] == "waiting_external"
    assert attempts[1]["status"] == "succeeded"
    manifest = json.loads((tmp_path / "evidence/manifest.json").read_text(encoding="utf-8"))
    assert manifest["external_handoffs"][0]["provider"] == "chatcut-mcp"
    assert any(a["artifact_id"] == "artifact:editable-project" and a["metadata"]["editable"] for a in manifest["artifacts"])

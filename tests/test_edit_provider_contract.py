import json
from pathlib import Path

from jsonschema import Draft202012Validator


def _schema(name):
    return json.loads((Path("schemas") / name).read_text(encoding="utf-8"))


def test_edit_provider_request_contract_accepts_agent_neutral_edit_job():
    request = {
        "version":"1.0",
        "request_id":"editreq-001",
        "job_id":"edit-001",
        "project_ref":"project:demo",
        "provider_surface":"desktop_local_mcp",
        "input_artifacts":[{"artifact_id":"artifact:normalized-source","uri":"artifacts/normalized-source.mp4","checksum":"sha256:abc"}],
        "operations":[
            {"operation_id":"op-1","capability":"media_import","parameters":{}},
            {"operation_id":"op-2","capability":"transcript_edit","time_range":{"start":0,"end":12.4},"parameters":{"remove_fillers":True}},
            {"operation_id":"op-3","capability":"captions","parameters":{"language":"zh"}},
            {"operation_id":"op-4","capability":"verification","parameters":{}}
        ],
        "requirements":{"editable_output":True,"verification_required":True,"preview_required":True,"approval_required":True},
        "intent_refs":["director:seg-1"],
        "approval_policy":{"destructive_changes":"review_required"}
    }
    Draft202012Validator(_schema("edit-provider-request.v1.schema.json")).validate(request)


def test_edit_provider_result_requires_editable_evidence():
    result = {
        "version":"1.0",
        "request_id":"editreq-001",
        "job_id":"edit-001",
        "provider":"chatcut",
        "provider_surface":"desktop_local_mcp",
        "status":"succeeded",
        "artifacts":[
            {"artifact_id":"artifact:editable-project","kind":"editable_project","uri":"provider://project/123","editable":True,"checksum":None,"metadata":{}},
            {"artifact_id":"artifact:preview","kind":"preview_video","uri":"artifacts/edit-preview.mp4","editable":False,"checksum":"sha256:def","metadata":{}}
        ],
        "verification":{"status":"pass","checks":[{"check":"timeline_edits_visible","status":"pass","evidence":"provider://verification/1"}]},
        "intent_refs":["director:seg-1"],
        "warnings":[],
        "downgrades":[]
    }
    Draft202012Validator(_schema("edit-provider-result.v1.schema.json")).validate(result)
    assert any(a["kind"] == "editable_project" and a["editable"] for a in result["artifacts"])

import json
from pathlib import Path

from runtime.pipeline import PipelineRunner
from runtime.providers import fixture_router


def load_pipeline():
    return json.loads(Path("examples/talking-head/pipeline-ir.json").read_text(encoding="utf-8"))


def test_walking_skeleton_runs_and_persists_evidence(tmp_path):
    runner = PipelineRunner(load_pipeline(), tmp_path, fixture_router())
    state = runner.run()
    assert state["status"] == "succeeded"
    assert all(job["status"] == "succeeded" for job in state["jobs"].values())
    assert (tmp_path / "state" / "run-state.json").exists()
    assert (tmp_path / "evidence" / "manifest.json").exists()
    manifest = json.loads((tmp_path / "evidence" / "manifest.json").read_text(encoding="utf-8"))
    assert len(manifest["events"]) == len(load_pipeline()["jobs"])
    assert any(a["artifact_id"] == "artifact:motion-render" for a in manifest["artifacts"])


def test_resume_does_not_rerun_succeeded_jobs(tmp_path):
    first = PipelineRunner(load_pipeline(), tmp_path, fixture_router())
    state1 = first.run()
    attempts_before = {job_id: len(slot["attempts"]) for job_id, slot in state1["jobs"].items()}
    second = PipelineRunner(load_pipeline(), tmp_path, fixture_router())
    state2 = second.run()
    attempts_after = {job_id: len(slot["attempts"]) for job_id, slot in state2["jobs"].items()}
    assert attempts_after == attempts_before


def test_provider_routing_uses_fallback_when_preferred_missing(tmp_path):
    pipeline = load_pipeline()
    motion = next(j for j in pipeline["jobs"] if j["job_id"] == "motion-001")
    motion["preferred_provider"] = "missing-provider"
    motion["fallback_providers"] = ["motion-runtime-remotion"]
    state = PipelineRunner(pipeline, tmp_path, fixture_router()).run()
    attempt = state["jobs"]["motion-001"]["attempts"][0]
    assert attempt["provider"] == "motion-runtime-remotion"

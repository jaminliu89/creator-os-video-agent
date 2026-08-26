import json
from pathlib import Path
import pytest

from runtime.pipeline import PipelineRunner
from runtime.providers import BaseProvider, CapabilityRouter, FixtureFFmpegProvider, FixtureDirectorProvider, ProviderUnavailable, fixture_router


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


class FailingMotionProvider(BaseProvider):
    provider_id = "motion-runtime-remotion"
    capabilities = {"motion_graphics", "kinetic_text", "video_layer", "audio_layer", "deterministic_render"}
    def execute(self, job, project_root):
        raise RuntimeError("simulated remotion failure")


class FallbackMotionProvider(BaseProvider):
    provider_id = "motion-runtime-hyperframes"
    capabilities = {"motion_graphics", "kinetic_text", "video_layer", "audio_layer", "deterministic_render"}
    def execute(self, job, project_root):
        target = Path(project_root) / "artifacts" / "motion-render.mp4.fixture"
        target.write_text("hyperframes fallback", encoding="utf-8")
        return {"status":"ok","artifacts":[{"artifact_id":"artifact:motion-render","kind":"video","uri":"artifacts/motion-render.mp4.fixture","producer_job":job["job_id"],"provider":self.provider_id,"qa_status":"pass","metadata":{"fixture":True}}]}


def test_runtime_failure_falls_back_and_records_evidence(tmp_path):
    pipeline = load_pipeline()
    motion = next(j for j in pipeline["jobs"] if j["job_id"] == "motion-001")
    motion["preferred_provider"] = "motion-runtime-remotion"
    motion["fallback_providers"] = ["motion-runtime-hyperframes"]
    router = CapabilityRouter([FixtureFFmpegProvider(), FixtureDirectorProvider(), FailingMotionProvider(), FallbackMotionProvider()])
    state = PipelineRunner(pipeline, tmp_path, router).run()
    attempts = state["jobs"]["motion-001"]["attempts"]
    assert [a["provider"] for a in attempts] == ["motion-runtime-remotion", "motion-runtime-hyperframes"]
    assert attempts[0]["status"] == "failed"
    assert attempts[1]["status"] == "succeeded"
    manifest = json.loads((tmp_path / "evidence" / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["provider_failovers"][0]["selected_provider"] == "motion-runtime-hyperframes"


def test_editable_edit_job_does_not_silently_downgrade_to_ffmpeg():
    job = {
        "job_id":"edit-editable",
        "kind":"edit",
        "requirements":{"capabilities":["transcript_edit"],"editable_output":True},
        "preferred_provider":"chatcut",
        "fallback_providers":["ffmpeg"],
    }
    router = CapabilityRouter([FixtureFFmpegProvider()])
    with pytest.raises(ProviderUnavailable):
        router.resolve(job)

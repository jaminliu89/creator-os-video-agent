from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List


TERMINAL = {"succeeded", "failed", "skipped"}


def _json_hash(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


@dataclass
class ProjectPaths:
    root: Path

    @property
    def state_dir(self) -> Path: return self.root / "state"
    @property
    def evidence_dir(self) -> Path: return self.root / "evidence"
    @property
    def artifacts_dir(self) -> Path: return self.root / "artifacts"
    @property
    def output_dir(self) -> Path: return self.root / "output"
    @property
    def run_state(self) -> Path: return self.state_dir / "run-state.json"
    @property
    def evidence_manifest(self) -> Path: return self.evidence_dir / "manifest.json"

    def ensure(self) -> None:
        for p in (self.state_dir, self.evidence_dir, self.artifacts_dir, self.output_dir): p.mkdir(parents=True, exist_ok=True)


class PipelineError(RuntimeError): pass


class PipelineRunner:
    """Deterministic orchestration kernel with durable state and provider fallback."""
    def __init__(self, pipeline: Dict[str, Any], project_root: Path, router: Any):
        self.pipeline=pipeline; self.paths=ProjectPaths(Path(project_root)); self.paths.ensure(); self.router=router
        self.jobs={job["job_id"]:job for job in pipeline["jobs"]}; self._validate_dag(); self.state=self._load_or_initialize_state(); self.evidence=self._load_or_initialize_evidence()

    @classmethod
    def from_file(cls,pipeline_path:Path,project_root:Path,router:Any):
        return cls(json.loads(Path(pipeline_path).read_text(encoding="utf-8")),project_root,router)

    def _validate_dag(self)->None:
        unknown=[]
        for job in self.jobs.values():
            for dep in job.get("needs",[]):
                if dep not in self.jobs: unknown.append((job["job_id"],dep))
        if unknown: raise PipelineError(f"Unknown dependencies: {unknown}")
        visited:set[str]=set(); active:set[str]=set()
        def visit(job_id:str)->None:
            if job_id in visited:return
            if job_id in active:raise PipelineError(f"Cycle detected at {job_id}")
            active.add(job_id)
            for dep in self.jobs[job_id].get("needs",[]):visit(dep)
            active.remove(job_id);visited.add(job_id)
        for job_id in self.jobs:visit(job_id)

    def _load_or_initialize_state(self)->Dict[str,Any]:
        current_hash=_json_hash(self.pipeline)
        if self.paths.run_state.exists():
            state=json.loads(self.paths.run_state.read_text(encoding="utf-8"))
            if state.get("pipeline_hash")!=current_hash:raise PipelineError("Pipeline changed since previous run; explicit migration/restart required")
            return state
        state={"version":"1.0","project_id":self.pipeline["project_id"],"pipeline_hash":current_hash,"created_at":int(time.time()),"jobs":{j:{"status":"planned","attempts":[]} for j in self.jobs}}
        self._write_json(self.paths.run_state,state);return state

    def _load_or_initialize_evidence(self)->Dict[str,Any]:
        if self.paths.evidence_manifest.exists():return json.loads(self.paths.evidence_manifest.read_text(encoding="utf-8"))
        evidence={"version":"1.0","project_id":self.pipeline["project_id"],"events":[],"artifacts":[],"provider_failovers":[]};self._write_json(self.paths.evidence_manifest,evidence);return evidence

    @staticmethod
    def _write_json(path:Path,value:Any)->None:
        path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix(path.suffix+".tmp");tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8");tmp.replace(path)

    def _persist(self)->None:self._write_json(self.paths.run_state,self.state);self._write_json(self.paths.evidence_manifest,self.evidence)
    def _dependencies_succeeded(self,job:Dict[str,Any])->bool:return all(self.state["jobs"][dep]["status"]=="succeeded" for dep in job.get("needs",[]))

    def ready_jobs(self)->List[Dict[str,Any]]:
        result=[]
        for job_id,job in self.jobs.items():
            status=self.state["jobs"][job_id]["status"]
            if status in TERMINAL or status=="running":continue
            if self._dependencies_succeeded(job):result.append(job)
        return result

    def run(self)->Dict[str,Any]:
        while True:
            ready=self.ready_jobs()
            if not ready:break
            for job in ready:self._run_job(job)
        blocked=[j for j,s in self.state["jobs"].items() if s["status"] not in TERMINAL]
        self.state["status"]="succeeded" if not blocked and all(s["status"]=="succeeded" for s in self.state["jobs"].values()) else "blocked";self._persist();return self.state

    def _record_success(self, job:Dict[str,Any], provider:Any, attempt:Dict[str,Any], result:Dict[str,Any])->None:
        job_id=job["job_id"];slot=self.state["jobs"][job_id];attempt["finished_at"]=int(time.time());attempt["status"]="succeeded";attempt["result"]=result;slot["status"]="succeeded"
        event_id=f"event:{job_id}:{attempt['attempt']}";self.evidence["events"].append({"event_id":event_id,"job_id":job_id,"provider":provider.provider_id,"semantic_hash":attempt["semantic_hash"],"result":result})
        for artifact in result.get("artifacts",[]):self.evidence["artifacts"].append(artifact)

    def _run_job(self,job:Dict[str,Any])->None:
        job_id=job["job_id"];slot=self.state["jobs"][job_id]
        candidates=self.router.candidates(job) if hasattr(self.router,"candidates") else [self.router.resolve(job)]
        if not candidates: self.router.resolve(job); return
        failures=[]
        for index,provider in enumerate(candidates):
            attempt={"attempt":len(slot["attempts"])+1,"provider":provider.provider_id,"started_at":int(time.time()),"semantic_hash":_json_hash({"job":job,"provider":provider.provider_id})}
            slot["status"]="running";slot["attempts"].append(attempt);self._persist()
            try:
                result=provider.execute(job=job,project_root=self.paths.root);self._record_success(job,provider,attempt,result)
                if failures:self.evidence["provider_failovers"].append({"job_id":job_id,"failed_providers":failures,"selected_provider":provider.provider_id})
                self._persist();return
            except Exception as exc:
                attempt["finished_at"]=int(time.time());attempt["status"]="failed";attempt["error"]=str(exc);failures.append({"provider":provider.provider_id,"error":str(exc)})
                has_next=index < len(candidates)-1
                slot["status"]="planned" if has_next else "failed";self._persist()
                if not has_next:raise

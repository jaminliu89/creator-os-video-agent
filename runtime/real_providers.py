from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict

from runtime.providers import BaseProvider, CapabilityRouter


def _run(cmd, cwd=None):
    subprocess.run(cmd, cwd=cwd, check=True)


def _sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def _artifact(project_root: Path, artifact_id: str, kind: str, path: Path, job_id: str, provider: str, **metadata):
    return {"artifact_id":artifact_id,"kind":kind,"uri":str(path.relative_to(project_root)),"checksum":"sha256:"+_sha256(path),"producer_job":job_id,"provider":provider,"qa_status":"pass","metadata":metadata}


class RealFFmpegProvider(BaseProvider):
    provider_id='ffmpeg'
    capabilities={"media_probe","trim","concat","audio_mux","subtitle_burn","transcode","assemble","transcript_edit"}

    def execute(self, job: Dict[str,Any], project_root: Path)->Dict[str,Any]:
        root=Path(project_root); source=root/'input/source.mp4'; artifacts=[]
        if not source.exists(): raise FileNotFoundError(source)
        if job['kind']=='ingest':
            target=root/'artifacts/normalized-source.mp4'; target.parent.mkdir(parents=True,exist_ok=True)
            _run(['ffmpeg','-y','-i',str(source),'-c','copy',str(target)])
            probe=root/'evidence/source-ffprobe.json'; probe.parent.mkdir(parents=True,exist_ok=True)
            raw=subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(target)],text=True)
            probe.write_text(raw,encoding='utf-8')
            artifacts=[_artifact(root,'artifact:normalized-source','video',target,job['job_id'],self.provider_id,real_media=True),_artifact(root,'evidence:source-probe','evidence',probe,job['job_id'],self.provider_id,real_media=True)]
        elif job['kind']=='edit':
            src=root/'artifacts/normalized-source.mp4'; target=root/'artifacts/rough-cut.mp4'
            _run(['ffmpeg','-y','-i',str(src),'-c','copy',str(target)])
            artifacts=[_artifact(root,'artifact:rough-cut','video',target,job['job_id'],self.provider_id,edit_mode='passthrough_real_media')]
        elif job['kind']=='qa':
            src=root/'artifacts/motion-render.mp4'; target=root/'evidence/final-media-probe.json'; target.parent.mkdir(parents=True,exist_ok=True)
            raw=subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(src)],text=True); target.write_text(raw,encoding='utf-8')
            data=json.loads(raw); types={s.get('codec_type') for s in data.get('streams',[])}
            if not {'video','audio'}.issubset(types): raise RuntimeError(f'final render missing streams: {types}')
            artifacts=[_artifact(root,'evidence:media-qa','evidence',target,job['job_id'],self.provider_id,video_audio_pass=True)]
        elif job['kind']=='export':
            src=root/'artifacts/motion-render.mp4'; target=root/'output/final.mp4'; target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,target)
            artifacts=[_artifact(root,'artifact:final-video','video',target,job['job_id'],self.provider_id,accepted=True)]
        else: raise RuntimeError(f'unsupported ffmpeg job kind {job["kind"]}')
        return {'status':'ok','artifacts':artifacts,'real':True}


class RealDirectorProvider(BaseProvider):
    provider_id='ai-director-engine'
    capabilities={"perception","semantic_direction","director_ir","intent_qa"}
    def execute(self, job:Dict[str,Any], project_root:Path)->Dict[str,Any]:
        root=Path(project_root); repo=Path(os.environ['AI_DIRECTOR_REPO']).resolve(); source=root/'artifacts/normalized-source.mp4'
        director=root/'state/director-ir.json'; motion=root/'state/motion-ir.json'; qa=root/'evidence/director-intent-qa.json'
        env=os.environ.copy(); env['PYTHONPATH']=str(repo)
        subprocess.run(['python',str(repo/'prototype/analyze.py'),str(source),'-o',str(director),'--model','tiny','--source-asset-ref','real-media-interview.mp4','--motion-output',str(motion),'--qa-output',str(qa)],cwd=repo,env=env,check=True)
        return {'status':'ok','artifacts':[_artifact(root,'state:director-ir','director_ir',director,job['job_id'],self.provider_id,real=True),_artifact(root,'state:motion-ir','motion_ir',motion,job['job_id'],self.provider_id,real=True),_artifact(root,'evidence:director-qa','evidence',qa,job['job_id'],self.provider_id,real=True)],'real':True}


class RealMotionRuntimeProvider(BaseProvider):
    provider_id='motion-runtime-remotion'
    capabilities={"motion_graphics","kinetic_text","video_layer","audio_layer","deterministic_render"}
    def execute(self,job:Dict[str,Any],project_root:Path)->Dict[str,Any]:
        root=Path(project_root); repo=Path(os.environ['MOTION_RUNTIME_REPO']).resolve()
        (repo/'public/assets').mkdir(parents=True,exist_ok=True); (repo/'examples/real-media-director').mkdir(parents=True,exist_ok=True); (repo/'out').mkdir(exist_ok=True)
        shutil.copy2(root/'artifacts/rough-cut.mp4',repo/'public/assets/real-media-interview.mp4')
        shutil.copy2(root/'state/motion-ir.json',repo/'examples/real-media-director/motion-ir.json')
        _run(['node','scripts/validate-motion-ir.mjs','examples/real-media-director/motion-ir.json'],cwd=repo)
        _run(['npx','remotion','render','src/index.ts','RealMediaDirector','out/orchestrated-final.mp4'],cwd=repo)
        rendered=repo/'out/orchestrated-final.mp4'; target=root/'artifacts/motion-render.mp4'; target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(rendered,target)
        return {'status':'ok','artifacts':[_artifact(root,'artifact:motion-render','video',target,job['job_id'],self.provider_id,real=True,engine='remotion')],'real':True}


def real_router()->CapabilityRouter:
    return CapabilityRouter([RealFFmpegProvider(),RealDirectorProvider(),RealMotionRuntimeProvider()])

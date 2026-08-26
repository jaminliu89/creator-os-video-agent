from pathlib import Path
import json
from runtime.pipeline import PipelineRunner
from runtime.real_providers import real_router

root=Path('work/real-media').resolve()
pipeline=Path('examples/real-media/pipeline-ir.json').resolve()
runner=PipelineRunner.from_file(pipeline,root,real_router())
state=runner.run()
print(json.dumps(state,ensure_ascii=False,indent=2))
if state.get('status')!='succeeded':
    raise SystemExit('pipeline did not succeed')
final=root/'output/final.mp4'
if not final.exists() or final.stat().st_size==0:
    raise SystemExit('missing final.mp4')
print(f'FINAL={final}')

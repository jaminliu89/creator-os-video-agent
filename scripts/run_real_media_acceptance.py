from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from runtime.pipeline import PipelineRunner
from runtime.real_providers import real_router


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a real-media Creator OS Video Agent pipeline")
    parser.add_argument("--project-root", default="work/real-media", help="Durable project working directory")
    parser.add_argument("--pipeline", default="examples/real-media/pipeline-ir.json", help="Pipeline IR JSON")
    parser.add_argument("--source", help="Optional source media to stage as input/source.mp4")
    args = parser.parse_args()

    root = Path(args.project_root).expanduser().resolve()
    pipeline = Path(args.pipeline).expanduser().resolve()
    if args.source:
        source = Path(args.source).expanduser().resolve()
        if not source.exists():
            raise SystemExit(f"source media not found: {source}")
        staged = root / "input" / "source.mp4"
        staged.parent.mkdir(parents=True, exist_ok=True)
        if source != staged:
            shutil.copy2(source, staged)
    staged = root / "input" / "source.mp4"
    if not staged.exists():
        raise SystemExit(f"missing staged source media: {staged}")
    if not pipeline.exists():
        raise SystemExit(f"pipeline IR not found: {pipeline}")

    runner = PipelineRunner.from_file(pipeline, root, real_router())
    state = runner.run()
    print(json.dumps(state, ensure_ascii=False, indent=2))
    if state.get("status") != "succeeded":
        raise SystemExit("pipeline did not succeed")
    final = root / "output" / "final.mp4"
    if not final.exists() or final.stat().st_size == 0:
        raise SystemExit("missing final.mp4")
    print(f"FINAL={final}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

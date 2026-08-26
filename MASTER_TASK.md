# MASTER TASK — Agent-neutral Video Production Orchestrator

## Objective
Build a production-grade local-first pipeline any compatible host Agent can execute:
`transcript/media → semantic direction → storyboard → Pipeline IR/DAG → provider routing → edit/motion/assets/audio → assembly → QA → final MP4`.

## Current decision
`creator-os-video-agent` is the orchestration Source of Truth above `ai-director-engine` and `motion-runtime-os`. No additional orchestrator repository.

## MT-001 — Contract & Architecture
Status: **DONE FOR V1 CONTRACT**
- [x] Agent-neutral orchestrator definition.
- [x] PRD v2 and cross-Agent architecture.
- [x] ChatCut/Codex/WorkBuddy/HyperFrames research capture.
- [x] Agent Compatibility Spec.
- [x] Pipeline IR Spec.
- [x] `schemas/pipeline-ir.v1.schema.json` — machine-readable Pipeline IR contract.
- [x] `registries/providers.v1.json` — capability/provider registry.
- [x] `registries/host-adapters.v1.json` — Codex/Claude/WorkBuddy/Hermes/Pi host registry.
- [x] `examples/talking-head/pipeline-ir.json` — first executable-shape walking-skeleton graph.

## MT-002 — Walking Skeleton
Status: **IN PROGRESS — CURRENT CRITICAL PATH**
One real talking-head project must create durable artifacts for every stage.
- [ ] `input/transcript.md` + source media convention.
- [ ] Transcript normalizer.
- [ ] Invoke/consume `ai-director-engine` Director IR.
- [ ] Storyboard compiler.
- [x] Director IR → Pipeline IR contract/fixture shape established.
- [ ] DAG runner with state persistence/resume.
- [ ] Capability router resolves provider registry without host-specific branching.
- [ ] FFmpeg provider adapter.
- [ ] Motion Runtime adapter (`motion-runtime-os`).
- [ ] Artifact/evidence manifest + final QA.
- [ ] `output/final.mp4` real-media acceptance artifact.

## MT-003 — Editable Edit Provider
- [ ] ChatCut capability discovery / MCP adapter.
- [ ] Import source media; transcript-based cut jobs; captions/timeline modifications.
- [ ] Export editable project evidence.
- [ ] FFmpeg fallback without corrupting Pipeline IR.

## MT-004 — Motion Router
- [ ] Route Motion IR to Remotion or HyperFrames by capability/semantics.
- [ ] Preserve cross-provider semantic QA from `motion-runtime-os`.
- [ ] Register downgrade/fallback evidence.

## MT-005 — Generation Routers
After core edit+motion works: image, video/B-roll, TTS/voice, music, optional avatar contracts. Provider brands never enter canonical Pipeline IR semantics.

## MT-006 — Host-Agent Neutrality
Same canonical fixture must execute under at least two host adapters with equivalent Pipeline IR semantics, durable layout, provider jobs and media QA. Handoff must work from files alone.

## MT-007 — Quality & Human Review
Transcript/timeline sync, media probe, director/motion semantic survival, visual continuity, provider downgrade report, approval gates and human preference evaluation.

## MVP Definition of Done
Not DONE because an Agent generated scripts. MVP requires one real talking-head project from files to `output/final.mp4`, resumable state, provider evidence, edit+motion execution, media/semantic QA, and successful execution from at least two host Agents.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider. ChatCut/Remotion/HyperFrames are providers, not canonical state. No silent semantic downgrade, prompt-only architecture, unnecessary repository, or Blender/Unreal/full-NLE detour on the critical path.

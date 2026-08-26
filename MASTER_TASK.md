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
- [x] Executable-shape talking-head and real-media Pipeline IR graphs.

## MT-002 — Walking Skeleton
Status: **IN PROGRESS — LOCAL ORCHESTRATION VERIFIED; CROSS-PRIVATE CI ACCESS BLOCKED**
One real talking-head project must create durable artifacts for every stage.
- [x] Source media convention: project-local `input/source.mp4`; transcript path reserved at `input/transcript.md`.
- [x] Transcript normalizer (`runtime/transcript.py`) supporting plain text and timestamped transcript input.
- [~] Real `ai-director-engine` adapter implemented; single-run CI verification blocked by private sibling checkout permission.
- [x] Storyboard compiler (`runtime/storyboard.py`) preserving Director IR semantics without provider leakage.
- [x] Director IR → Pipeline IR contract/fixture shape established.
- [x] DAG runner with dependency validation and state persistence/resume.
- [x] Capability router with preferred/fallback provider resolution and no host-specific workflow branch.
- [~] Real FFmpeg adapter implemented for ingest/edit passthrough/media QA/export; cross-repo full acceptance still pending.
- [~] Real Motion Runtime adapter implemented for staging Motion IR/source media and Remotion render; single-run CI verification blocked by private sibling checkout permission.
- [x] Artifact/evidence manifest kernel with append-only attempts, provider/result evidence, checksum and artifact lineage.
- [~] Final media QA code implemented; end-to-end Video Agent evidence pending cross-repo CI access.
- [ ] `output/final.mp4` Video Agent orchestrated acceptance artifact.

Evidence:
- `Video Agent Walking Skeleton` run `32945714649`: SUCCESS.
- Pipeline IR JSON Schema validation: PASS.
- DAG/router/resume tests: PASS.
- Transcript/Storyboard contract tests added and gated in Walking Skeleton CI.
- `Video Agent Real Media Vertical Slice` run `32946222946`: FAILED at sibling private repository checkout BEFORE pipeline execution. This is an infrastructure permission blocker, recorded in `docs/CROSS_REPO_CI_ACCESS.md`; it is not counted as product acceptance.

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
Not DONE because an Agent generated scripts or because lower repositories independently rendered real media. MVP requires one Video Agent-orchestrated real talking-head project from files to `output/final.mp4`, resumable state, provider evidence, edit+motion execution, media/semantic QA, and successful execution from at least two host Agents.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider. ChatCut/Remotion/HyperFrames are providers, not canonical state. No silent semantic downgrade, prompt-only architecture, unnecessary repository, secret-in-source workaround, or Blender/Unreal/full-NLE detour on the critical path.

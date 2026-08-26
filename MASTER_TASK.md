# MASTER TASK — Agent-neutral Video Production Orchestrator

## Objective
Build a production-grade local-first pipeline any compatible host Agent can execute:
`transcript/media → semantic direction → storyboard → Pipeline IR/DAG → provider routing → edit/motion/assets/audio → assembly → QA → final MP4`.

## Current decision
`creator-os-video-agent` is the orchestration Source of Truth above `ai-director-engine` and `motion-runtime-os`. No additional orchestrator repository.

## MT-001 — Contract & Architecture
Status: **DONE FOR V1 CONTRACT**
- [x] Agent-neutral orchestrator definition, PRD v2, research capture, Agent Compatibility Spec, Pipeline IR Spec/Schema.
- [x] Provider and host-adapter registries.
- [x] Talking-head and real-media Pipeline IR graphs.

## MT-002 — Walking Skeleton
Status: **DONE FOR REMOTION REAL-MEDIA VERTICAL SLICE**
- [x] Project-local source/transcript conventions.
- [x] Transcript normalizer and storyboard compiler.
- [x] Real `ai-director-engine` adapter.
- [x] DAG runner with dependency validation, state persistence and resume.
- [x] Capability router with preferred/fallback resolution.
- [x] Runtime failure failover: failed provider attempt is persisted, next compatible provider is tried, and `provider_failovers` evidence is recorded.
- [x] Real FFmpeg ingest/edit/media-QA/export adapter.
- [x] Real Motion Runtime Remotion adapter.
- [x] Artifact/evidence manifest with checksums and lineage.
- [x] `output/final.mp4` Video Agent-orchestrated real-media acceptance.

Evidence:
- Walking Skeleton run `32952129723`: SUCCESS after media asset contract fix.
- Runtime failover contract run `32952946112`: SUCCESS.
- Real Media Vertical Slice run `32952129605`: SUCCESS.
- Final artifact `9600622752`, ~40.8 MB; video+audio probe PASS; artifact upload PASS.

## MT-003 — Editable Edit Provider
Status: **NEXT AFTER MOTION ROUTER + WORKBENCH GATEWAY**
- [ ] ChatCut capability discovery / MCP adapter.
- [ ] Import source media; transcript-based cut jobs; captions/timeline modifications.
- [ ] Export editable project evidence.
- [x] FFmpeg fallback exists without corrupting Pipeline IR.

## MT-004 — Motion Router
Status: **IN PROGRESS**
- [x] Remotion real-media provider.
- [x] HyperFrames real provider adapter implemented through `motion-runtime-os` provider contract.
- [x] Runtime provider failure automatically tries fallback and records failover evidence.
- [x] CLI supports explicit `--motion-provider` while Pipeline IR remains provider-neutral at the semantic level.
- [ ] HyperFrames-first real-media Video Agent acceptance CI PASS.
- [ ] Preserve/cross-check provider semantic QA evidence at orchestrator level.

## MT-005 — Generation Routers
After core edit+motion works: image, video/B-roll, TTS/voice, music, optional avatar contracts. Provider brands never enter canonical Pipeline IR semantics.

## MT-006 — Host-Agent Neutrality
Same canonical fixture must execute under at least two host adapters with equivalent Pipeline IR semantics, durable layout, provider jobs and media QA. Handoff must work from files alone.

## MT-007 — Quality & Human Review
Transcript/timeline sync, media probe, director/motion semantic survival, visual continuity, provider downgrade report, approval gates and human preference evaluation.

## MVP Definition of Done
Current real-media pipeline is product-plumbing accepted for Remotion. Full MVP additionally requires editable workbench consumption, at least two Host Agents, and human-review/quality gates. HyperFrames provider acceptance closes MT-004 but does not alone close the whole MVP.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider. ChatCut/Remotion/HyperFrames are providers, not canonical state. No silent semantic downgrade, prompt-only architecture, unnecessary repository, secret-in-source workaround, or Blender/Unreal/full-NLE detour on the critical path.

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
Status: **DONE FOR REAL-MEDIA VERTICAL SLICE**
- [x] Project-local source/transcript conventions.
- [x] Transcript normalizer and storyboard compiler.
- [x] Real `ai-director-engine` adapter.
- [x] DAG runner with dependency validation, state persistence and resume.
- [x] Capability router with preferred/fallback resolution.
- [x] Runtime failure failover with persisted attempts and `provider_failovers` evidence.
- [x] Real FFmpeg ingest/edit/media-QA/export adapter.
- [x] Artifact/evidence manifest with checksums and lineage.
- [x] `output/final.mp4` Video Agent-orchestrated real-media acceptance.

Evidence:
- Walking Skeleton run `32952129723`: SUCCESS.
- Runtime failover contract run `32952946112`: SUCCESS.
- Remotion Real Media Vertical Slice run `32952129605`: SUCCESS, artifact `9600622752`.

## MT-003 — Editable Edit Provider
Status: **NEXT EDITING BATTLE**
- [ ] ChatCut capability discovery / MCP adapter.
- [ ] Import source media; transcript-based cut jobs; captions/timeline modifications.
- [ ] Export editable project evidence.
- [x] FFmpeg fallback exists without corrupting Pipeline IR.

## MT-004 — Motion Router
Status: **DONE FOR REMOTION + HYPERFRAMES REAL MEDIA**
- [x] Remotion real-media provider.
- [x] HyperFrames real provider adapter through `motion-runtime-os` provider contract.
- [x] Runtime provider failure automatically tries fallback and records failover evidence.
- [x] CLI supports explicit `--motion-provider` without changing canonical semantic intent.
- [x] HyperFrames-first real-media Video Agent acceptance CI PASS.
- [x] Final HyperFrames video+audio probe PASS and artifact uploaded.

Evidence:
- HyperFrames Real Media run `32953105657`: SUCCESS.
- HyperFrames artifact `9600999497`, digest `sha256:f1de4e64bbade8de5ab478bb0686a2446e76ff03340be839ee746c19506969ee`.

## MT-005 — Generation Routers
After editable edit-provider integration: image, video/B-roll, TTS/voice, music, optional avatar contracts. Provider brands never enter canonical Pipeline IR semantics.

## MT-006 — Host-Agent Neutrality
Same canonical fixture must execute under at least two host adapters with equivalent Pipeline IR semantics, durable layout, provider jobs and media QA. Handoff must work from files alone.

## MT-007 — Quality & Human Review
Transcript/timeline sync, media probe, director/motion semantic survival, visual continuity, provider downgrade report, approval gates and human preference evaluation.

## Cross-product dependency — Zhijian M9
`zhijian-ai` now owns the desktop gateway/client surface for starting and observing Video Agent runs. Backend gateway contract CI is green; frontend client/build gate is being added. Zhijian must not duplicate Pipeline IR/DAG/provider semantics.

## MVP Definition of Done
Video production plumbing is accepted across Remotion and HyperFrames. Full MVP still requires editable workbench integration, ChatCut/edit-provider path, at least two Host Agents, and human-review/quality gates.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider. ChatCut/Remotion/HyperFrames are providers, not canonical state. No silent semantic downgrade, prompt-only architecture, unnecessary repository, secret-in-source workaround, or Blender/Unreal/full-NLE detour on the critical path.

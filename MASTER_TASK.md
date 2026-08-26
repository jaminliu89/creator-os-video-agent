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
- Runtime failover contract run `32952946112`: SUCCESS.
- Remotion Real Media Vertical Slice: SUCCESS, artifact `9600622752`.
- HyperFrames Real Media run `32953105657`: SUCCESS, artifact `9600999497`.

## MT-003 — Editable Edit Provider
Status: **IN PROGRESS — AGENT-NEUTRAL EXTERNAL MCP BRIDGE DONE**
- [x] Edit Provider Request/Result v1 machine schemas.
- [x] `editable_output=true` capability gate prevents silent FFmpeg downgrade.
- [x] ChatCut represented as editable external MCP provider, not an orchestrator.
- [x] Agent-neutral ChatCut request/result file bridge.
- [x] New durable state `waiting_external` for MCP/browser/human handoffs.
- [x] Explicit `resume_external()` semantics; no busy-loop and no false provider failure.
- [x] Request/result identity, editable artifact and verification checks.
- [x] External handoff evidence persisted in `external_handoffs`.
- [x] Any Host Agent can fulfill the same request through ChatCut MCP without changing Pipeline IR.
- [ ] Execute against a live authenticated ChatCut MCP surface and capture a real editable project artifact.
- [ ] Verify transcript cuts/captions/timeline modifications against a real source project.
- [ ] Verify editable project reopen/round-trip and preview/export evidence.

Evidence:
- Walking Skeleton run `32956377710`: SUCCESS, including `tests/test_external_edit_bridge.py`.

## MT-004 — Motion Router
Status: **DONE FOR REMOTION + HYPERFRAMES REAL MEDIA**
- [x] Remotion real-media provider.
- [x] HyperFrames real provider adapter through `motion-runtime-os` provider contract.
- [x] Runtime provider failure automatically tries fallback and records failover evidence.
- [x] CLI supports explicit `--motion-provider` without changing canonical semantic intent.
- [x] HyperFrames-first real-media Video Agent acceptance CI PASS.
- [x] Final HyperFrames video+audio probe PASS and artifact uploaded.

## MT-005 — Generation Routers
After live editable edit-provider acceptance: image, video/B-roll, TTS/voice, music, optional avatar contracts. Provider brands never enter canonical Pipeline IR semantics.

## MT-006 — Host-Agent Neutrality
Status: **PARTIAL — FILE HANDOFF CONTRACT NOW EXISTS**
Same canonical fixture must execute under at least two Host Agents with equivalent Pipeline IR semantics. `waiting_external` + request/result files now make cross-Agent handoff deterministic; live two-host acceptance remains.

## MT-007 — Quality & Human Review
Status: **PARTIAL VIA ZHIJIAN**
Transcript/timeline sync, media probe, director/motion semantic survival, provider downgrade report, approval gates and human preference evaluation. Zhijian now records append-only approve/reject/override events with provenance.

## Cross-product dependency — Zhijian M9
`zhijian-ai` now has a real Video Agent product surface:
- starts and observes Video Agent runs;
- streams `final.mp4` for local preview;
- imports Motion IR + Director IR + Evidence into its real Timeline Store;
- preserves `artifactId / producerJob / provider / directorIntentRefs / motionLayerId` provenance;
- exposes human approve/reject;
- Clip timing edits generate provenance-aware override events before local state mutation.

Latest Zhijian integration run `32956028759`: SUCCESS.

## MVP Definition of Done
Video production plumbing is accepted across Remotion and HyperFrames, and Zhijian human takeover is wired. Full MVP still requires live ChatCut editable-project acceptance and at least two real Host Agents executing the same canonical handoff.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider. ChatCut/Remotion/HyperFrames are providers, not canonical state. No silent semantic downgrade, prompt-only architecture, unnecessary repository, secret-in-source workaround, or Blender/Unreal/full-NLE detour on the critical path.

# MASTER TASK — Agent-neutral Video Production Orchestrator

## Objective
Build a production-grade local-first pipeline any compatible host Agent can execute:
`transcript/media → semantic direction → storyboard → Pipeline IR/DAG → provider routing → edit/motion/assets/audio → assembly → QA → final MP4`.

## Product decision — 2026-08-26
The canonical MVP must NOT depend on paid ChatCut execution. ChatCut is **OPTIONAL_PROVIDER / BENCHMARK**. Primary differentiation is local-first Semantic Motion/MG Intelligence:
`Director IR → MG Plan/Motion Grammar → Motion IR → HyperFrames | Motion Canvas | Remotion → Zhijian human takeover`.

## MT-001 — Contract & Architecture
Status: **DONE FOR V1 CONTRACT**
- [x] Agent-neutral orchestrator, PRD, Pipeline IR Schema, provider/host registries.

## MT-002 — Walking Skeleton
Status: **DONE FOR REAL-MEDIA VERTICAL SLICE**
- [x] Real `ai-director-engine` adapter, DAG/resume/router/failover, FFmpeg, artifact/evidence lineage, final MP4.
- [x] Remotion and HyperFrames real-media acceptance.

## MT-003 — Editable Edit Provider
Status: **OPTIONAL INTEGRATION — CORE CONTRACT DONE**
- [x] Edit Provider Request/Result v1 schemas.
- [x] `editable_output=true` prevents silent FFmpeg downgrade.
- [x] `waiting_external` + explicit resume + external handoff evidence.
- [x] ChatCut request/result bridge remains available for users who have ChatCut.
- [ ] Live ChatCut authenticated round-trip is optional evidence, not MVP blocker.

## MT-004 — Motion Router
Status: **DONE FOR REMOTION + HYPERFRAMES REAL MEDIA**
- [x] Real Remotion + HyperFrames providers, runtime failover, media QA and artifacts.

## MT-005 — Motion / MG Intelligence — CURRENT PRIMARY BATTLE
Goal: produce impressive knowledge/talking-head/brand MG locally without paid NLE dependency.
- [x] Composable Motion Grammar + restraint policy.
- [x] Provider-neutral MG Plan v1 Schema.
- [x] Semantic MG Planner: Director IR → differentiated grammar plan.
- [x] MG Plan → Motion IR compiler.
- [x] Typography execution baseline: hero text, keyword isolation, animated number counter.
- [x] Diagram/data execution baseline: animated bar chart, before/after comparison, process/callout flow.
- [x] Rhythm/spatial execution baseline: veil/negative-space behavior, impact light, camera push-in.
- [x] MG QA: grammar-family diversity, effect density, exposition restraint, attention target and timing checks.
- [x] Real 20s vertical source → Neutral baseline + Directed MG → local Remotion MP4 with preserved source audio.
- [x] A/B artifacts packaged together for human preference review.
- [ ] Blind preference evaluation: Directed must show measurable preference lift vs Neutral; collect qualitative failure tags.
- [ ] HyperFrames executes the expanded MG grammar with semantic parity, not only established Motion IR subset.
- [ ] Motion Canvas provider discovery/contract/real render for diagram/vector specialist role.
- [ ] Expand grammar execution: line chart, timeline/node graph, document/UI, mask/morph transitions.
- [ ] Zhijian exposes MG Plan/grammar provenance and per-effect human override.

Evidence:
- `motion-runtime-os` MG Intelligence run `32965740388`: SUCCESS — planner/compiler/schema/MG-QA/renderer-build PASS.
- Directed MG A/B Real Media run `32965688798`: SUCCESS — pinned source, semantic compile, Neutral+Directed local renders, video/audio probes and artifact upload PASS.
- A/B artifact `9605679296`, ~59.2 MB, digest `sha256:0acf5fd570e63828ac521ba1bce36236a13fae6d3e0b40da6f8d9fa95aef042b`.

## MT-006 — Generation Routers
After MG quality acceptance: optional image/video B-roll, TTS/voice, music/avatar providers. Local/no-cost paths preferred where quality permits.

## MT-007 — Host-Agent Neutrality
Status: **PARTIAL**
File contracts and external handoff semantics exist; two real Host Agents must still execute the same canonical fixture.

## MT-008 — Quality & Human Review
Status: **IN PROGRESS**
Media/semantic QA, MG restraint/density QA and append-only Zhijian approve/reject/override evidence exist. Human blind preference is now the primary unresolved quality gate.

## Zhijian M9
Core human takeover is accepted: start/observe pipeline, local final preview, Timeline Store import, provenance, approve/reject and provenance-aware Clip override. Next: import MG Plan/grammar provenance and support per-effect edits.

## MVP Definition of Done
The local pipeline no longer depends on ChatCut and already renders a real Directed MG A/B pair. MVP quality closure now requires Directed > Neutral human preference evidence, expanded MG parity across the chosen local providers, and Zhijian per-effect takeover. ChatCut remains an optional editable NLE adapter.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider. Renderers do not decide narrative meaning. No template-ID architecture, silent semantic downgrade, paid-provider release dependency, prompt-only state, or decorative animation on every sentence.

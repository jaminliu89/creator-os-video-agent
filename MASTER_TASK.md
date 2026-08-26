# MASTER TASK — Agent-neutral Video Production Orchestrator

## Objective
Build a production-grade local-first pipeline any compatible host Agent can execute:
`transcript/media → semantic direction → storyboard → Pipeline IR/DAG → provider routing → edit/motion/assets/audio → assembly → QA → final MP4`.

## Product decision — 2026-08-26
The canonical MVP must NOT depend on paid ChatCut execution. ChatCut is now **OPTIONAL_PROVIDER / BENCHMARK**, not a release blocker. Our primary differentiation is a local-first Semantic Motion/MG Intelligence stack:
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
- [x] `motion-runtime-os/docs/MG_INTELLIGENCE_SPEC.md` defines composable motion grammar and restraint policy.
- [x] Provider-neutral `MG Plan v1` machine schema.
- [x] Deterministic Semantic MG Planner baseline maps Director IR → grammar plan.
- [x] Planner tests enforce revelation/contrast/question differentiation and exposition restraint.
- [ ] MG Plan → Motion IR compiler.
- [ ] Typography grammar execution: kinetic text, keyword isolation, number counter, mask reveal.
- [ ] Diagram/data grammar execution: bar/line/comparison/process/callout.
- [ ] Rhythm/spatial execution: freeze, negative space, push/pull, focus isolation, semantic transitions.
- [ ] HyperFrames-first real 20–40s directed MG acceptance with source audio.
- [ ] Subtitle-only neutral baseline vs Directed MG blind preference evaluation.
- [ ] Motion Canvas provider discovery/contract/real render for diagram/vector specialist role.
- [ ] Zhijian exposes MG Plan/grammar provenance and per-effect human override.

## MT-006 — Generation Routers
After MG Intelligence acceptance: optional image/video B-roll, TTS/voice, music/avatar providers. Local/no-cost paths preferred where quality permits.

## MT-007 — Host-Agent Neutrality
Status: **PARTIAL**
File contracts and external handoff semantics exist; two real Host Agents must still execute the same canonical fixture.

## MT-008 — Quality & Human Review
Status: **PARTIAL VIA ZHIJIAN**
Media/semantic QA plus append-only approve/reject/override evidence exists. Add MG-specific attention, restraint, temporal alignment, continuity and human preference gates.

## Zhijian M9
Core human takeover is accepted: start/observe pipeline, local final preview, Timeline Store import, provenance, approve/reject and provenance-aware Clip override.

## MVP Definition of Done
MVP no longer requires ChatCut. It requires one real 20–40s source segment to run through Director → MG Planner → local motion providers → final MP4 → Zhijian takeover, with source audio preserved, semantic/restraint QA and a directed-vs-neutral human preference result. ChatCut remains an optional editable NLE adapter.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider. Renderers do not decide narrative meaning. No template-ID architecture, silent semantic downgrade, paid-provider release dependency, prompt-only state, or decorative animation on every sentence.

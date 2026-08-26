# MASTER TASK — Agent-neutral Video Production Orchestrator

## Objective
Build a production-grade local-first pipeline any compatible host Agent can execute:
`transcript/media → semantic direction → storyboard → Pipeline IR/DAG → provider routing → edit/motion/assets/audio → assembly → QA → final MP4`.

## Product decision — 2026-08-26
The canonical MVP must NOT depend on paid ChatCut execution. ChatCut is **OPTIONAL_PROVIDER / BENCHMARK**. Primary differentiation is local-first Semantic Motion/MG Intelligence:
`Director IR → MG Plan/Motion Grammar → Motion IR → Remotion | HyperFrames → Zhijian human takeover`.

Motion Canvas remains EXPERIMENTAL / future diagram specialist until unattended headless rendering is proven in CI.

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
- [x] HyperFrames executes the expanded MG grammar (`bar_chart`, `comparison`, `process_flow`, `hero_text`, `number_counter`, `veil`) from the same Motion IR in strict mode with preserved source audio.
- [x] Reproducible concealed A/B package builder + preference scorer.
- [~] Blind preference evaluation: infrastructure DONE; real reviewer votes and measurable Directed preference lift remain.
- [~] Motion Canvas: provider decision + strict entry gate DONE; real unattended headless render not yet verified.
- [ ] Expand grammar execution: line chart, timeline/node graph, document/UI, mask/morph transitions.
- [~] Zhijian MG takeover: grammar provenance visible/preserved in Override Evidence; richer per-effect parameter controls remain.

Evidence:
- `motion-runtime-os` MG Intelligence run `32965740388`: SUCCESS — planner/compiler/schema/MG-QA/renderer-build PASS.
- Directed MG A/B run `32974061233`: SUCCESS — Neutral+Directed local renders, source-audio probes, concealed study pack PASS. Artifact `9608852317`, digest `sha256:57509aad783224d96dda01c81739058577f456f83437d3a10d277d6bc8f35621`.
- Directed MG HyperFrames run `32974210663`: SUCCESS — strict HyperFrames render + MG semantic parity + media probe PASS. Artifact `9608898870`, digest `sha256:b0ad4ca884a81b1c5b56b0b5796fa2856b7fe029aafe9279cfaec4ccdeedbcd9`.

## MT-006 — Generation Routers
After MG quality acceptance: optional image/video B-roll, TTS/voice, music/avatar providers. Local/no-cost paths preferred where quality permits.

## MT-007 — Host-Agent Neutrality
Status: **PARTIAL**
File contracts and external handoff semantics exist; two real Host Agents must still execute the same canonical fixture.

## MT-008 — Quality & Human Review
Status: **IN PROGRESS**
Media/semantic QA, MG restraint/density QA, concealed A/B study packaging and append-only Zhijian approve/reject/override evidence exist. Real blind human preference is now the primary unresolved quality gate.

## Zhijian M9
Core human takeover is accepted: start/observe pipeline, local final preview, Timeline Store import, MG provenance, approve/reject and provenance-aware Clip override. Next: richer per-effect parameter edits and preference feedback ingestion.

## MVP Definition of Done
The local pipeline no longer depends on ChatCut, and expanded MG semantics now execute through both verified local providers. MVP quality closure now requires Directed > Neutral human preference evidence, broader grammar/style quality, and richer Zhijian per-effect takeover. ChatCut remains an optional editable NLE adapter.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider. Renderers do not decide narrative meaning. No template-ID architecture, silent semantic downgrade, paid-provider release dependency, prompt-only state, or decorative animation on every sentence.

# MASTER TASK — Agent-neutral Video Production Orchestrator

## Objective
Build a production-grade local-first pipeline any compatible host Agent can execute:
`transcript/media → semantic direction → storyboard → Pipeline IR/DAG → provider routing → edit/motion/assets/audio → assembly → QA → final MP4`.

## Product decision — 2026-08-26
The canonical MVP does NOT depend on paid ChatCut execution. ChatCut is **OPTIONAL_PROVIDER / BENCHMARK**. Verified differentiation is now:
`Director IR → MG Planner → Art Direction → Motion IR → Remotion | HyperFrames → QA → Zhijian takeover → Preference Evidence`.

Motion Canvas remains EXPERIMENTAL / future diagram specialist until unattended headless CI rendering is proven.

## MT-001 — Contract & Architecture
Status: **DONE FOR V1 CONTRACT**
- [x] Agent-neutral orchestrator, PRD, Pipeline IR Schema, provider/host registries.

## MT-002 — Walking Skeleton
Status: **DONE FOR REAL-MEDIA VERTICAL SLICE**
- [x] Real `ai-director-engine` adapter, DAG/resume/router/failover, FFmpeg, artifact/evidence lineage, final MP4.
- [x] Remotion and HyperFrames real-media acceptance.

## MT-003 — Editable Edit Provider
Status: **OPTIONAL INTEGRATION — CORE CONTRACT DONE**
- [x] Edit Provider Request/Result v1 schemas, `editable_output` safety, external handoff/resume.
- [x] ChatCut request/result bridge retained for users with ChatCut.
- [ ] Live ChatCut authenticated round-trip is optional evidence, not MVP blocker.

## MT-004 — Motion Router
Status: **DONE FOR REMOTION + HYPERFRAMES REAL MEDIA**
- [x] Real providers, runtime failover, media QA, semantic mapping and artifacts.

## MT-005 — Motion / MG / Art Direction Intelligence
Status: **ENGINEERING CORE DONE; TASTE LEARNING IN PROGRESS**
- [x] Composable Motion Grammar + restraint policy + MG Plan v1.
- [x] Semantic MG Planner + MG Plan → Motion IR compiler.
- [x] Typography/data/diagram/rhythm execution and MG QA.
- [x] Real Neutral vs Directed A/B with source audio.
- [x] Remotion + HyperFrames execute the same Directed MG semantics in strict/local mode.
- [x] Reproducible concealed A/B package + scorer.
- [x] Art Direction Engine v1 with `editorial_restraint`, `precision_tech`, `kinetic_signal`.
- [x] Semantic invariance: style may change palette/type/geometry/rhythm/intensity but not narrative function, attention target or grammar.
- [x] All three styles render real media through Remotion; `precision_tech` same Motion IR also renders through HyperFrames.
- [x] Expanded cross-provider grammar: `line_chart`, `timeline`, `node_graph`, `document_highlight`, `browser_frame`, `mask_reveal/hero_text`.
- [x] Zhijian imports MG + Art Direction provenance and preserves it in human Override Evidence.
- [~] Human blind preference: infrastructure DONE; real reviewer votes and measurable preference lift pending.
- [ ] Style Selection Intelligence: choose art direction from content/audience/brand/context automatically.
- [ ] Preference Learning: convert blind votes and Zhijian overrides into typed/reversible preference signals.
- [ ] Advanced composition: semantic morph/mask transitions, spatial continuity, richer maps/charts/UI/doc choreography.
- [~] Rich Zhijian per-effect controls: provenance exists; parameter-level visual editing remains.

### MT-005 Evidence
- MG Intelligence/Art Direction semantic gate `32975984410`: SUCCESS.
- Directed MG A/B `32974061233`: SUCCESS; artifact `9608852317`, digest `sha256:57509aad783224d96dda01c81739058577f456f83437d3a10d277d6bc8f35621`.
- Directed MG HyperFrames `32974210663`: SUCCESS; artifact `9608898870`, digest `sha256:b0ad4ca884a81b1c5b56b0b5796fa2856b7fe029aafe9279cfaec4ccdeedbcd9`.
- Art Direction real-media `32976364819`: SUCCESS; all 3 Remotion profiles + HyperFrames precision parity; artifact `9609809535`, digest `sha256:ef897ef254682c5f333cadeda98939aea3760ec89a950f356481786601bc624d`.
- Expanded MG cross-provider `32976405003`: SUCCESS; Remotion + HyperFrames exact same Motion IR, source audio and semantic mapping PASS; artifact `9609855462`, digest `sha256:0b7120ceee9f975ddee782a31e15b674e3a73b7a1f6e04004b9428c4e356bc97`.
- Zhijian Art Direction provenance `32976886488`: SUCCESS; Python contracts + frontend build PASS.

## MT-006 — Generation Routers
After taste/quality acceptance: optional image/video B-roll, TTS/voice, music/avatar providers. Local/no-cost paths preferred where quality permits.

## MT-007 — Host-Agent Neutrality
Status: **PARTIAL**
File contracts and external handoff semantics exist; two real Host Agents must still execute the same canonical fixture.

## MT-008 — Quality & Human Review
Status: **IN PROGRESS — PRIMARY QUALITY GATE**
Machine/media/semantic/restraint/style evidence is strong. The unresolved question is now taste: real humans must prefer Directed/Styled output over neutral or provide structured failure tags.

## Zhijian M9
Core human takeover is accepted: start/observe, final preview, Timeline Store import, MG/Art Direction provenance, approve/reject and provenance-aware override. Next: parameter-level style/effect editing and typed preference feedback ingestion.

## MVP Definition of Done
Technical MG/style execution is no longer the blocker. MVP quality closure requires credible human preference evidence and a feedback loop that improves style/grammar selection without silently rewriting canonical assets. ChatCut remains optional.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider. Renderers do not decide narrative meaning. Art Direction restyles but cannot rewrite semantics. No template-ID architecture, silent downgrade, paid-provider release dependency, prompt-only state, or decorative animation on every sentence.

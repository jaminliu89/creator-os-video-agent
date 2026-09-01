# MASTER TASK — Agent-neutral Video Production Orchestrator

## Objective
Build a production-grade local-first pipeline any compatible host Agent can execute:
`transcript/media → semantic direction → Beat Graph → Visual Decision → Director Timeline → Pipeline IR/DAG → provider routing → edit/motion/assets/audio → assembly → QA → final MP4`.

## Product decision — 2026-09-02
MoneyPrinterTurbo is **INFRASTRUCTURE CANDIDATE / RENDERER REFERENCE**, not Director Core.

We will absorb useful media-plumbing patterns while keeping semantic direction inside AI Director Engine + Director Timeline.

Canonical differentiation:
`Director IR → Beat Graph → Visual Decision → Director Timeline → MG/Asset/Audio Routing → Remotion | HyperFrames | FFmpeg | optional adapters → QA → Human Preference Evidence`.

ChatCut remains OPTIONAL_PROVIDER / BENCHMARK. MoneyPrinterTurbo remains OPTIONAL_INFRASTRUCTURE_REFERENCE. Neither may become a semantic single point of truth.

## MT-001 — Contract & Architecture
Status: **DONE FOR V2 CONTRACT**
- [x] Agent-neutral orchestrator, PRD, Pipeline IR Schema, provider/host registries.
- [x] Director Timeline v1 schema added.
- [x] Visual Decision layer made explicit between Director IR and Pipeline IR.
- [x] Renderer/media infrastructure separated from director semantics.

## MT-002 — Walking Skeleton
Status: **DONE FOR REAL-MEDIA VERTICAL SLICE; DIRECTOR TIMELINE INTEGRATION NEXT**
- [x] Real `ai-director-engine` adapter, DAG/resume/router/failover, FFmpeg, artifact/evidence lineage, final MP4.
- [x] Remotion and HyperFrames real-media acceptance.
- [ ] Emit `director-timeline.json` from the existing Director/Beat path and compile it into current Pipeline IR without semantic loss.

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
- [x] Expanded cross-provider grammar: `line_chart`, `timeline`, `node_graph`, `document_highlight`, `browser_frame`, `mask_reveal/hero_text`.
- [~] Human blind preference: infrastructure DONE; real reviewer votes and measurable preference lift pending.
- [ ] Style Selection Intelligence.
- [ ] Preference Learning.
- [ ] Advanced composition and richer maps/charts/UI/doc choreography.

## MT-006 — Generation Routers
Status: **INTERFACES RESERVED; QUALITY-GATED**
- [ ] Stock/media adapter interface using Director Timeline `asset_query` and `purpose`, not raw keyword matching.
- [ ] Optional Pexels/Pixabay/Coverr-style providers.
- [ ] Optional image/video generation providers.
- [ ] Optional HeyGen/D-ID-compatible digital-human providers.
- [ ] Optional TTS/music/SFX providers.

## MT-007 — MoneyPrinterTurbo Absorption
Status: **DOCUMENTATION + CONTRACT DONE; CODE EXTRACTION NOT STARTED**
- [x] Competitor Capture added: `docs/benchmarks/MONEYPRINTERTURBO_CAPTURE.md`.
- [x] Benchmark Registry added: `registries/benchmarks.v1.json`.
- [x] NOW/LATER/IGNORE decisions recorded.
- [x] Deployment-vs-director diagnosis matrix added.
- [x] Architecture/PRD updated so MoneyPrinterTurbo-like modules sit below Director Timeline.
- [ ] Implement provider-neutral media infrastructure interfaces for stock search, subtitle timing, TTS timing, FFmpeg assembly and batch execution.
- [ ] Only after interfaces exist, evaluate code-level reuse/license/maintenance economics.
- [ ] Do not fork MoneyPrinterTurbo as the main product.

## MT-008 — Neutral vs Directed Benchmark
Status: **NEXT QUALITY CLOSURE**
Use one identical transcript/source fixture.

Baseline A:
`keyword/stock assembly → render`.

Directed B:
`Beat Graph → Visual Decision → Director Timeline → providers → render`.

Measure:
- semantic alignment per beat;
- temporal alignment;
- visual redundancy;
- attention control;
- pacing/contrast;
- manual corrections per minute;
- blind human preference.

Do not claim Director superiority before preference evidence exists.

## MT-009 — Host-Agent Neutrality
Status: **PARTIAL**
File contracts and external handoff semantics exist; two real Host Agents must still execute the same canonical fixture.

## MT-010 — Quality & Human Review
Status: **IN PROGRESS — PRIMARY QUALITY GATE**
Machine/media/semantic/restraint/style evidence is strong. The unresolved question is taste: real humans must prefer Directed/Styled output over neutral or provide structured failure tags.

## Immediate executable slice
1. Existing Director/Beat output emits valid `schemas/director-timeline.v1.schema.json`.
2. Pipeline compiler consumes Director Timeline and emits current jobs.
3. Add one local/zero-cost asset lookup adapter or fixture adapter.
4. Render identical Neutral vs Directed test video.
5. Produce evidence package with timing + semantic mappings + human review ballot.

## MVP Definition of Done
Technical render success is not the blocker. MVP quality closure requires:
- Director Timeline as a real runtime artifact, not documentation only;
- at least edit + motion + asset/media-infrastructure routing;
- semantic/temporal QA;
- credible Neutral vs Directed preference evidence;
- feedback loop that improves selection without silently rewriting canonical assets.

## Constraints
Host Agent ≠ Director ≠ Orchestrator ≠ Provider ≠ Renderer.
Renderers do not decide narrative meaning.
Art Direction restyles but cannot rewrite semantics.
No template-ID architecture, silent downgrade, paid-provider release dependency, prompt-only state, keyword-stock-as-director-core, or decorative animation on every sentence.

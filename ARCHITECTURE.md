# Architecture — Agent-neutral Video Production Orchestrator

## Architectural decision
`creator-os-video-agent` is the orchestration plane above `ai-director-engine` and `motion-runtime-os`.

The canonical separation is now:

```text
Host Agent Layer
Codex | Claude | WorkBuddy | Hermes | Pi | other
                ↓
Agent Adapter / Capability Discovery
                ↓
Project Workspace + State Machine
                ↓
Script / Transcript / Source Media
                ↓
AI Director Engine
                ↓
Beat Graph + Director IR
                ↓
Visual Decision Engine
                ↓
Director Timeline
                ↓
Pipeline Compiler
                ↓
Pipeline IR / Job DAG
        ┌───────┼───────────┬───────────┐
        ↓       ↓           ↓           ↓
      Edit    Motion      Assets       Audio
   ChatCut    Remotion    Stock        TTS
   FFmpeg     HyperFrames Image/Video  Music/SFX
                         Avatar
        └───────┼───────────┴───────────┘
                ↓
Asset Router + Timeline Assembly
                ↓
Renderer / Media Infrastructure
 FFmpeg | provider adapters | MoneyPrinterTurbo-like primitives
                ↓
Render + Quality Gate
                ↓
Final MP4 + Evidence + Editable State
```

## Core separation
### Host Agent
Reasoning/execution host. Replaceable.

### Director Engine
Owns **why/what**: narrative intent, attention, pacing, shot/edit/camera/motion/audio/B-roll intent.

### Visual Decision Engine
Converts beat semantics into an explicit treatment decision. It decides whether a beat should use A-roll, B-roll, still image, AI image, AI video, MG motion, kinetic text, chart, screen recording, UI demo, digital human, black frame, hold existing, or intentionally no replacement.

### Director Timeline
The durable bridge between directing and execution. Schema: `schemas/director-timeline.v1.schema.json`.

A Director Timeline binds each beat to:
- exact time range;
- narrative function;
- emotion and attention target;
- pacing;
- visual mode and purpose;
- asset query/refs;
- motion intent and text emphasis;
- music/SFX/silence decisions;
- provider constraints and fallbacks;
- QA expectations.

### Orchestrator
Owns **when/how-to-route**: DAG state, job creation, provider choice, retries, handoff, artifact dependencies and acceptance.

### Provider
Executes a bounded capability. Examples: ChatCut NLE, FFmpeg media primitive, Remotion/HyperFrames motion, image/video generation, stock providers, TTS, music, avatar/digital-human providers.

### Renderer / Media Infrastructure
Owns codec/media plumbing only. It must not invent narrative meaning. MoneyPrinterTurbo is classified here as an infrastructure/renderer reference, not as Director Core. Reusable patterns include TTS timing, stock-media adapters, subtitle/transcription plumbing, batch jobs and FFmpeg assembly.

## Canonical project layout
```text
project/
  input/
    transcript.md
    brief.md
    media/
  state/
    transcript.json
    beat-graph.json
    director-ir.json
    director-timeline.json
    storyboard.json
    pipeline-ir.json
    run-state.json
  jobs/
    edit/
    motion/
    visual/
    audio/
    assemble/
  assets/
  providers/
  evidence/
  output/
    final.mp4
```

## State machine
`INGEST → NORMALIZE → DIRECT → VISUAL_DECIDE → TIMELINE → PLAN → ROUTE → EXECUTE → ASSEMBLE → QA → REVIEW → DELIVER`

Every transition writes durable state. A new agent session resumes from files rather than reconstructing decisions from chat history.

## Pipeline IR
Pipeline IR is not Motion IR, Director IR or Director Timeline. It describes executable production jobs and dependencies.

Minimum job fields:
- `job_id`
- `kind`: edit | motion | visual | audio | assemble | qa | export
- `input_refs`
- `output_refs`
- `time_range`
- `intent_ref`
- `capability_requirements`
- `preferred_provider`
- `fallback_providers`
- `status`
- `attempts`
- `evidence_refs`

## Provider router
Score candidates by:
`capability + semantic fidelity + editability + determinism + latency + cost + privacy + availability`.

Examples:
- transcript cleanup / editable timeline → ChatCut preferred where available, FFmpeg fallback for deterministic cuts;
- kinetic text / charts / React UI → Remotion;
- web-native motion / GSAP / HTML / Three.js → HyperFrames;
- missing B-roll → stock/search/generation adapter chosen from Director Timeline purpose;
- avatar/digital human → HeyGen, D-ID or compatible adapter;
- mux/probe/transcode → FFmpeg;
- MoneyPrinterTurbo-like modules → optional media-infrastructure adapters only.

## MoneyPrinterTurbo decision
See `docs/benchmarks/MONEYPRINTERTURBO_CAPTURE.md` and `registries/benchmarks.v1.json`.

Decision:
- absorb infrastructure patterns;
- do not fork it into the product core;
- do not use keyword-to-stock matching as Visual Decision Intelligence;
- benchmark Neutral stock assembly against Directed output using human preference evidence.

## Deployment vs director defects
Before tuning providers, use `docs/DEPLOYMENT_VS_DIRECTOR_DIAGNOSIS.md`.

Rule: codec, bitrate, hardware acceleration and timestamp fixes may repair deployment defects; they cannot repair missing narrative function, visual purpose, pacing or attention control.

## Agent portability
Canonical logic must live in schemas, Skills, CLI contracts, MCP/tool manifests, project files and state-machine rules. Host adapters only translate conventions into the same runtime operations.

## Failure model
No silent fallback. Unsupported semantics produce structured downgrade/failure records. Retry policy is bounded. Every external-generation job records model/provider/input/output metadata.

## Quality model
Separate:
1. execution success;
2. contract conformance;
3. semantic preservation;
4. temporal alignment;
5. visual/audio quality;
6. human preference.

A renderer returning MP4 only satisfies item 1.

# Architecture — Agent-neutral Video Production Orchestrator

## Architectural decision
`creator-os-video-agent` is the orchestration plane above `ai-director-engine` and `motion-runtime-os`.

```text
Host Agent Layer
Codex | Claude | WorkBuddy | Hermes | Pi | other
                ↓
Agent Adapter / Capability Discovery
                ↓
Project Workspace + State Machine
                ↓
Semantic Director / Director IR
                ↓
Pipeline Compiler
                ↓
Pipeline IR / Job DAG
        ┌───────┼────────┬────────┐
        ↓       ↓        ↓        ↓
      Edit    Motion    Assets   Audio
   ChatCut    Remotion  Image    TTS
   FFmpeg     HyperFrames Video  Music
        └───────┼────────┴────────┘
                ↓
Artifact Graph / Timeline Assembly
                ↓
Render + Quality Gate
                ↓
Final MP4 + Evidence
```

## Core separation
### Host Agent
Reasoning/execution host. It may read/write files and invoke tools. It is replaceable.

### Director Engine
Owns why/what: narrative intent, attention, pacing, shot/edit/camera/motion/audio/B-roll intent.

### Orchestrator
Owns when/how-to-route: DAG state, job creation, provider choice, retries, handoff, artifact dependencies and acceptance.

### Provider
Owns execution of a bounded capability. Examples: ChatCut NLE, FFmpeg media primitive, Remotion/HyperFrames motion, image/video generation, TTS, music.

## Canonical project layout
```text
project/
  input/
    transcript.md
    brief.md
    media/
  state/
    transcript.json
    director-ir.json
    storyboard.json
    pipeline-ir.json
    run-state.json
  jobs/
    edit/
    motion/
    visual/
    audio/
  assets/
  providers/
  evidence/
  output/
    final.mp4
```

## State machine
`INGEST → NORMALIZE → DIRECT → PLAN → ROUTE → EXECUTE → ASSEMBLE → QA → REVIEW → DELIVER`

Every transition writes durable state. A new agent session must resume from files rather than reconstructing decisions from chat history.

## Pipeline IR
Pipeline IR is not Motion IR and not Director IR. It describes executable production jobs and dependencies.

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
- transcript cleanup / editable timeline → ChatCut preferred, FFmpeg fallback for deterministic cuts;
- kinetic text / charts / React UI → Remotion;
- web-native motion / GSAP / HTML / Three.js → HyperFrames;
- missing B-roll → generation provider;
- mux/probe/transcode → FFmpeg.

## Agent portability
Canonical logic must live in:
- schemas;
- Skills;
- CLI contracts;
- MCP/tool manifests;
- project files;
- state machine rules.

Codex/Claude/WorkBuddy/Hermes/Pi adapters only translate host conventions into the same runtime operations.

## Failure model
No silent fallback. Unsupported semantics produce structured downgrade/failure records. Retry policy is bounded. Every external-generation job records model/provider/input/output metadata.

## Quality model
Separate:
1. execution success;
2. contract conformance;
3. semantic preservation;
4. visual/audio quality;
5. human preference.

A renderer returning MP4 only satisfies item 1.

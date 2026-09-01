# Creator OS Video Agent

## Product definition

**Agent-neutral Video Production Orchestrator** — a local-first production protocol that lets Codex, Claude Code, WorkBuddy, Hermes, Pi and other capable agents run the same video workflow without binding the system to one model or one editor.

It is not another timeline editor, not another renderer, and not another keyword-to-stock video generator.

It owns:

`input → transcript → Beat Graph / Director IR → Visual Decision → Director Timeline → Pipeline IR → provider routing → render → QA → deliverables`

## Repository boundary

- `ai-director-engine` = understand/reason/decide, emits Director IR / beat semantics.
- `creator-os-video-agent` = converts semantic decisions into Director Timeline, orchestrates the production graph and routes providers.
- `motion-runtime-os` = executes Motion IR through Remotion / HyperFrames and verifies artifacts.
- ChatCut = optional editable NLE/editing provider.
- FFmpeg = deterministic local media primitive / renderer infrastructure.
- Remotion / HyperFrames = programmatic motion/render providers.
- Image/video/TTS/music/avatar systems = optional providers behind adapters.
- MoneyPrinterTurbo = benchmark + media-infrastructure reference only; useful plumbing patterns may be absorbed, but it does not own Director semantics.

## Canonical pipeline

```text
input/transcript.md + media/
        ↓
Ingest / Transcript Normalize
        ↓
AI Director Engine
        ↓
Beat Graph + Director IR
        ↓
Visual Decision Engine
        ↓
Director Timeline
        ↓
Pipeline IR / Job DAG
   ┌────┼──────────┬───────────┬───────────┐
   ↓    ↓          ↓           ↓
 Edit  Motion     Assets      Audio
ChatCut Remotion  Stock       TTS/Music/SFX
FFmpeg HyperFrames Image/Video Avatar
   └────┴──────────┴───────────┴───────────┘
        ↓
Timeline / Composition Assembly
        ↓
Renderer / Media Infrastructure
        ↓
QA: timing / semantic / media / visual / preference
        ↓
output/final.mp4 + evidence/
```

## Director Timeline

`schemas/director-timeline.v1.schema.json` is the durable bridge between “the AI understands the sentence” and “the renderer executes the correct visual action”.

It can explicitly choose:
A-roll, B-roll, still image, AI image, AI video, MG motion, kinetic text, chart, screen recording, UI demo, digital human, black frame, hold-existing, or intentional none.

This prevents the system from defaulting every sentence to generic stock footage.

## MoneyPrinterTurbo benchmark

The benchmark is documented in:
- `docs/benchmarks/MONEYPRINTERTURBO_CAPTURE.md`
- `registries/benchmarks.v1.json`
- `docs/DEPLOYMENT_VS_DIRECTOR_DIAGNOSIS.md`

Decision: reuse infrastructure ideas where useful; do not fork it into the main product and do not use keyword-to-stock matching as the director brain.

## Agent contract

A host agent is compatible when it can provide enough of these capabilities:
1. read/write project files;
2. execute approved local commands/CLI;
3. call MCP/HTTP tools when configured;
4. load Skills/instructions;
5. observe command/tool results and continue an Agent Loop.

Canonical workflow logic belongs in files/schemas/skills, not a host-specific prompt.

## Current objective

Close one reproducible Neutral-vs-Directed vertical slice where the same transcript is rendered through:

- Neutral baseline: keyword/stock-style assembly;
- Directed path: Beat Graph → Director Timeline → asset/motion routing.

Success is measured by semantic alignment, temporal alignment, reduced redundancy, manual corrections per minute and blind human preference — not simply “MP4 rendered successfully”.

See `PRD.md`, `ARCHITECTURE.md`, `MASTER_TASK.md`, `AGENT_HANDOFF.md`, `schemas/` and `docs/`.

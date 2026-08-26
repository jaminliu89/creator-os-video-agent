# Creator OS Video Agent

## Product definition

**Agent-neutral Video Production Orchestrator** — a local-first production protocol that lets Codex, Claude Code, WorkBuddy, Hermes, Pi and other capable agents run the same video workflow without binding the system to one model or one editor.

It is not another timeline editor and not another renderer.

It owns:

`input → transcript → semantic/director plan → storyboard → asset plan → edit/motion jobs → provider routing → render → QA → deliverables`

## Repository boundary

- `ai-director-engine` = understand/reason/decide, emits Director IR.
- `motion-runtime-os` = execute Motion IR through Remotion / HyperFrames and verify artifacts.
- `creator-os-video-agent` = orchestrate the whole production graph and route work to Edit/Motion/Voice/Visual providers.
- ChatCut = editable NLE/editing provider through MCP/agent plugin.
- FFmpeg = deterministic local media primitive.
- Remotion / HyperFrames = programmatic motion/render providers.
- Image/video/TTS/music systems = optional generation providers behind adapters.

## Agent contract

A host agent is compatible when it can provide enough of these capabilities:

1. read/write project files;
2. execute approved local commands/CLI;
3. call MCP/HTTP tools when configured;
4. load Skills/instructions;
5. observe command/tool results and continue an Agent Loop.

The workflow must never depend on a Codex-only or WorkBuddy-only prompt.

## Canonical pipeline

```text
input/transcript.md + media/
        ↓
Ingest / Transcript Normalize
        ↓
Semantic Director / Director IR
        ↓
Storyboard + Production Plan
        ↓
Pipeline IR / Job DAG
   ┌────┼──────────┬───────────┐
   ↓    ↓          ↓           ↓
 Edit  Motion     Assets      Audio
ChatCut Remotion  Image/Video Voice/Music
FFmpeg HyperFrames providers   providers
   └────┴──────────┴───────────┘
        ↓
Timeline / Composition Assembly
        ↓
Render
        ↓
QA: timing / media / semantic / visual
        ↓
output/final.mp4 + evidence/
```

## Current objective

Build one reproducible walking skeleton where the same project can be driven by at least two different host agents and where provider choice can change without changing the semantic production plan.

See `PRD.md`, `ARCHITECTURE.md`, `MASTER_TASK.md`, and `docs/`.

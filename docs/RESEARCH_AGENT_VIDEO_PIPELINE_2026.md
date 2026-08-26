# Research — Agent Video Production Pipeline 2026

## Executive conclusion
The market is converging on agent-driven video production rather than one-model-one-video generation. The important abstraction is an Agent runtime operating an editable project through Skills, MCP/tools, local files and CLI/renderers.

## ChatCut pattern
Public ChatCut materials describe an official Agent Plugin for Codex and Claude Code. The plugin connects to a hosted ChatCut MCP surface and exposes project/timeline editing, transcription, captions, motion graphics, image/video generation, voice/music and export. The key product insight is not any single AI feature; it is exposing a real editable NLE as an agent-callable tool surface.

Implication for us: ChatCut should be an `edit_provider`, not our architecture core. Our runtime must continue to work when ChatCut is absent.

## Codex / Claude pattern
Coding agents are effective video-production hosts because they can combine project files, code generation, CLI execution, tool calls and iterative verification. The workflow is durable when the production state is written to files rather than retained only in conversation context.

Implication: host-specific prompts must be thin. Canonical workflow logic belongs in Skills + schemas + state files.

## WorkBuddy pattern
Community workflows show WorkBuddy being used to turn repeatable media-generation/editing SOPs into Skills and to execute local multi-step creation tasks. This reinforces the same architecture: the host agent is a replaceable executor; the workflow is the durable asset.

## HyperFrames pattern
HyperFrames explicitly positions itself as agent-native HTML-to-video: the agent writes editable HTML/CSS/JS and seekable animation code, then the framework renders deterministic frames/MP4. It supports project folders rather than opaque generation outputs.

Implication: HyperFrames is a motion/render provider well suited to web-native MG, GSAP, Lottie, CSS and Three.js semantics.

## Remotion pattern
Remotion represents the React/programmatic-video branch. It is especially strong where timeline output is derived from data, components, captions, UI, charts and reusable code. It belongs beside HyperFrames behind a provider-neutral Motion IR/router.

## The five-step transcript workflow — corrected architecture
The popular workflow is often described as:
1. transcript;
2. storyboard;
3. prompts/code;
4. asset generation/render;
5. export/check.

For a production-grade system this is insufficient. We expand it to:

`ingest → normalize → semantic direct → storyboard → Pipeline IR/DAG → provider routing → execute → assemble → QA → review → deliver → learn`

The missing concepts are structured state, provider contracts, resumability, semantic QA and evidence.

## Why not bind to one Agent
Codex, Claude Code, WorkBuddy, Hermes and Pi differ in tool syntax and runtime ergonomics, but the pipeline only requires a common capability profile: filesystem, command/tool execution, Skill loading and observation/retry. Therefore agent choice must be an adapter-level concern.

## Competitive capture
### ChatCut
Absorb: editable project + MCP surface + task Skills + verification.
Do not copy: editor implementation or ChatCut-specific state as canonical state.
Status: NOW as optional Edit Provider.

### HyperFrames
Absorb: project-as-code, deterministic render, agent-native skills, seekable timelines.
Status: NOW as Motion Provider.

### Remotion
Absorb: componentized deterministic programmatic video, reusable motion primitives, data-driven rendering.
Status: NOW as Motion Provider.

### WorkBuddy/Codex-style workflow
Absorb: filesystem-centric Agent Loop, local command execution, workflow Skill packaging.
Do not copy: host-specific prompts as system architecture.
Status: NOW as Host Agent Adapters.

## Product opportunity
The gap is not another editor or another renderer. The gap is a portable Video Production Orchestrator that converts semantic intent into auditable jobs and lets any capable agent execute them through interchangeable providers.

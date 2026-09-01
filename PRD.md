# PRD — Creator OS Video Agent v2.1

## 1. Problem
AI agents can already read transcripts, write code, call CLIs and interact with editing/rendering tools, but current workflows are fragmented and host-specific. A second problem is more fundamental: many automatic video systems can technically render a complete MP4 yet still feel generic because they jump directly from script/keywords to stock clips or renderer commands without an explicit director layer.

The result is brittle automation with weak semantic timing, repetitive B-roll, little pacing contrast and no durable explanation of why a visual choice exists.

## 2. Product
Create an **agent-neutral video production runtime** that converts transcript/media intent into structured director decisions and dispatches them to interchangeable providers.

Canonical product path:
`Script/Transcript → Director IR/Beat Graph → Visual Decision → Director Timeline → Pipeline IR/DAG → Providers → Renderer → QA/Evidence`.

The product is the orchestration protocol + director-to-execution contract + evidence loop. It is not the LLM host and not a renderer.

## 3. Target users
- creators making talking-head, education, product, documentary and faceless videos;
- studios operating multiple AI agents;
- developers building repeatable video automations;
- Creator OS as the upstream product surface.

## 4. Jobs to be done
Given source video/audio/transcript, the user can state the intended result once. Any compatible host agent can then:
1. normalize transcript/timestamps;
2. identify semantic beats and director intent;
3. decide visual treatment for every meaningful beat;
4. write a machine-readable Director Timeline;
5. generate provider-neutral production jobs and missing-asset prompts;
6. execute editing/motion/generation/media-infrastructure providers;
7. assemble and render;
8. verify timing, media streams, semantic intent, visual continuity and restraint;
9. deliver final MP4 plus evidence and editable project artifacts.

## 5. Core workflow
### Stage A — Ingest
Inputs: `input/transcript.md`, media files, brief, references, brand/style constraints.
Outputs: normalized transcript, media manifest, project brief.

### Stage B — Understand / Direct
Use `ai-director-engine` or compatible Semantic Director to produce Beat Graph / Director IR: revelation, contrast, question, proof, explanation, emphasis, pacing, emotional transition and attention target.

### Stage C — Visual Decision
For each beat, explicitly choose a treatment rather than defaulting to “find related B-roll”. Supported modes include:
- A-roll;
- B-roll;
- still image;
- AI image;
- AI video;
- MG motion;
- kinetic text;
- chart/data visual;
- screen recording;
- UI demo;
- digital human/avatar;
- black frame;
- hold existing;
- intentional none.

### Stage D — Director Timeline
Persist the visual/audio/director contract using `schemas/director-timeline.v1.schema.json`.

It must bind decisions to exact beat ranges and preserve narrative function, attention target, pacing, purpose, asset intent, motion/text emphasis, music/SFX/silence and QA constraints.

### Stage E — Production Plan
Compile Director Timeline into storyboard and provider-neutral Pipeline IR/DAG. Transcript segments become explicit jobs rather than prose prompts.

### Stage F — Provider execution
Router chooses providers by capability, semantic fidelity, editability, determinism, latency, cost, privacy and quality:
- ChatCut: optional editable NLE/edit path;
- FFmpeg: deterministic cuts, probes, muxing and media transforms;
- Remotion: React/programmatic motion;
- HyperFrames: HTML/CSS/JS/GSAP/Three.js deterministic motion;
- stock/search providers: Pexels/Pixabay/Coverr-style adapters;
- generation providers: image, video, TTS, music, SFX;
- digital humans: HeyGen, D-ID or compatible adapters;
- MoneyPrinterTurbo-like modules: optional media-infrastructure adapters, never Director Core.

### Stage G — Assembly
All jobs write results back to the shared artifact graph. Timeline/composition assembly consumes structured timing and intent references.

### Stage H — Quality gate
- transcript/timeline sync;
- beat/asset temporal alignment;
- artifact existence/checksum;
- video+audio probe;
- caption visibility/timing;
- motion/director semantic survival;
- visual continuity/keyframe sampling;
- restraint/redundancy checks;
- provider failures and retry evidence;
- human preference evidence when comparing editorial approaches.

### Stage I — Deliver
`output/final.mp4`, editable provider project where available, manifests, render results and QA evidence.

## 6. MoneyPrinterTurbo benchmark decision
MoneyPrinterTurbo is recorded as an **Infrastructure Candidate / Renderer Reference**, not as the core product architecture.

We absorb or emulate useful patterns around multi-provider integration, TTS/timestamps, stock-media adapters, subtitles/transcription, batch execution and FFmpeg media plumbing.

We do not adopt as core:
- keyword-to-stock matching as visual intelligence;
- random/simple clip sequencing as editing policy;
- renderer-owned narrative choices;
- one-shot script-to-video without an inspectable Director Timeline.

See `docs/benchmarks/MONEYPRINTERTURBO_CAPTURE.md`, `registries/benchmarks.v1.json` and `docs/DEPLOYMENT_VS_DIRECTOR_DIAGNOSIS.md`.

## 7. Host-agent compatibility
The pipeline may be run by Codex, Claude Code, WorkBuddy, Hermes, Pi or another agent. Host-specific adapters are thin wrappers only. Canonical workflow logic lives in files/schemas/skills, not a proprietary system prompt.

Minimum capability profile:
- filesystem read/write;
- command execution or delegated executor;
- Skill/instruction loading;
- tool/MCP or HTTP invocation for external providers;
- iterative observation and retry.

## 8. Product principles
- Transcript is input, not source of truth after planning; structured IR is.
- Director intent and provider execution are separate.
- Director Timeline is the execution boundary for visual meaning.
- Agent host and provider are separate dimensions.
- Files are durable handoff state; chat context is disposable.
- Every stage has machine-readable inputs/outputs and acceptance gates.
- No provider may silently drop unsupported semantics.
- A successful render is not automatically a good edit.
- Do not solve director defects with renderer/deployment tuning.

## 9. MVP
One talking-head/knowledge-video project:
- transcript + source MP4;
- Semantic Director / Beat Graph;
- Director Timeline v1;
- Pipeline IR;
- one deterministic local edit/render path;
- motion path through Remotion and HyperFrames;
- automatic captions;
- at least one B-roll/asset routing path;
- final MP4;
- evidence package;
- Neutral vs Directed comparison fixture;
- repeatable execution from at least two host agents.

## 10. Non-goals for MVP
- rebuild ChatCut/CapCut/Premiere;
- fork MoneyPrinterTurbo into the product core;
- full Blender/Unreal pipeline;
- every image/video provider;
- autonomous publishing;
- human-equivalent director quality claim.

## 11. Success metrics
Engineering: deterministic replay, stage-level resume, no hidden host dependency, provider-contract conformance, Director Timeline preservation.

Product: time-to-first-cut, manual interventions per minute, semantic/temporal mismatch rate, visual redundancy, editability rate and blind human preference of Directed output versus neutral keyword/stock baseline.

## 12. Definition of Done
MVP is accepted only when the same canonical project can be executed by two distinct host agents, produces equivalent Director Timeline/Pipeline jobs, routes edit + motion + asset/media infrastructure, renders a media-probed MP4 and preserves audit evidence.

A prompt-only demo or a technically successful but semantically unverified MP4 is not DONE.

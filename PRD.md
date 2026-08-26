# PRD — Creator OS Video Agent v2

## 1. Problem
AI agents can already read transcripts, write code, call CLIs and interact with editing/rendering tools, but current workflows are fragmented and host-specific. A Codex workflow, Claude workflow, WorkBuddy workflow or Hermes workflow often encodes business logic directly in prompts and tool-specific commands. The result is brittle, non-portable and hard to verify.

## 2. Product
Create an **agent-neutral video production runtime**. The system converts transcript/media intent into structured production artifacts and dispatches jobs to interchangeable providers such as ChatCut, FFmpeg, Remotion, HyperFrames, image/video generation, TTS and music systems.

The product is the orchestration protocol and evidence loop — not the LLM host and not the renderer.

## 3. Target users
- creators making talking-head, education, product, documentary and faceless videos;
- studios operating multiple AI agents;
- developers building repeatable video automations;
- Creator OS as the upstream product surface.

## 4. Jobs to be done
Given source video/audio/transcript, the user can say what result they want once. Any compatible host agent can then:
1. normalize transcript/timestamps;
2. identify semantic beats and director intent;
3. produce storyboard and motion/edit blueprint;
4. generate provider jobs and missing-asset prompts;
5. execute editing/motion/generation providers;
6. assemble and render;
7. verify timing, media streams, semantic intent and visual continuity;
8. deliver final MP4 plus evidence and editable project artifacts.

## 5. Core workflow
### Stage A — Ingest
Inputs: `input/transcript.md`, media files, brief, references, brand/style constraints.
Outputs: normalized transcript, media manifest, project brief.

### Stage B — Understand / Direct
Use `ai-director-engine` or compatible Semantic Director to produce Director IR. Important beats include revelation, contrast, question, emphasis, pacing and emotional transition.

### Stage C — Production Plan
Compile Director IR into storyboard, shot/motion/edit plan and a provider-neutral Pipeline IR/DAG. This is where transcript segments become explicit jobs rather than prose prompts.

### Stage D — Provider execution
Router chooses providers by capability, editability, determinism, latency, cost and quality:
- ChatCut: editable transcript/timeline/NLE and motion graphics through MCP/plugin;
- FFmpeg: deterministic cuts, probes, muxing and media transforms;
- Remotion: React/programmatic motion;
- HyperFrames: HTML/CSS/JS/GSAP/Three.js deterministic motion;
- generation providers: image, video, TTS, music, avatar/digital-human adapters.

### Stage E — Assembly
All jobs write results back to the shared artifact graph. Timeline/composition assembly must consume structured timing rather than human drag/drop state.

### Stage F — Quality gate
- transcript/timeline sync;
- artifact existence/checksum;
- video+audio probe;
- caption visibility and timing;
- motion/director semantic survival;
- visual continuity/keyframe sampling;
- provider failures and retry evidence.

### Stage G — Deliver
`output/final.mp4`, editable provider project where available, manifests, render results and QA evidence.

## 6. Host-agent compatibility
The pipeline may be run by Codex, Claude Code, WorkBuddy, Hermes, Pi or another agent. Host-specific adapters are thin wrappers only. Canonical workflow logic lives in files/schemas/skills, not a proprietary system prompt.

Minimum capability profile:
- filesystem read/write;
- command execution or delegated executor;
- Skill/instruction loading;
- tool/MCP or HTTP invocation for external providers;
- iterative observation and retry.

## 7. Product principles
- Transcript is input, not source of truth after planning; structured IR is.
- Director intent and provider execution are separate.
- Agent host and provider are separate dimensions.
- Files are durable handoff state; chat context is disposable.
- Every stage has machine-readable inputs/outputs and acceptance gates.
- No provider may silently drop unsupported semantics.
- A successful render is not automatically a good edit.

## 8. MVP
One talking-head project:
- transcript + source MP4;
- Semantic Director / storyboard;
- Pipeline IR;
- one editable edit path (ChatCut when available, FFmpeg fallback);
- motion path through Remotion and HyperFrames;
- automatic captions;
- final MP4;
- evidence package;
- repeatable execution from at least two host agents.

## 9. Non-goals for MVP
- rebuild ChatCut/CapCut/Premiere;
- full Blender/Unreal pipeline;
- every image/video provider;
- autonomous publishing;
- human-equivalent director quality claim.

## 10. Success metrics
Engineering: deterministic replay, stage-level resume, no hidden host dependency, provider-contract conformance.
Product: time-to-first-cut, manual interventions per minute of output, QA failure rate, editability rate, human preference vs neutral baseline.

## 11. Definition of Done
MVP is accepted only when the same canonical project can be executed by two distinct host agents, produces equivalent structured jobs, successfully routes at least edit + motion providers, renders a media-probed MP4 and preserves audit evidence. A prompt-only demo is not DONE.

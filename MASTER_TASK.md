# MASTER TASK — Agent-neutral Video Production Orchestrator

## Objective
Build a production-grade local-first pipeline that any compatible host Agent can execute:

`transcript/media → semantic direction → storyboard → Pipeline IR/DAG → provider routing → edit/motion/assets/audio → assembly → QA → final MP4`

## Current decision
Do **not** create another repository. `creator-os-video-agent` is the orchestration Source of Truth above `ai-director-engine` and `motion-runtime-os`.

## MT-001 — Contract & Architecture
- [x] Redefine repository as Agent-neutral orchestrator.
- [x] PRD v2.
- [x] Cross-Agent architecture.
- [x] 2026 ChatCut/Codex/WorkBuddy/HyperFrames research capture.
- [x] Agent Compatibility Spec.
- [x] Pipeline IR Spec.
- [ ] JSON Schema for Pipeline IR.
- [ ] Provider Registry machine-readable schema.
- [ ] Host Adapter Registry for Codex/Claude/WorkBuddy/Hermes/Pi.

## MT-002 — Walking Skeleton
One talking-head project must create durable artifacts for every stage.

- [ ] `input/transcript.md` + source media convention.
- [ ] Transcript normalizer.
- [ ] Invoke/consume `ai-director-engine` Director IR.
- [ ] Storyboard compiler.
- [ ] Director IR → Pipeline IR compiler.
- [ ] DAG runner with state persistence/resume.
- [ ] FFmpeg provider adapter.
- [ ] Motion Runtime adapter (`motion-runtime-os`).
- [ ] Evidence manifest + final QA.
- [ ] `output/final.mp4` acceptance artifact.

## MT-003 — Editable Edit Provider
- [ ] ChatCut capability discovery / MCP adapter.
- [ ] Import source media.
- [ ] Transcript-based cut jobs.
- [ ] Captions and timeline modifications.
- [ ] Motion-graphic job dispatch where useful.
- [ ] Export/editable project evidence.
- [ ] If ChatCut unavailable, fallback remains FFmpeg without corrupting Pipeline IR.

## MT-004 — Motion Router
- [ ] Route Motion IR jobs to Remotion or HyperFrames based on semantics.
- [ ] Preserve existing cross-provider semantic QA from `motion-runtime-os`.
- [ ] Register downgrade/fallback evidence.

## MT-005 — Generation Routers
After core edit+motion works:
- [ ] Image generation adapter contract.
- [ ] Video/B-roll generation adapter contract.
- [ ] TTS/voice adapter contract.
- [ ] Music adapter contract.
- [ ] Optional avatar/digital-human adapter contract.

Do not hard-wire Seedance/Kling/etc. into Pipeline IR; they are provider implementations.

## MT-006 — Host-Agent Neutrality
The same canonical fixture must execute under at least two host adapters.

Candidate hosts: Codex, Claude Code, WorkBuddy, Hermes, Pi.

Gate:
- equivalent Pipeline IR semantics;
- same durable project layout;
- provider jobs run without host-specific workflow forks;
- final media QA passes;
- handoff between Agents works from files alone.

## MT-007 — Quality & Human Review
- [ ] transcript/timeline sync QA;
- [ ] media stream probe;
- [ ] motion/director semantic survival;
- [ ] visual continuity/keyframe sampling;
- [ ] provider downgrade report;
- [ ] optional approval points before expensive generation/export;
- [ ] human preference evaluation for creative quality.

## MVP Definition of Done
The project is not DONE because an Agent generated scripts. MVP requires one real talking-head project to run from files to `output/final.mp4`, with resumable state, provider evidence, edit+motion execution, media/semantic QA, and successful execution from at least two different host Agents.

## Constraints
- Host Agent ≠ Director ≠ Orchestrator ≠ Provider.
- ChatCut is a provider, not canonical state.
- Remotion/HyperFrames are providers, not canonical state.
- No silent semantic downgrade.
- No prompt-only architecture.
- No unnecessary new repository.
- Blender/Unreal/full NLE cloning are outside current critical path.

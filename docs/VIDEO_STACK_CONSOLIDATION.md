# Video Stack Consolidation

## Canonical responsibility map

- `zhijian-ai` — human-facing desktop creative workbench. Owns canvas/timeline/media/chat/preview/approval UX and local project interaction.
- `creator-os-video-agent` — headless agent-neutral production orchestrator. Owns Pipeline IR, Job DAG, provider routing, retries/resume, artifact graph and evidence.
- `ai-director-engine` — Director Brain. Owns perception, semantic directing and Director IR.
- `motion-runtime-os` — Motion Runtime. Owns Motion IR execution, Remotion/HyperFrames adapters and render QA.

## Provider assets to register
- `omnipotent-director`: HyperFrames production recipe/Skill provider.
- `metaforge-pipeline`: Remotion motion-theme/recipe reference provider.
- `digital-human-video`: digital-human/avatar provider Skill.
- `audio-transcriber-tts`: transcript/TTS provider.
- `music-studio`: music/audio provider candidate.
- ChatCut: editable NLE provider via MCP/plugin.
- FFmpeg: deterministic local edit/media primitive.

## Anti-duplication rule
Video Agent is the canonical production orchestration owner. Zhijian may expose a local Harness client/facade, but must not maintain a second independent Pipeline IR/DAG/router implementation. Motion Runtime owns provider-neutral motion execution. Director Engine owns semantic intent. Recipe repositories may contain templates, Skills and provider-specific knowledge but must not redefine the orchestration protocol.

## Data flow
```text
Human / Host Agent
      ↓
zhijian-ai UI OR headless host (Codex/Claude/WorkBuddy/Hermes/Pi)
      ↓
creator-os-video-agent
      ↓
Pipeline IR / DAG
      ├─ ai-director-engine → Director IR
      ├─ edit provider → ChatCut/FFmpeg/etc
      ├─ motion-runtime-os → Remotion/HyperFrames
      ├─ avatar provider → digital-human-video
      └─ audio/visual providers
      ↓
Artifact Graph + QA Evidence
      ↓
zhijian-ai preview/timeline/human approval OR headless delivery
```

## Migration sequence
1. Keep existing repositories/history.
2. Extract unique schemas/templates/skills from overlapping repos.
3. Register them as providers/recipes in Video Agent.
4. Make Zhijian consume Video Agent contracts instead of rebuilding orchestration.
5. Stop new platform-level Agent Loop/Router implementations in provider/reference repos.

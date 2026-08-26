# Pipeline IR Spec v1

## Purpose
Pipeline IR is the executable production graph between Director IR and concrete providers. It is distinct from Director IR (creative intent) and Motion IR (motion execution).

## Root shape
```yaml
version: 1.0
project_id: string
source_refs: []
intent_ref: state/director-ir.json
jobs: []
artifacts: []
quality_gates: []
```

## Job
```yaml
job_id: edit-001
kind: edit
needs: []
input_refs: [asset:source-video, state:transcript]
output_refs: [artifact:rough-cut]
time_range: {start: 0.0, end: 30.0}
intent_refs: [director:segment-1]
requirements:
  capabilities: [transcript_edit, timeline]
  editable_output: true
preferred_provider: chatcut
fallback_providers: [ffmpeg]
status: planned
attempts: []
evidence_refs: []
```

## Job kinds
- ingest
- transcribe
- direct
- edit
- motion
- image_generate
- video_generate
- voice
- music
- avatar
- assemble
- qa
- export

## Provider-neutral requirement
Pipeline IR may refer to a capability (`timeline_edit`, `motion_graphics`, `video_generate`) but cannot embed a ChatCut API call, Remotion JSX, HyperFrames HTML or host-agent command.

## Artifact graph
Every job output is registered with:
- logical artifact ID;
- file/provider reference;
- checksum when file-backed;
- media metadata;
- producer job/provider;
- semantic intent reference;
- QA status.

## Retry/resume
Attempts are append-only. Re-running an interrupted project must reuse completed artifacts whose inputs and semantic hashes have not changed.

## Semantic hash
A job should derive a stable hash from normalized input refs + relevant intent + parameters + provider version. This enables caching and safe resume.

## Downgrades
If a provider cannot satisfy a requested capability or semantic intent, it must return a structured downgrade. The orchestrator decides whether to choose another provider, request review or accept the downgrade. Silent dropping is forbidden.

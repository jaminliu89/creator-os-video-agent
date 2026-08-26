# Agent Compatibility Spec v1

## Goal
The canonical video pipeline must be executable by multiple host agents without rewriting product logic.

## Capability profile
A host declares support for:

```yaml
host:
  id: codex|claude|workbuddy|hermes|pi|other
  filesystem:
    read: true
    write: true
  command_execution:
    supported: true
    shell: bash|zsh|powershell|delegated
  skills:
    supported: true
    discovery: native|filesystem|prompt
  tools:
    mcp: true|false
    http: true|false
  observation_loop: true
  sandboxing: optional
```

## Required operations
- `read_project_state`
- `write_project_state`
- `discover_capabilities`
- `execute_job`
- `observe_job`
- `record_evidence`
- `resume_from_state`

## Compatibility levels
### L0 Planning only
Can read/write files, cannot execute tools. May generate Pipeline IR but cannot satisfy production acceptance.

### L1 Local executor
Filesystem + command execution. Can use FFmpeg, Remotion, HyperFrames and local scripts.

### L2 Tool-connected executor
L1 + MCP/HTTP providers such as ChatCut or cloud generation services.

### L3 Production host
L2 + resumable Agent Loop, bounded retry, evidence capture and approval gates.

## Portability rule
No canonical state may contain Codex-, Claude-, WorkBuddy-, Hermes- or Pi-specific command syntax. Host adapters translate generic job operations into native calls.

## Handoff rule
A second compatible agent must be able to continue by reading only the repository/project state plus provider credentials/configuration; prior chat transcript is optional.

## Acceptance
The MVP host-neutrality gate requires the same project fixture to be planned/executed by at least two host adapters with equivalent Pipeline IR semantics and successful final QA.

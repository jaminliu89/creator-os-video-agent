# Edit Provider Contract v1

Status: ACTIVE / MT-003
Date: 2026-08-26

## Purpose
Define how an editable NLE provider such as ChatCut participates in Creator OS Video Agent without becoming the owner of Pipeline IR or Director intent.

## Verified ChatCut product boundary
Official ChatCut docs describe two external-Agent MCP paths:
1. Agent Plugin hosted MCP: Claude Code Desktop or Codex Desktop controls a hosted ChatCut project visible in the host Browser pane.
2. ChatCut Desktop local MCP: an external desktop Agent controls the native ChatCut Desktop project currently open on the same computer.

Official capabilities include media import/organization, timeline cutting/trimming/arrangement, transcription/captions, motion graphics, asset generation, export and verification of edits in the editor.

Sources:
- https://chatcut.io/docs/agent-plugin
- https://chatcut.io/docs/external-agents-and-mcp
- https://chatcut.io/docs/timeline

## Architectural rule
ChatCut is an EDIT PROVIDER. It does not own:
- Pipeline IR semantics;
- DAG ordering;
- Director IR;
- provider-selection policy;
- cross-provider evidence semantics.

The host Agent/MCP bridge may translate generic Edit Provider operations into the current ChatCut tool schema discovered in that session. Tool names are deliberately not hard-coded here because the maintained plugin controls its own MCP surface.

## Required capabilities
An editable provider may advertise:
- `media_import`
- `transcript_edit`
- `timeline_edit`
- `captions`
- `motion_graphics`
- `editable_project`
- `export`
- `verification`

## Pipeline requirements
`requirements.editable_output=true` is a hard semantic requirement. A non-editable provider such as FFmpeg must not silently satisfy that job. If no editable provider is available, orchestration must stop/review rather than downgrade without evidence.

FFmpeg is a valid fallback only when:
- `editable_output=false`, or
- a future explicit downgrade policy has been approved and recorded as evidence.

## Provider request
The adapter receives a normal Pipeline IR edit job plus resolved input artifacts and Director intent references. It should construct a provider request containing:
- project/session reference;
- source artifact references;
- requested edit operations/capabilities;
- Director intent references, never reinterpreted silently;
- output requirements (`editable_project`, preview/export media);
- approval policy for destructive changes.

## Provider result
A successful editable provider returns artifacts/evidence for:
- editable project/timeline reference;
- exported or preview media if requested;
- operation summary;
- verification that edits are visible/applied;
- provider surface (`hosted_mcp` or `desktop_local_mcp`);
- warnings/downgrades;
- lineage back to Pipeline job and Director intent refs.

## Authentication
Authorization remains in the provider's maintained browser/desktop flow. Cookies, access tokens and passwords must never be stored in Pipeline IR, repository files, prompts or evidence manifests.

## Acceptance gates
MT-003 closes only when a real editable project demonstrates:
`real media → Pipeline edit job → ChatCut MCP adapter → editable timeline → verification → exported preview/project evidence`
with FFmpeg remaining a legal non-editable fallback for jobs that allow it.

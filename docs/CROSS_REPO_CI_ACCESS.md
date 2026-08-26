# Cross-Repo CI Access — Explicit Blocker

Date: 2026-08-26
Status: BLOCKED BY GITHUB PERMISSION, not by pipeline code.

## What failed
`Video Agent Real Media Vertical Slice` run `32946222946` failed at the second `actions/checkout` step before Python/Node/FFmpeg execution. `creator-os-video-agent`, `ai-director-engine`, and `motion-runtime-os` are private sibling repositories. The repository-scoped default `GITHUB_TOKEN` cannot read the sibling private repositories.

## Required resolution
Provide a repository secret such as `CROSS_REPO_TOKEN` using a fine-grained token/GitHub App installation with read access to:
- `jaminliu89/ai-director-engine`
- `jaminliu89/motion-runtime-os`

The token should be used only for sibling checkout. It must not be embedded in source, Pipeline IR, evidence, logs, or provider configuration.

## Evidence boundary
This infrastructure failure does NOT invalidate existing independent real-media acceptance in Director Engine and Motion Runtime. It does mean Video Agent cannot yet claim a single CI run orchestrated all three private repositories end-to-end.

## Next acceptance
After cross-repo read access is configured, rerun `.github/workflows/real-media-vertical-slice.yml`. Acceptance requires the orchestrated job to reach final media probe and upload `output/final.mp4` plus state/evidence artifacts.

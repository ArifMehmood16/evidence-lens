# Implementation Plan: Shared development workflow

**Feature**: 001-development-workflow | **Date**: 2026-10-19 | **Spec**: [spec.md](spec.md)

## Summary and technical context

Use official Spec Kit 1.2.2 rendered integrations for three editors and supported project template overrides. Keep the existing selected ECC adaptations and add explicit artifact handoffs. Runtime for smoke tests: Python standard library plus Bash and Git; the CLI is optional local development tooling.

## Constitution Check

Pass: one workflow and feature directory, maintained upstream scripts instead of custom orchestration, reviewed licenses and local state, observable tooling tests, honest verification. RAG quality, production capacity, and public frontend gates are N/A because no application behavior changes.

## Research and design

See [research.md](research.md). Keep upstream assets intact and separately hash-tracked by their generated manifests. Store project policy in the constitution and overrides. Do not install hooks or global settings. Roll back this integration through Git if needed; remove/recreate the ignored local CLI environment independently.

No domain data-model.md or API contracts are needed: this feature adds repository guidance and tooling only. [quickstart.md](quickstart.md) defines validation scenarios.

## Affected paths

.specify/, official speckit-* skill directories, existing ECC skills, AGENTS.md, documentation/PR entry points, specs/, tools/spec-kit-requirements.txt, tests/tooling/, third_party/spec-kit/LICENSE, and documentation CI.

## Verification and release gates

Run ECC verification-loop, recording results in verification.md. Tests use isolated temporary projects, exercising official scripts rather than creating live feature state. Verify creation and override selection, existing-plan preservation, missing-prerequisite failure, and managed asset hashes across all editors. Run Markdown lint and shell syntax checks. Inspect tracked/untracked changes for local paths, secrets, and unintended code.

CI runs the same offline tests. Real editor sessions and remote CI completion must be reported separately; script tests do not demonstrate LLM adherence. Convergence assesses all FR/SC obligations and adds tasks if required evidence is missing.

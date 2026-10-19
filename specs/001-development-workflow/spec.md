# Feature Specification: Shared development workflow

**Feature**: 001-development-workflow | **Created**: 2026-10-19 | **Status**: Implemented; see verification limitations

**Input**: Integrate Spec Kit and ECC throughout EvidenceLens, rather than for one pilot feature.

**Scope amendment, 2026-10-19:** the user explicitly deferred GitHub Actions for the entire development project. Verification is local until the user explicitly authorizes Actions later.

## Problem and scope

Contributors need one durable, reproducible way to specify and validate work across the entire application. Install the official Spec Kit integrations and connect the existing selected ECC skills through shared governance and templates. Application implementation, global editor settings, automatic agent execution, and installing the full ECC collection are out of scope.

## User Scenarios & Testing

### User Story 1 — Consistent development in supported editors (Priority: P1)

A contributor using Codex, Claude Code, or Cursor creates a feature and obtains the same EvidenceLens requirements and quality gates.

**Independent Test**: Exercise official feature/plan/task helpers in an isolated temporary project and inspect integration manifests.

**Acceptance Scenarios**:

1. Given the shared overrides, when a new feature is created, its spec and plan use the project templates and task setup returns the project task template.
2. Given an existing plan with contributor edits, when setup runs again, those edits remain.
3. Given missing required feature artifacts, when prerequisites are checked, the command fails with an actionable error.

### User Story 2 — Reuse and verification throughout delivery (Priority: P1)

A contributor sees ECC research and verification obligations in every substantial feature workflow, with RAG/frontend/operations checks applied where relevant.

**Independent Test**: Review constitution, override resolution, feature index, ECC skills, and PR entry points against the documented workflow.

### Edge Cases

A clone has no current-feature pointer; contributors must select their feature. An editor may not discover skills until refreshed. Small fixes should not require unnecessary new specifications. Upgrades must preserve project overrides.

## Requirements

- **FR-001**: Include official Spec Kit integrations for Codex, Claude Code, and Cursor, pinned to a reviewed revision.
- **FR-002**: All integrations MUST use one constitution and shared override templates.
- **FR-003**: Planning MUST include ECC search-first research in the canonical feature directory.
- **FR-004**: Implementation MUST include ECC verification evidence, applicable specialist checks, and convergence against that evidence.
- **FR-005**: Workflow guidance MUST cover all application areas and later roadmap phases, with a small-fix route.
- **FR-006**: Preserve local state isolation, existing artifacts, Apache project licensing, and upstream MIT attribution; no automatic hooks or global configuration.
- **FR-007**: Provide repeatable local smoke tests and verification commands. Remove GitHub Actions workflows and keep Actions disabled until explicitly requested by the user.

## Success Criteria

- **SC-001**: Every registered upstream asset matches its manifest hash; all three editor integrations are present.
- **SC-002**: Offline tests demonstrate shared template selection, rerun preservation, and rejection of missing prerequisites.
- **SC-003**: Authored Markdown passes the configured linter; contributors have reproducible setup and validation commands.

## Verification obligations

Run the tooling suite, shell syntax checks, authored Markdown lint, and diff review locally. Review licenses, local-state exclusions, and the global lifecycle manually. Report editor sessions not exercised. Remote CI is intentionally excluded.

## Assumptions

Agent instructions require human review and cannot prove model adherence. Application RAG accuracy, load, clinical usefulness, security scanning, and frontend behavior are outside this tooling feature.

# Tasks: Shared development workflow

## Phase 1: Research and installation

- [x] T001 Inspect official Spec Kit release and existing ECC skills; record choices in research.md per FR-001/FR-003.
- [x] T002 Install official integrations under .agents/, .claude/, .cursor/, and .specify/ with events disabled per FR-001/FR-006.

## Phase 2: Shared lifecycle

- [x] T003 Write .specify/memory/constitution.md and shared overrides per FR-002/FR-003/FR-004.
- [x] T004 Connect ECC skills, AGENTS.md, contribution docs, PR template, and specs/README.md per FR-003/FR-004/FR-005.
- [x] T005 Preserve upstream notices, pinned tooling setup, and local-state ignores per FR-006.

## Phase 3: Verification

- [x] T006 Add and run tests/tooling checks and CI integration per FR-007/SC-001/SC-002.
- [x] T007 Run lint, syntax, and diff/license checks; record ECC evidence in verification.md per SC-003.
- [x] T008 Assess all requirements against implementation and verification, resolving gaps before completion per FR-004.

## Phase 4: User-directed local verification policy

The user amended FR-007 after initial integration. T006 records the original implementation; its GitHub Actions portion is superseded by this phase.

- [x] T009 Remove .github/workflows/docs.yml, disable repository Actions, and attempt cancellation of outstanding runs per amended FR-007; record GitHub's cancellation limitation in verification.md.
- [x] T010 Update AGENTS.md, constitution, templates, contributor guidance, and current feature artifacts to require local checks and explicit user instructions before introducing Actions.
- [x] T011 Validate the amended scope locally and record the results and GitHub state in verification.md.

# Verification: Shared development workflow

**Date**: 2026-10-19 | **Checked scope**: Integration changes on chore/spec-kit-ecc-integration, based on e3ed7e4; this report accompanies the implementation commit.

The initial integration evidence below is retained for history. The local-only verification amendment at the end supersedes its GitHub Actions configuration and remote-CI expectations.

## Acceptance evidence

- **FR-001/FR-002/SC-001:** all three official integrations are registered with events disabled. The tooling suite verifies every registered upstream file against its generated manifest and exercises project overrides through the shipped helpers.
- **FR-003/FR-004:** reviewed constitution, plan/task overrides, ECC skills, and PR guidance. Research and verification use the same feature directory; convergence treats missing required evidence as unfinished work.
- **FR-005:** reviewed specs/README.md coverage of every roadmap phase, shared agent entry points, and the behavior-preserving small-fix path.
- **FR-006:** reviewed MIT notices, CLI source pin, ignored local environment/feature pointer, and absence of generated event-hook configuration. Existing-plan preservation is tested.
- **FR-007/SC-002:** four offline unittest scenarios cover template selection, task preparation, prerequisite errors, rerun preservation, and managed asset integrity. Initially these checks were also configured for CI; that configuration was subsequently removed under the amendment below.
- **SC-003:** authored Markdown lint passes; setup and verification commands are in docs/agent-tooling.md and quickstart.md.

## Checks performed

- **Passed:** `python3 -m unittest discover -s tests/tooling -v` — four tests, Python 3.14 on the development Mac; no network/model/cloud calls.
- **Passed:** `npx --yes markdownlint-cli2@0.18.1` — authored Markdown and rules, including constitution and overrides. Initial bare placeholder paths triggered HTML lint errors; corrected and rerun successfully.
- **Passed:** `bash -n` for each .specify/scripts/bash/*.sh helper.
- **Passed:** skill-creator quick_validate.py for the four adapted/original project skills, using the local tooling environment. This is a developer check; the external validator is not a CI dependency.
- **Passed:** `git diff --check`, manual diff/license review, local Markdown link-target review, and ignore checks for .tools/ and .specify/feature.json.
- **Passed:** CLI installation/version check at pinned Spec Kit 1.2.2; official integrations installed with events disabled.

## Limitations and remaining work

Live interactive sessions in Claude Code, Cursor, and Codex were not separately exercised. Instructions and template tests do not prove model adherence. No application build, clinical/RAG quality evaluation, production load test, dependency vulnerability audit, frontend check, or deployment was run: this feature changes development tooling only.

Remote GitHub Actions completion was not observed for the initial integration. The initial CI configuration was reviewed locally and subsequently removed at the user's instruction. CLI transitive dependencies are not fully locked across platforms; the reviewed source commit is pinned.

## Convergence assessment

Reviewed seven functional requirements, three success criteria, both user stories, plan decisions, all eight tasks, and the five constitution principles. The implementation and local evidence satisfy this tooling scope. No remaining buildable gap was identified; no empty convergence phase was appended. Application roadmap capabilities remain planned and are not represented as implemented by this integration.

## Local-only verification amendment — 2026-10-19

**Reason:** the user explicitly requested no GitHub Actions throughout development until further clear instructions. FR-007, the plan, shared guidance, templates, and constitution 1.1.0 now reflect that scope. This is a user-directed scope change, not a relaxation to conceal failed checks.

- Removed .github/workflows/docs.yml; no GitHub Actions workflow files remain in the working tree.
- Disabled repository Actions; the GitHub permissions API returned `enabled: false`.
- Attempted normal and forced cancellation of existing queued runs 39282208605 and 39280080431. GitHub returned HTTP 409, stating they were not in progress. Both records still appeared queued after disabling Actions; no cancellation success is claimed. Actions must remain disabled until the user requests otherwise.
- Passed locally: four tooling smoke tests, bundled Bash syntax checks, authored Markdown lint, and diff whitespace checks. Application code did not change; no new tests were needed.
- Local verification commands remain documented. Remote CI is intentionally excluded, and its absence does not block completion of this amended scope.

Convergence: amended FR-007 and tasks T009–T011 are satisfied, with the GitHub cancellation limitation recorded above. Other application and live-editor limitations remain unchanged.

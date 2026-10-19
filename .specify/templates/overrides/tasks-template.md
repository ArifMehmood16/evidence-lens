# Tasks: [FEATURE]

**Input**: This feature's spec.md, plan.md, research.md, and applicable contracts.

Use stable T001-style IDs, [US1] story labels, exact paths, and requirement references. Replace examples with concrete tasks. Mark [P] only for independent work; this does not authorize spawning agents. Include meaningful tests required by the spec and constitution. Do not generate unused scaffolding.

## Phase 1: Prerequisites

- [ ] T001 Resolve [specific prerequisite] in [path] per [FR/SC/plan reference].

## Phase 2: User Story 1 — [Outcome]

**Independent validation**: [behavior and command/scenario].

- [ ] T002 [US1] Add [behavior/contract test] in [path] per [FR-001/US1 scenario].
- [ ] T003 [US1] Implement [smallest behavior] in [path] per [FR-001].

Repeat phases only for scoped stories. State dependencies and applicable recovery tests. Prefer regression tests demonstrating a defect before a fix where practical.

## Phase 3: Verification and completion

Run checks locally. GitHub Actions tasks are out of scope unless explicitly requested by the user.

- [ ] T004 Use ECC verification-loop and record commands, outcomes, acceptance mappings, and limitations in verification.md per Constitution V.
- [ ] T005 Run applicable RAG/frontend/infrastructure checks from plan.md; record evidence or explain N/A in verification.md per Constitution III–IV.
- [ ] T006 Reconcile documentation and affected specs, inspect the diff, and verify quickstart.md scenarios per plan.md.

Convergence runs after implementation. It appends remaining work as a new numbered phase without changing existing IDs or silently expanding intent. A checked task is not proof of acceptance; verification evidence must support it.

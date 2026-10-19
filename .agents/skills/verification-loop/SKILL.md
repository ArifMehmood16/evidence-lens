---
name: verification-loop
description: Verify a substantial EvidenceLens change or release using applicable build, type, lint, behavior, security, and diff checks, with an honest evidence report. Use after implementation or before a PR.
license: MIT
metadata:
  origin: ECC
---

# Verify the actual change

Run checks locally. Do not create, enable, or dispatch GitHub Actions unless the user explicitly requests it; remote CI is intentionally deferred for this project.

Adapted from affaan-m/ECC at 76aaa77df6adc5b889e689007bf99b9a4f74af34.
See ../../../third_party/ecc/LICENSE and ../../../docs/agent-tooling.md.

1. Inspect the diff and changed contracts. Read the relevant feature acceptance criteria and repository commands; do not assume npm or Python tooling is configured.
2. Run the applicable formatter/linter, type checks, and build. Preserve command exit status. Documentation-only changes need document and link checks rather than a fabricated application build.
3. Run behavior and integration tests appropriate to the change. For RAG configuration changes, use rag-change-evaluation. Do not manufacture tests to reach a coverage percentage.
4. Run configured secret/dependency/security checks where relevant. Do not print discovered credentials. A grep for key-like strings is not a security audit.
5. Inspect the final diff for unrequested edits, misleading claims, source-license violations, personal paths, and migration/rollback gaps.
6. Report each check as passed, failed, or not run with its reason. In the Spec Kit workflow, save commands, outcomes, checked change scope, acceptance mappings, remaining risks, and evidence links in the current feature's verification.md. Use .specify/templates/overrides/verification-template.md as a guide. Small fixes may use the PR instead. Never label unrun checks green.

Before Spec Kit convergence, read this report alongside spec.md, plan.md, and tasks.md. Missing required evidence remains incomplete work; convergence appends remediation tasks and implementation resolves them. Keep all work in the same feature artifacts.

Fix relevant failures and rerun affected checks. Do not repeatedly run an unchanged full suite once meaningful verification passes. Missing tooling does not authorize global installation, bypassing controls, or unrelated cleanup.

# Edition 0001 — Skill readiness and evidence of use

**Root:** [EL-MASTER-1.0.0](../../master-plan-v1.0.0.md), original P05/P08/G07.  
**Immediate parent:** [baseline manifest](../../baseline.json); exact digest in manifest.json.  
**Issued:** 2026-10-19 | **Scope:** the user's request to improve reliable skill use across hosts.

## Reason and inherited intent

A skill committed to Git does not demonstrate that a host discovered or loaded it, or that an agent applied it. This child elaborates the original [engineering and evidence invariants](../../master-plan-v1.0.0.md#architecture-and-engineering-invariants) and G07 local governance. All original features, acceptance criteria, source policies, local-only checks, and authorization boundaries are inherited unchanged.

## Explicit additions

- **Add P05.FR001:** keep one canonical project skill body and provide small native Claude Code entry points for the existing four project skills. Codex and Cursor use the documented .agents path. Acceptance: each entry resolves correctly; broken routing fails preflight.
- **Add G07.FR001:** run a local stage-specific readiness/context check for substantial work. It validates relevant file configuration, planning lineage, and upstream command integrity and prints selected skill paths/hashes; optional context output explicitly loads those bodies into the session. Acceptance: missing routing, changed upstream assets, and canonical freshness changes are observable.
- **Add P08.FR001:** verification distinguishes configured, discovery observed, loaded, and applied-with-evidence. Acceptance: no tool/agent report infers live execution from a file or --host label; concrete actions and evidence links support claims of application.

No existing ID is replaced or retired. No root application scope or release threshold changes.

## Derived implementation artifacts

[Feature spec](../../../../specs/002-agent-readiness/spec.md) and [plan](../../../../specs/002-agent-readiness/plan.md) define DEV002.W01–W03 and AC1–AC3. Research, execution tasks, and verification stay in the same feature directory. The spec, plan, and this edition are sealed by manifest.json; mutable result/status records are excluded.

## Limits and migration

Existing projects need no data migration. Editor sessions may need a refresh and explicit skill selection. The preflight does not inspect host internals, invoke models, modify global settings, add hooks, or enable GitHub Actions. It cannot prove comprehension or prevent deliberate bypass. Actual per-host smoke-test observations must be recorded when performed.

A later change to this issued intent needs edition 0002 or its then-current successor, with references to the original master and immediate predecessor.

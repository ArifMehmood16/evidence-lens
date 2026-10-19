# Feature Specification: Agent skill readiness and use evidence

**Feature:** DEV-002 | **Date:** 2026-10-19 | **Status:** Implemented; see verification.md  
**Root:** [EL-MASTER-1.0.0](../../docs/planning/master-plan-v1.0.0.md), P05/P08/G07.  
**Parent:** docs/planning/baseline.json; digest recorded in child manifest.  
**Edition:** [0001](../../docs/planning/editions/0001/edition.md).

## Problem and scope

A committed skill proves that guidance is present in a checkout. It does not prove editor discovery, context loading, or application to a task. The user requests a practical improvement across the existing Spec Kit/ECC workflow.

Improve local discovery, explicit loading, and verification evidence. Preserve canonical skills and upstream command hashes. Live editor automation, model API calls, automatic hooks, global settings, and GitHub Actions are outside this change.

## Requirements and acceptance

- **P05.FR001 — Portable discovery:** expose the four canonical project skills through Claude Code native routing entries. Codex and Cursor continue using .agents/skills as supported by their documented discovery paths. **AC1:** each Claude entry resolves to the correct canonical file, without copying its procedural body; a missing/broken entry fails the local preflight.
- **G07.FR001 — Explicit local preflight:** provide a read-only command selecting host, stage, and optional RAG/frontend guidance. **AC2:** it validates planning integrity, relevant upstream skill integrity, disabled event settings, and native routes; prints canonical paths/hashes; and can print relevant skill contents into session context. A canonical update changes its reported hash; a modified upstream command fails.
- **P08.FR001 — Honest use evidence:** distinguish configuration present, host discovery observed, guidance loaded, and application evidence. **AC3:** command output never marks discovery/application verified merely from file inspection. Verification guidance requires canonical path/hash, concrete action, evidence location, and stated host limitations.

## Scenarios and boundaries

A contributor opens this repository in Claude Code and explicitly selects /evidencelens-search-first; the route instructs it to read the canonical ECC adaptation. In Codex/Cursor, the canonical project skill can be selected directly or loaded by explicit preflight context.

A setup check may pass while an editor hides skills due to workspace/trust settings or a session cache. That is reported as unobserved host discovery, not success. A user-provided --host value is a label, not host authentication. Self-reported use must be supported by observable research, code, checks, or reviewed outputs.

No additional root application features or performance claims are introduced. An ordinary chat with no filesystem/tool access must receive the relevant guidance through its available file/context workflow.

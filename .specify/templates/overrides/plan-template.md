# Implementation Plan: [FEATURE]

**Feature**: [identifier] | **Date**: [DATE] | **Spec**: [spec.md](spec.md)

## Summary

[Implementation approach and scope; requirement identifiers.]

## Technical Context

- Language/runtime and target environments: [versions; laptop and cloud implications].
- Dependencies and storage: [existing capabilities first; chosen additions].
- Testing and evaluation: [commands/tools or explicit setup tasks].
- Scale and resource budgets: [workload, memory, latency, throughput, cost, or N/A reason].
- Constraints and unknowns: [mark unresolved decisions NEEDS CLARIFICATION].

## Constitution Check

Check .specify/memory/constitution.md before research and after design. Record pass, unresolved, or N/A with reason for: one workflow; library reuse/SOLID; provenance/security; measurable scaling/recovery; evidence-backed completion. Resolve blocking violations before implementation.

## Phase 0: Research using ECC

Read .agents/skills/search-first/SKILL.md. Search repository capabilities and maintained upstream libraries. Save decisions, alternatives, sources/pinned versions, license/security implications, and reasons for custom code in this feature's research.md. Link an ADR only for consequential lasting decisions. Do not create an additional ECC plan.

## Phase 1: Design and contracts

[Responsibilities and real I/O boundaries; affected modules; lifecycle/state transitions; interface compatibility; migrations, rollback, and recovery; telemetry and redaction.]

Create data-model.md and contracts/ only when needed; explain N/A otherwise. Write quickstart.md with executable acceptance scenarios and expected outcomes. Keep implementation code out of design documents.

## Project Structure

[Actual affected paths, including specs/FEATURE/{spec,plan,research,tasks,verification}.md. Do not invent unused packages.]

## Verification and release gates

Use .agents/skills/verification-loop/SKILL.md during implementation and before completion. Save commands, outcomes, acceptance mappings, limitations, and checked revision/change scope in verification.md. Define required build/type/lint/behavior/security checks and justified N/A categories now.

Evidence-affecting changes also use rag-change-evaluation with baseline/candidate corpus/model/config identifiers. Public frontend changes also use frontend-release-review. Infrastructure changes include deployment, health, rollback/recovery, and cost evidence appropriate to scope. A missing required check stays incomplete.

After implementation, converge against spec, plan, tasks, and verification.md. Append missing work to tasks.md, implement it, and refresh evidence. Reconcile changed contracts with affected earlier specs.

## Complexity Tracking

[Only actual exceptions or consequential tradeoffs: need, simpler alternative, evidence, owner, review condition. Remove if none.]

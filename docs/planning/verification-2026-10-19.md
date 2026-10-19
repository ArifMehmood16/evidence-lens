# Planning baseline audit and verification

**Date:** 2026-10-19. **Scope:** EL-MASTER-1.0.0, its edition process, local checker, and shared agent guidance; based on repository revision d09abf8. This is an execution record, not an amendment to the master.

## Audit findings and resulting plan

The existing architecture, evaluation/scaling specifications, and nine-phase roadmap were substantial but lacked a complete application work-unit catalogue. Only the development-tooling feature had detailed Spec Kit artifacts. The prior policy allowed in-place specification updates, conflicting with the user's new master/child requirement.

The [original master](master-plan-v1.0.0.md) now records 24 features, 72 work units, 72 acceptance criteria, explicit unit dependencies, seven release gates, eight architecture/engineering invariants, and nine unresolved decisions. Each work unit includes inputs, output, acceptance, verification, and a common sizing/readiness/completion policy. Application status remains Planned. Provider, source, budget, and review decisions are not fabricated as settled.

The master and six supporting documents are sealed in baseline.json. No child edition has been issued yet. Future intent changes require child files with original-ID references, immediate-parent hashes, and explicit add/replace/retire declarations. Spec Kit templates, ECC verification, AGENTS.md, constitution 2.0.0, contributor guidance, and PR guidance now follow that rule. Prior supporting documents are preserved rather than rewritten.

## Local verification

- `python3 tools/check_planning.py` passed: 24 features, 72 units, zero child editions, seven sealed files. All unit dependency references resolve; the graph has no cycles.
- `python3 -m unittest discover -s tests/tooling -v` passed eight tests: four existing Spec Kit smoke/integrity checks plus baseline-mutation, parent-digest, committed-manifest-rewrite, and cycle regression checks.
- `npx --yes markdownlint-cli2@0.18.1` passed on authored documents, templates, rules, and skills.
- Local Markdown file/anchor review passed (58 targets). Git initially flagged intentional Markdown two-space hard breaks; .gitattributes delegates Markdown line-ending whitespace to markdownlint MD009, which permits those breaks and still checks excess whitespace. `git diff --check` then passed without changing sealed document bytes. New application features were not implemented or claimed tested.

## Limits and remaining decisions

This establishes a full feature-level planning baseline, not all future library choices, concrete endpoint schemas, clinical review, or measured quality/capacity. Implementation-ready child specs resolve those details before dependent work, under D01–D09 and the definition of ready.

The checksum and Git-history checks detect accidental changes when run locally; they cannot prevent deliberate bypass or history rewriting. Agent instructions require review. GitHub Actions remains disabled and no workflow is added. Cloud resources, model calls, domain changes, and external posting were not performed.

## Convergence

The requested master catalogue, acceptance mapping, work-unit decomposition, original/child references, and preservation policy are present. Local verification found no remaining baseline integrity or dependency gap. Working status records are separate from sealed intent; future planning corrections must be issued as children rather than edits to the originals.

# EvidenceLens Constitution

## I. One workflow across the application

Every substantial behavior, interface, infrastructure, or evaluation change MUST follow Spec Kit's specify → plan → tasks → implement → converge lifecycle. This applies to source admission, ingestion, retrieval, generation, APIs, practitioner UI, security, deployment, and operations. Canonical intent lives in specs/FEATURE/spec.md and plan.md; tasks.md tracks delivery. Architecture and roadmap documents provide context, not a competing backlog.

ECC MUST operate inside this lifecycle: use .agents/skills/search-first/SKILL.md during planning and save reuse research in the feature's research.md; use .agents/skills/verification-loop/SKILL.md during implementation and save actual evidence in verification.md. Do not create separate ECC requirements or tasks. Small behavior-preserving fixes may record scope and evidence in their PR, while reconciling affected specifications.

## II. Purposeful implementation and library reuse

Implementations MUST address explicit requirements with the smallest useful design. Evaluate maintained libraries before custom infrastructure. Apply SOLID through cohesive responsibilities and narrow interfaces at real boundaries; prefer composition and use OOP where state or invariants benefit. Follow docs/engineering-standards.md. Abstractions, services, dependencies, and design patterns require a concrete reason. Research may run inline; no stage requires delegation. Do not generate unused data models, contracts, or code scaffolds; explain inapplicable artifacts in the plan.

## III. Evidence integrity and security

RAG work MUST preserve provenance, version, permissions, source locators, and evidence qualifiers. Retrieved content is untrusted data. Relevance, source quality, evidence sufficiency, and claim support remain distinct. No zero-hallucination guarantee or confidence claim based on similarity alone. Apply docs/evaluation.md and .agents/skills/rag-change-evaluation/SKILL.md to evidence-affecting changes.

Applicable OWASP-oriented controls, failure behavior, data/license boundaries, and authorization tests MUST be specified before implementing exposed behavior. Follow SECURITY.md and docs/engineering-standards.md. Public frontend work MUST use .agents/skills/frontend-release-review/SKILL.md; private sessions and staging retain indexing restrictions and access controls.

## IV. Observable, testable scaling

Each substantial change MUST define observable acceptance criteria and applicable tests or experiments. Plans MUST state failure/recovery behavior and relevant latency, throughput, memory, cost, or quality budgets, with N/A reasons when appropriate. Describe datasets, document/chunk counts, workload, hardware, model/config versions, and uncertainty for scale results. Laptop and cloud runs SHOULD share contracts and configuration semantics. Projected capacity is not measured capacity.

## V. Completion requires evidence

Verification MUST run locally during project development. GitHub Actions MUST remain disabled; do not add, enable, dispatch, or restore workflows until the user explicitly requests it. Roadmap phases, toolkit defaults, and release readiness do not grant that authorization. Local quality checks remain required where applicable.

Tasks MUST trace to requirements and include applicable verification work. Tests are required for meaningful behavior, security boundaries, and recovery contracts; avoid tests that mirror implementation or merely raise coverage. Implementation MUST record passed, failed, and not-run checks in verification.md, including commands, outcomes, scope, and limitations. Unrun checks never count as passes.

Convergence MUST assess implementation and verification evidence against spec, plan, tasks, and these principles. Missing required evidence is unfinished work. Preserve Spec Kit's append-only convergence contract: append remediation tasks without rewriting intent or implementation. Implementation then fixes gaps and refreshes evidence. Blocking failures or unmet acceptance criteria prevent completion; exceptions require a rationale, owner, and expiry and cannot override user instructions or evidence/security invariants.

## Governance

AGENTS.md routes agents here; docs/engineering-standards.md holds detailed policy. Templates in .specify/templates/overrides/ implement these requirements for all integrations. Project policy takes precedence over generic toolkit examples. User instructions retain precedence. Amend the constitution and affected templates together; explain the change and migration in the PR. Version breaking governance changes as major, new principles as minor, and clarifications as patch. Keep feature specs current using Git history; never rewrite requirements merely to make failing work pass.

Amendment 1.1.0: the user's project-wide instruction defers GitHub Actions until explicitly requested. Existing workflow configuration is removed; verification remains local. No application migration is required.

**Version**: 1.1.0 | **Ratified**: 2026-10-19 | **Last Amended**: 2026-10-19

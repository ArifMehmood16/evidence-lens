# EvidenceLens engineering standards

Proposed repository policy, 19 October 2026. These requirements guide implementation; they do not claim that tools, checks, or deployment controls are already installed.

## Purposeful implementation

GitHub Actions is deferred for the whole development project until the user explicitly instructs its introduction. Run applicable checks locally and preserve their evidence. Do not treat toolkit defaults, roadmap phases, or publishing code as permission to enable Actions or add workflows.

Every change must address an agreed requirement, measured failure, or documented operational need. Prefer a small working vertical slice. Avoid speculative services, unused interfaces, generated scaffolding, duplicated configuration, and abstractions with no demonstrated variation. Line count is neither a delivery target nor a quality metric.

Before writing infrastructure code, check the existing codebase and maintained libraries for the capability. Record a consequential dependency choice with its purpose, alternatives, maintenance status, license, operational cost, and replacement boundary. Use libraries for validation, migrations, authentication integrations, parsing, retries, telemetry, and accessible UI primitives where they meet the requirements. Do not rebuild mature capabilities merely to showcase code.

## Architecture and object design

Apply SOLID through cohesive responsibilities, narrow interfaces, substitutable implementations with contract tests, and dependencies directed toward domain contracts. Use composition before inheritance. Classes are appropriate for stateful adapters and domain objects with invariants; straightforward data transformations should remain functions. Do not force OOP or a design pattern onto every module.

Use adapters for storage, search, queues, parsers, and model providers; strategies for genuinely selectable retrieval policies; and dependency injection at application boundaries. Introduce repositories, factories, or other patterns only where they reduce concrete coupling or repeated behavior. Domain logic should not depend directly on HTTP handlers or cloud SDKs. Avoid a universal base service or generic repository that hides the behavior under test.

Keep one modular codebase initially, with separate API and worker execution where justified. Extract services only for measured independent scaling, ownership, or failure isolation. Reuse framework conventions instead of creating a parallel application framework.

## Specification before expansion

Each substantial feature follows the repository-wide Spec Kit + ECC lifecycle in [agent-tooling.md](agent-tooling.md). Specifications capture the user problem, scope, contracts, failures, acceptance criteria, security, observability, recovery, and evaluation cases. Spec Kit owns spec/plan/tasks; ECC research and verification feed the same feature directory. The [constitution](../.specify/memory/constitution.md) and shared template overrides govern every application area. Small behavior-preserving fixes can capture scope and evidence in the PR.

Use architecture decision records for choices that are costly to reverse. Changes to embeddings, chunking, prompts, thresholds, and index schemas must carry versioned configuration and evaluation evidence. No silent default changes that invalidate comparisons.

## Quality gates

Adopt formatting, linting, type checks, dependency locking, secret scanning, and vulnerability checks when the corresponding code exists. Candidate Python tooling is Ruff, a single chosen type checker, pytest, and a locked dependency manager. Frontend tooling should include TypeScript checking, linting, component behavior tests, accessibility checks, and Playwright for critical browser flows. Choose one tool for each responsibility and avoid overlapping pipelines.

Test domain invariants, integration contracts, failure recovery, and user-visible behavior. Use real database/search integrations for boundaries that mocks cannot establish. Add regression cases for verified defects. Do not demand arbitrary coverage percentages or tests that merely repeat implementation details. RAG quality gates are defined separately in evaluation.md.

Pull requests explain the requirement, implementation, verification, and limitations. Keep changes reviewable, remove dead code, and document justified tradeoffs. A check is only reported as passing when it actually ran; configured, skipped, and failed are distinct states.

## Security from the first implementation

Maintain a threat model and map applicable controls to OWASP ASVS and the OWASP guidance for LLM applications. Pin the referenced standard version when the control matrix is created. This is a verification framework, not a claim of OWASP certification.

Enforce authentication and object-level authorization server-side; use least-privilege service identities, managed secrets, parameterized queries, output escaping, secure session handling, CSRF controls where relevant, HTTPS, bounded request sizes, timeouts, quotas, and redacted logs. Validate external URLs against SSRF risks, including redirects and private-network destinations. Isolate document parsing and constrain file types, sizes, decompression, and execution time.

Treat retrieved documents as untrusted data. Protect source admission, provenance, cache authorization scope, deletion propagation, and index integrity. Test prompt injection, poisoned documents, unsupported claims, sensitive-data disclosure, cross-user retrieval, unsafe output handling, and excessive model consumption. Models must not receive unrestricted tools or execute instructions found in a source. Security-critical failures block release; accepted exceptions need a reason, owner, and expiry.

## Frontend quality and search visibility

For public landing pages, documentation, and explicitly published content: provide a sitemap containing canonical indexable URLs, a deliberate robots policy, unique titles and descriptions, consistent canonical URLs, one main H1 with logical heading hierarchy, descriptive internal links, clean URL slugs, accessible images, compressed responsive assets, mobile layouts, HTTPS, and Open Graph metadata/images. Use structured data only when it accurately represents visible content and fits the page type.

Do not remove noindex globally. Authenticated practitioner sessions, personal queries, unpublished briefs, and staging deployments must not become public search content. Authentication provides access control; robots.txt and noindex do not. Where noindex is used, account for crawler access needed to observe it. Never place private routes or user query URLs in the public sitemap.

Test keyboard navigation, focus visibility, labels, contrast, loading/error states, and screen-reader semantics against applicable WCAG 2.2 AA criteria. Decorative images use empty alternative text; informative images describe the information conveyed. Do not add keyword-stuffed alt text.

Measure Core Web Vitals and page weight on representative mobile conditions. Lab checks provide early regression detection; field measurements are needed after real traffic exists. Broken-link checks include both internal routes and canonical metadata. A framework's SEO or image component is preferred to duplicate custom plumbing when suitable.

Search Console verification is a deployment task requiring access to the selected domain/property. A backlink strategy should prioritize useful research write-ups, reproducible benchmark reports, documentation, and relevant community participation. No purchased/spam links, automatic outreach, or unapproved messages. Neither verification nor backlink work is complete merely because it appears in this checklist.

## Agent rules and reusable skills

Use a concise root AGENTS.md as the shared repository policy, with narrow task-specific skills where repeated procedures justify them. Keep editor-specific files thin and consistent with that source of truth. Skills should have explicit triggers, inputs, steps, validation, and stopping conditions; avoid loading an entire external instruction collection into every task.

Before adopting ECC or another external agent toolkit, confirm the upstream repository, inspect its license and selected components, pin a revision, and review scripts, hooks, tools, and network behavior. Adopt only components that serve EvidenceLens. Do not auto-install global hooks or change user-wide editor settings as part of repository setup. The confirmed upstream is affaan-m/ECC. Two selected skills are installed as reviewed project-local adaptations; see agent-tooling.md for revision, license, and changes.

## Open source boundaries

The requested project license is Apache-2.0. Third-party libraries, models, datasets, source documents, and imported agent skills retain their own licenses and notices. The project license does not relicense source corpora. Publish reproducible acquisition manifests and only redistributable fixtures; exclude credentials, local user paths, raw private material, generated indexes, and tool-specific local state from Git.

Apache-2.0 is permissive: it allows proprietary derivatives subject to its terms. Publishing this repository under Apache-2.0 makes this code open source but does not require downstream modifications to remain open source.

## References to verify during implementation

- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
- [OWASP GenAI risks](https://genai.owasp.org/llm-top-10/)
- [Google indexing controls](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

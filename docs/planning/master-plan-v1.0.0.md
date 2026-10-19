# EvidenceLens master development plan — v1.0.0

**Document ID:** EL-MASTER-1.0.0  
**Issued:** 2026-10-19  
**State:** Sealed planning baseline; application implementation is not complete.  
**Owner:** Project owner (Arif Mehmood); engineering and practitioner review roles are assigned per work unit.

## Authority and edition policy

This file is the original master copy. Do not edit, overwrite, renumber, or replace it after sealing, including to fix a typo. Publish future intent changes as new child editions under docs/planning/editions/, following the [edition procedure](README.md). Each child references this original file, its stable IDs, and its immediate parent edition. A child contains explicit changes rather than an untraceable copied plan. Unchanged intent is inherited.

This master establishes application scope, feature outcomes, acceptance criteria, work boundaries, dependencies, and release conditions. Feature implementation plans elaborate these requirements through Spec Kit and ECC; they must not silently redefine them. If this master and an older supporting document differ, this master governs. Applied child changes supersede only the IDs they explicitly identify. Git history and local checks provide auditability, not tamper-proof storage or automatic model compliance.

The baseline manifest seals this master and the existing [architecture](../architecture.md), [evaluation specification](../evaluation.md), [scaling model](../scaling.md), [phase estimates](../development-plan.md), and [engineering standards](../engineering-standards.md). Their current bytes are preserved. They retain their original draft labels and historical wording; that does not permit editing their sealed content. Their unknowns remain unknown. Operational guidance and working status records can change, but accepted intent must change through a child edition.

## Audit result and planning completeness

Before this baseline, the repository had a substantive architecture, a nine-phase roadmap, proposed quality/capacity targets, and one detailed tooling feature. It did not have a complete application feature/work-unit breakdown or an immutable master/child edition contract. This baseline supplies that missing planning structure.

There are **24 features, 72 work units, and 72 unit acceptance criteria** below. All application units are planned, not completed. Read this together with decision register D01–D09: a complete plan records decisions that remain to be made; it does not pretend that sources, credentials, budgets, providers, or clinical review have already been agreed. Concrete library versions, endpoint schemas, and migration details are resolved in child feature specifications before dependent coding.

## Product contract

The primary user is a practitioner investigating supplement evidence. The three outcomes are: investigate an evidence question; audit a published claim; inspect disagreement between findings. The result is an evidence brief with source passages, evidence type, population, formulation, reported dose/duration/outcome, limitations, conflicting findings, missing evidence, and corpus/index versions.

Scope begins with English material and a proposed topic set of magnesium, vitamin D, omega-3, and creatine, subject to D01. Diverse verifiable research, expert commentary, creator material, newspapers, magazines, books, and practitioner case studies are eligible only after source admission and permission review. Reputation is contextual metadata; it does not establish claim correctness. Research ranking alone neither admits nor rejects a source.

Patient records, individual prescribing, autonomous clinical decisions, guaranteed zero hallucination, comprehensive systematic-review claims, and undisclosed full-text access are excluded. Commentary may establish what somebody said without establishing a treatment effect. No mention of a safety issue is not proof of safety.

## Architecture and engineering invariants

- **P01 — Separate pipelines:** asynchronous replayable ingestion and bounded query serving share versioned evidence contracts. Start with a modular codebase and API/worker processes; add services only for measured needs.
- **P02 — Preserve evidence:** source/document/version/span/chunk/study/claim/index/query identities and qualifiers remain traceable. Publish complete versions only, pin one physical index per query, and enforce current exclusions on retrieval, caches, release, and rollback.
- **P03 — Bounded generation:** retrieve lexical and dense candidates, fuse/deduplicate, optionally rerank, build budgeted context, assess sufficiency, generate structured claims, and verify before release. At most one follow-up retrieval and one revision in the initial policy.
- **P04 — Measure distinct concepts:** source credibility, retrieval relevance, evidence sufficiency, support, useful coverage, and operational failure remain separate. Raw similarity and self-reported model certainty are not calibrated probabilities.
- **P05 — Reuse deliberately:** use maintained libraries/frameworks and real boundary adapters; apply SOLID, composition, typed contracts, and OOP only where state/invariants justify it. No speculative abstraction count or generated-code volume target.
- **P06 — Local and portable:** the M5/24 GB/1 TB laptop is a bounded development profile, not the architecture's capacity ceiling. Proposed Python/FastAPI, PostgreSQL, OpenSearch, object storage, and React/TypeScript choices remain benchmarkable through adapters. AWS is a reference deployment assumption, not an authorization or irrevocable vendor choice.
- **P07 — Local checks only:** GitHub Actions remains disabled throughout development until the user's explicit instruction. No pipeline, toolkit, milestone, or plan grants permission to enable it. Cloud spend, deployment, domain verification, and external posting also require the applicable user authorization.
- **P08 — Honest evidence:** no fabricated completion, benchmark, security audit, practitioner signoff, or clinical validation. Record actual commands, versions, failures, limitations, and measured workload. No secrets or nonredistributable corpora in the public repository.

## Delivery, sizing, and dependency rules

A work unit is a reviewable outcome with one acceptance criterion and a named verification method. Each is initially sized at roughly **0.5–2 focused engineering days**, not a delivery promise. If discovery makes a unit larger, a child edition decomposes it into new subordinate IDs and preserves the original outcome. Do not rename old IDs or split units merely to inflate activity. The older 47–74-day phase estimate is a rough starting estimate; do not sum it with these unit sizes or claim a precise calendar schedule. Re-estimate from observed work through a child edition.

The project owner is initially the implementation/decision owner; practitioner label review and independent security review are explicit roles, not assumed available staff. A unit may start only when its required inputs and decisions are resolved or a child explicitly permits an isolated experiment. Unit dependencies below form a DAG, not the numbered chapter reading order. Parallel opportunities do not authorize spawning agents.

Every unit follows: relevant baseline IDs → child feature spec/plan → ECC reuse research → scoped tasks → implementation → local verification → convergence. Reuse the same feature artifacts; do not create a second ECC backlog. Unsealed drafts may be refined. Seal accepted spec/plan intent in an edition manifest before relying on it as an implementation baseline. Task status and measured results are execution records; changes to required behavior, acceptance criteria, or dependencies require a new edition.

**Definition of ready:** parent/root references exist; unit scope and boundaries are clear; dependencies and blocking decisions are resolved; applicable fixtures, controls, budgets, and verification are named. **Definition of done:** acceptance evidence exists, applicable local checks pass, changes remain in scope, provenance/security constraints hold, limitations are recorded, and convergence finds no unaddressed required work. An intentionally blocked cloud task is neither failed nor completed.

## Release gates

These gates are proposed acceptance targets, not achieved results. Ratify or amend numeric targets through a child edition using development evidence before accessing the locked release test. Never retrospectively reduce a threshold to relabel a failed run.

- **G01 — Contract and critical fixtures:** all declared fixture citations resolve to real eligible versions/spans; zero invented citations and zero accepted critical unit/dose/population substitutions in the fixed release suite. Replay, partial publication, in-flight deletion, and rollback fixtures pass. This finite gate is not a universal zero-error claim.
- **G02 — Domain quality:** on the declared held-out release, proposed Evidence Recall@20 ≥0.90; citation correctness and completeness each ≥0.95; unsupported factual claim rate ≤0.02; useful answer coverage ≥0.70 on gold-answerable questions; correct abstention ≥0.90 on gold-unanswerable questions. Report study/passages separately, critical slices, denominators, 95% clustered intervals, and answers containing any unsupported claim. Wide uncertainty means preliminary evidence.
- **G03 — Evaluation independence:** 30 seed and 200 development items precede a separately locked 400-item release with reviewed labels, study/query-family separation, documented practitioner review coverage, and no tuning on locked labels. Shortfalls require a child decision before claims. Inspecting holdout failures for tuning requires a new holdout.
- **G04 — Declared operational profile:** local resource/latency budgets are established by D08; no invented laptop throughput guarantee. For an authorized cloud pilot, proposed ≤100,000 chunks at 5 offered RPS, p95 retrieval/reranking ≤1.5 s, p95 verified brief ≤15 s, and <1% infrastructure errors over 30 steady minutes, with 8,000 evidence tokens and 500 output tokens maximum. Include provider quotas and queueing. Proposed monthly 99.5% availability and discovery-to-search freshness ≤24 h require ongoing observation; a short run does not prove them. This cloud gate does not block a clearly labelled local-only release.
- **G05 — Reproducibility and claims:** every experiment/release records code/config/corpus/model revisions, raw outputs, environment, actual document/chunk counts, warm/cold state, stage timings, usage, cost assumptions, and known regressions. Ten million documents remains a projection until actually exercised; synthetic load cannot prove domain quality.
- **G06 — Security and permission:** applicable input/egress, identity/authorization, parser, output, secret, retention, license, and isolation controls pass declared tests before external exposure. Security-critical unresolved issues block the affected release; no checklist is a certification.
- **G07 — Development governance:** local checks remain runnable and honest; Actions is disabled; sealed baseline and edition lineage checks pass. No draft child changes effective intent before it is sealed.

## Milestones and first implementation path

1. **M0 — Evidence definition:** F01–F03 establish the user/source/question contracts; D01/D02/D07/D09 are recorded. Source permission precedes acquisition.
2. **M1 — Local evidence path:** F04–F11 establish the complete ingestion/retrieval/answer path. Implement narrow examples inside these units first; do not call an entire feature complete from a single happy-path demonstration. F11.W03 demonstrates ingestion replay and one traceable answer.
3. **M2 — Inspectable practitioner baseline:** F12, F16.W01, and F18.W01 make the baseline usable, measurable, and diagnosable. Security is developed alongside interfaces, not postponed until a cloud deployment.
4. **M3 — Reliable retrieval and release:** F13–F16 plus relevant F17 controls produce controlled optimization, verified release, claim audit, and held-out quality evidence.
5. **M4 — Authorized cloud readiness:** F17–F20 establish access, caching, exclusion propagation, and deployment/recovery evidence only after explicit authorization and budget.
6. **M5 — Measured scale and resilience:** F21–F22 exercise capacity and recovery on declared, authorized environments.
7. **M6 — Reviewable portfolio:** F23–F24 produce public-facing readiness and reproducible case studies. A local demo may be published as such; unavailable cloud results remain clearly planned.

## Feature and work-unit catalogue

Each work-unit heading is a stable ID. Its acceptance criterion has the matching AC suffix within the feature. Links from children may point to a feature anchor (for example #f01) and name the exact work/acceptance ID. Proposed directories in outputs describe responsibility, not a requirement to scaffold empty packages.

## F01

**Practitioner workflow and evidence contract**  
**Roadmap phase:** 0  
**Feature outcome:** Scope decision record with first topics, review availability, and explicit exclusions.  
**Implementation status at baseline:** Planned.

### F01.W01

**Define the three practitioner journeys**  
**Depends on:** None; resolve relevant decision-register inputs.  
**Input:** Original requirements and practitioner feedback.  
**Deliverable:** Product brief and 30 seed questions covering investigation, claim audit, disagreement, and absence of evidence.  
**Acceptance F01.AC01:** Every question has a workflow, intended user outcome, required qualifiers, answerability expectation, and prohibited inference; absent practitioner review is labelled.  
**Verification:** Review the 30 cases against the brief; no individual treatment recommendations or patient-data workflows are included.

### F01.W02

**Define the evidence brief schema**  
**Depends on:** F01.W01  
**Input:** F01.W01.  
**Deliverable:** Versioned typed schema and example supported, partial, conflicting, and unavailable briefs.  
**Acceptance F01.AC02:** Examples distinguish studied dose from recommendation, evidence gap from outage, and unknown safety information from absence of risk; invalid citation references fail validation.  
**Verification:** Schema tests accept each response type and reject missing provenance or unsupported enum combinations.

### F01.W03

**Define release scope and exclusions**  
**Depends on:** F01.W02  
**Input:** F01.W02 and open decisions D01–D03.  
**Deliverable:** Scope decision record with first topics, review availability, and explicit exclusions.  
**Acceptance F01.AC03:** English-first topic scope and source types are recorded; patient records, autonomous clinical action, and universal zero-error claims are excluded.  
**Verification:** Review scope against all seed questions; record unanswered practitioner questions without fabricating agreement.

## F02

**Source admission and permissions**  
**Roadmap phase:** 0  
**Feature outcome:** Evidence-type and expertise rubric plus study-link provenance rules.  
**Implementation status at baseline:** Planned.

### F02.W01

**Model the source registry**  
**Depends on:** F01.W03  
**Input:** Approved product scope.  
**Deliverable:** Registry schema, admission checklist, and allowed/blocked/pending source examples.  
**Acceptance F02.AC01:** Identity, category, acquisition route, attribution, access and reuse basis, retention, review date, update policy, and approval state are mandatory or explicitly unknown.  
**Verification:** Fixtures cannot become ingestion-eligible with pending permission or unverifiable identity.

### F02.W02

**Implement admission checks**  
**Depends on:** F02.W01  
**Input:** F02.W01.  
**Deliverable:** Source-policy evaluator and auditable decision record.  
**Acceptance F02.AC02:** Only eligible routes fetch material; public availability never substitutes for permission; abstract-only and full-text coverage stay distinguishable.  
**Verification:** Allowed, revoked, missing-license, prohibited route, and expired-review fixtures produce the expected decisions.

### F02.W03

**Appraise heterogeneous evidence**  
**Depends on:** F02.W02  
**Input:** F02.W02.  
**Deliverable:** Evidence-type and expertise rubric plus study-link provenance rules.  
**Acceptance F02.AC03:** Blogs, newspapers, creator material, books, and research retain their types; prestige is not truth; reports derived from one study do not count as independent confirmation.  
**Verification:** Review mixed-source examples including low-ranked research and credible commentary; preserve unknowns and conflicts.

## F03

**Seed corpus and question annotations**  
**Roadmap phase:** 0–2  
**Feature outcome:** 200 reviewed development questions with query-family identifiers.  
**Implementation status at baseline:** Planned.

### F03.W01

**Acquire a representative seed manifest**  
**Depends on:** F01.W03, F02.W03  
**Input:** Admitted sources and scope.  
**Deliverable:** Approximately 100 eligible documents with source/version/license references.  
**Acceptance F03.AC01:** Every included item has an acquisition decision and provenance; fewer items are acceptable with a documented coverage gap rather than padding.  
**Verification:** Audit the full seed manifest and a sample of original passages; distribute only permitted fixtures.

### F03.W02

**Label seed questions**  
**Depends on:** F03.W01, F01.W01  
**Input:** F03.W01 and F01.W01.  
**Deliverable:** 30 annotated seed questions and reviewer guide.  
**Acceptance F03.AC02:** Each item identifies evidence spans, study/document IDs, required qualifiers, prohibited inferences, answerability, and reviewer rationale.  
**Verification:** Double-review a declared sample, record disagreements and review availability; model-generated labels remain provisional.

### F03.W03

**Expand the development set**  
**Depends on:** F03.W02  
**Input:** F03.W02.  
**Deliverable:** 200 reviewed development questions with query-family identifiers.  
**Acceptance F03.AC03:** Coverage includes numeric terms, aliases, formulations, populations, conflicting findings, and unanswerable cases; duplicates/families are labelled.  
**Verification:** Report category counts and unresolved labels; split candidates for later holdout without inspecting holdout answers during tuning.

## F04

**Local runtime and domain contracts**  
**Roadmap phase:** 1  
**Feature outcome:** Compose profile for database/search and local blob adapter.  
**Implementation status at baseline:** Planned.

### F04.W01

**Establish minimal runnable packaging**  
**Depends on:** F01.W03  
**Input:** Domain brief contract and library research.  
**Deliverable:** Locked Python environment, API/worker entry points, and local configuration examples.  
**Acceptance F04.AC01:** A clean setup starts a health endpoint and worker without credentials in source; configuration errors fail clearly.  
**Verification:** Fresh environment smoke run with valid and missing configuration; document actual commands.

### F04.W02

**Create storage and service boundaries**  
**Depends on:** F04.W01  
**Input:** F04.W01.  
**Deliverable:** Typed contracts for provenance, blobs, jobs, retrieval, and model calls.  
**Acceptance F04.AC02:** Domain types have stable IDs/version fields and do not import cloud or HTTP SDKs; adapters cover real variation only.  
**Verification:** Contract tests with simple adapters prove schema validation and substitution; no pass-through wrapper inventory.

### F04.W03

**Provide a bounded local profile**  
**Depends on:** F04.W02  
**Input:** F04.W02.  
**Deliverable:** Compose profile for database/search and local blob adapter.  
**Acceptance F04.AC03:** Startup, health, shutdown, data reset, and resource limits are documented; model execution mode is explicit and cannot silently send data externally.  
**Verification:** Run on the available laptop, record peak memory and disk; successful startup is not a production capacity claim.

## F05

**Acquisition and immutable snapshots**  
**Roadmap phase:** 1  
**Feature outcome:** Allowlisted HTML connector using shared acquisition contract.  
**Implementation status at baseline:** Planned.

### F05.W01

**Build one permitted structured connector**  
**Depends on:** F02.W03, F04.W03  
**Input:** Source registry and local adapters.  
**Deliverable:** Connector with pagination, rate limits, watermarks, and fixture responses.  
**Acceptance F05.AC01:** Interrupted acquisition resumes from recorded progress without skipping eligible records; disallowed destinations are never fetched.  
**Verification:** Replay paginated responses with duplicates, 429s, timeouts, and changed watermarks.

### F05.W02

**Persist source snapshots**  
**Depends on:** F05.W01  
**Input:** F05.W01.  
**Deliverable:** Content-addressed raw snapshot and version manifest.  
**Acceptance F05.AC02:** Original bytes, fetch time, modification metadata, source decision, content hash, and license snapshot are retained; changed bytes create a new version.  
**Verification:** Fetch an unchanged item twice and then an updated item; assert stable document identity and correct version count.

### F05.W03

**Add controlled HTML acquisition**  
**Depends on:** F05.W02  
**Input:** F05.W02.  
**Deliverable:** Allowlisted HTML connector using shared acquisition contract.  
**Acceptance F05.AC03:** Redirects and URL destinations are validated; bounded response size/time and crawl policy apply; logs do not expose secrets.  
**Verification:** Fixtures cover redirects, forbidden/private destinations, oversized responses, and changed pages.

## F06

**Parsing, OCR, and citation locators**  
**Roadmap phase:** 1  
**Feature outcome:** Quality checks and inspect/retry command.  
**Implementation status at baseline:** Planned.

### F06.W01

**Parse structured content with locators**  
**Depends on:** F05.W03  
**Input:** XML/HTML snapshots.  
**Deliverable:** Parser adapter emitting sections, evidence spans, and extraction diagnostics.  
**Acceptance F06.AC01:** Each span resolves to the original version and stable section/offset; HTML never receives invented page numbers.  
**Verification:** Round-trip citation fixtures verify exact source text/hash and section context.

### F06.W02

**Evaluate PDF and OCR profiles**  
**Depends on:** F06.W01  
**Input:** F06.W01.  
**Deliverable:** Parser comparison and permitted multi-column/table/scan fixtures.  
**Acceptance F06.AC02:** Tables retain headers, units, captions, and footnotes; uncertain OCR and reading order are flagged, not silently trusted.  
**Verification:** Inspect gold fixture regions and numeric tokens; select a profile with documented limitations.

### F06.W03

**Quarantine invalid extraction**  
**Depends on:** F06.W02  
**Input:** F06.W02.  
**Deliverable:** Quality checks and inspect/retry command.  
**Acceptance F06.AC03:** Malformed files, ambiguous numbers/tables, and missing provenance cannot publish; each item has a reason and reproducible retry path.  
**Verification:** Malformed and low-quality fixtures enter quarantine; corrected versions reprocess without losing prior failure evidence.

## F07

**Normalization, deduplication, and chunking**  
**Roadmap phase:** 1–3  
**Feature outcome:** Fixed-window baseline and section-aware child/parent chunk profiles.  
**Implementation status at baseline:** Planned.

### F07.W01

**Normalize identifiers and aliases**  
**Depends on:** F06.W03  
**Input:** Parsed records.  
**Deliverable:** Canonical bibliographic/ingredient fields and conservative study-link candidates.  
**Acceptance F07.AC01:** Original strings and units remain available; no unsupported elemental-mass conversion or silent study merge occurs.  
**Verification:** Fixtures separate compounds, formulations, ambiguous study matches, and identifier conflicts.

### F07.W02

**Deduplicate without deleting provenance**  
**Depends on:** F07.W01  
**Input:** F07.W01.  
**Deliverable:** Exact deduplication and candidate near-duplicate relationships.  
**Acceptance F07.AC02:** Exact repeats avoid duplicate processing; distinct publications remain citable; uncertain near-duplicates are not destroyed.  
**Verification:** Replay copies and related papers; confirm original source/version references survive.

### F07.W03

**Create versioned chunk manifests**  
**Depends on:** F07.W02  
**Input:** F07.W02.  
**Deliverable:** Fixed-window baseline and section-aware child/parent chunk profiles.  
**Acceptance F07.AC03:** Deterministic IDs include source version and chunker config; every chunk references original spans; table qualifiers stay attached.  
**Verification:** Repeat chunking with identical config and compare IDs; change config and verify new IDs and recorded token distributions.

## F08

**Durable ingestion and complete publication**  
**Roadmap phase:** 1  
**Feature outcome:** Completeness manifest and query-eligibility state transition.  
**Implementation status at baseline:** Planned.

### F08.W01

**Implement jobs, leases, and retries**  
**Depends on:** F07.W03, F04.W03  
**Input:** Stage contracts and normalized chunks.  
**Deliverable:** Durable job ledger with idempotency keys and bounded retry policy.  
**Acceptance F08.AC01:** Duplicate delivery performs no duplicate committed work; expired leases recover; poison jobs stop at the retry budget.  
**Verification:** Kill a worker before/after writes and before acknowledgement; replay and inspect terminal job counts.

### F08.W02

**Make stage handoff durable**  
**Depends on:** F08.W01  
**Input:** F08.W01.  
**Deliverable:** Outbox or equivalent transactional handoff and dispatcher.  
**Acceptance F08.AC02:** A committed stage cannot silently lose downstream work; re-dispatch remains idempotent.  
**Verification:** Crash between transaction commit and dispatch, restart, and verify eventual downstream processing.

### F08.W03

**Gate document-version publication**  
**Depends on:** F08.W02  
**Input:** F08.W02.  
**Deliverable:** Completeness manifest and query-eligibility state transition.  
**Acceptance F08.AC03:** No version becomes searchable until expected chunks and metadata are validated; partial indexing remains ineligible.  
**Verification:** Interrupt a batch mid-index and confirm zero eligible partial version; resume and confirm one complete published version.

## F09

**Embedding and index generations**  
**Roadmap phase:** 1–3  
**Feature outcome:** Shadow-build validation and alias switch/rollback procedure.  
**Implementation status at baseline:** Planned.

### F09.W01

**Batch and cache embeddings**  
**Depends on:** F08.W03  
**Input:** Validated chunk manifests awaiting embedding/index publication, and model decision D04.  
**Deliverable:** Token-aware embedding adapter and cache.  
**Acceptance F09.AC01:** Cache keys include content, preprocessing, and exact model revision; dimensions/model spaces cannot mix; rate-limit retries are bounded.  
**Verification:** Duplicate, model-change, dimension-mismatch, and throttling tests plus measured batch usage.

### F09.W02

**Build a validated physical index**  
**Depends on:** F09.W01  
**Input:** F09.W01.  
**Deliverable:** BM25/vector mappings and index-release manifest.  
**Acceptance F09.AC02:** Expected searchable counts and active-version filters match the manifest; incompatible embeddings reject publication.  
**Verification:** Index a fixture corpus and reconcile counts, versions, and query eligibility.

### F09.W03

**Support rebuild and atomic serving selection**  
**Depends on:** F09.W02  
**Input:** F09.W02.  
**Deliverable:** Shadow-build validation and alias switch/rollback procedure.  
**Acceptance F09.AC03:** Each query pins one physical release; failed builds never become active; rollback retains current exclusions.  
**Verification:** Run queries through an alias switch and failed rebuild; confirm no mixed-generation evidence or resurrected revoked source.

## F10

**Lexical and dense retrieval baselines**  
**Roadmap phase:** 2  
**Feature outcome:** BM25-only and dense-only raw results and run manifests.  
**Implementation status at baseline:** Planned.

### F10.W01

**Implement lexical retrieval**  
**Depends on:** F09.W03, F03.W02  
**Input:** Indexed fixture corpus.  
**Deliverable:** BM25 profile with explicit filters and exact-term preservation.  
**Acceptance F10.AC01:** Ingredient names, numeric terms, identifiers, and explicit source/date filters survive query construction; inferred filters are not forced.  
**Verification:** Expected fixtures retrieve exact identifiers and respect filter boundaries.

### F10.W02

**Implement dense ANN retrieval**  
**Depends on:** F10.W01  
**Input:** F10.W01.  
**Deliverable:** Dense profile with pinned embedding/query settings.  
**Acceptance F10.AC02:** Queries use the index model space; unsupported dimensions/configs fail clearly; ANN approximation and domain relevance are reported separately.  
**Verification:** Compare candidate retrieval with exact nearest-neighbor samples and labelled evidence queries.

### F10.W03

**Record reproducible baseline runs**  
**Depends on:** F10.W02  
**Input:** F10.W02.  
**Deliverable:** BM25-only and dense-only raw results and run manifests.  
**Acceptance F10.AC03:** Both use identical corpus/question versions and declared budgets; failures, costs, and stage timings remain in the report.  
**Verification:** Replay the baseline configuration and compare deterministic parts; document hosted-model nondeterminism.

## F11

**Bounded query API and cited baseline answers**  
**Roadmap phase:** 2  
**Feature outcome:** One-command licensed fixture demo from ingestion through brief.  
**Implementation status at baseline:** Planned.

### F11.W01

**Expose a typed bounded query contract**  
**Depends on:** F10.W03, F01.W02  
**Input:** Brief schema and retrievers.  
**Deliverable:** API input/output/error schemas and request limits.  
**Acceptance F11.AC01:** Invalid/oversized requests fail explicitly; question interpretation and explicit filters remain inspectable; timeouts differ from evidence gaps.  
**Verification:** Contract tests cover valid requests, ambiguity, invalid filters, timeout, and no evidence.

### F11.W02

**Generate structured cited drafts**  
**Depends on:** F11.W01  
**Input:** F11.W01.  
**Deliverable:** Generator adapter, prompt version, context budget, citation-ID validator.  
**Acceptance F11.AC02:** Every cited ID belongs to supplied evidence; model-generated URLs/unknown IDs are rejected; retrieved instructions cannot change tool authority.  
**Verification:** Adversarial prompt fixtures and fabricated IDs fail release; supported brief cites resolvable spans.

### F11.W03

**Complete the first vertical slice**  
**Depends on:** F11.W02  
**Input:** F11.W02.  
**Deliverable:** One-command licensed fixture demo from ingestion through brief.  
**Acceptance F11.AC03:** One document is acquired, parsed, indexed, cited, and replayed without duplicates; unsupported questions produce a gap; failure traces identify the stage.  
**Verification:** Fresh environment replay plus supported/unsupported query demo; do not label this initial validator clinically verified.

## F12

**Practitioner evidence workspace**  
**Roadmap phase:** 2  
**Feature outcome:** Feedback contract linked to query/claim/evidence IDs.  
**Implementation status at baseline:** Planned.

### F12.W01

**Provide question and result states**  
**Depends on:** F11.W03  
**Input:** Typed API contract.  
**Deliverable:** Minimal accessible question form and results view.  
**Acceptance F12.AC01:** Loading, evidence gap, partial answer, disagreement, and outage have distinct states; only release-checked factual text is shown.  
**Verification:** UI behavior tests cover every response type, keyboard submission, errors, and cancellation.

### F12.W02

**Build passage inspection**  
**Depends on:** F12.W01  
**Input:** F12.W01.  
**Deliverable:** Claim-to-source viewer with qualifiers and version details.  
**Acceptance F12.AC02:** Every displayed citation opens the correct version/span; source type, population, formulation, dates, and extraction warnings remain visible.  
**Verification:** Select citations across HTML, PDF, and table fixtures; no broken or invented locator is accepted.

### F12.W03

**Capture structured reviewer feedback**  
**Depends on:** F12.W02  
**Input:** F12.W02.  
**Deliverable:** Feedback contract linked to query/claim/evidence IDs.  
**Acceptance F12.AC03:** Feedback separates relevance, support, applicability, and critical-error reports; sensitive free text is bounded and retained only under policy.  
**Verification:** Submit and retrieve feedback for a fixture query; verify access, validation, and redacted logs.

## F13

**Hybrid retrieval and controlled optimization**  
**Roadmap phase:** 3  
**Feature outcome:** Reproducible optimization report and retained-config ADR.  
**Implementation status at baseline:** Planned.

### F13.W01

**Fuse and rerank candidates**  
**Depends on:** F10.W03, F16.W01  
**Input:** Baseline runs and evaluation harness.  
**Deliverable:** Hybrid fusion and cross-encoder candidate profile.  
**Acceptance F13.AC01:** Comparison holds corpus, generator, and unrelated settings fixed; reranker failure is explicit; candidate count/truncation is recorded.  
**Verification:** Paired BM25/dense/hybrid/reranked experiments include numerical, alias, and difficult-source slices.

### F13.W02

**Optimize context composition**  
**Depends on:** F13.W01, F07.W03  
**Input:** F13.W01 and F07.W03.  
**Deliverable:** Study-aware deduplication, parent expansion, and diversity controls.  
**Acceptance F13.AC02:** Context respects token budget and preserves qualifiers/contradictions; multiple summaries of one study cannot dominate as independent evidence.  
**Verification:** Ablate fixed versus structure-aware chunks and source diversity; inspect missing-qualifier and repeated-study cases.

### F13.W03

**Select the combined configuration**  
**Depends on:** F13.W02  
**Input:** F13.W02.  
**Deliverable:** Reproducible optimization report and retained-config ADR.  
**Acceptance F13.AC03:** Each retained optimization improves a declared target without violating predeclared critical-slice or cost/latency tolerances; combined profile is evaluated separately.  
**Verification:** Report paired uncertainty, negative experiments, runtime/memory/cost, and remaining regressions; rejected techniques stay experimental.

## F14

**Evidence sufficiency and verified release**  
**Roadmap phase:** 4  
**Feature outcome:** Development-only threshold configuration and release controller.  
**Implementation status at baseline:** Planned.

### F14.W01

**Assess sufficiency and bounded follow-up**  
**Depends on:** F13.W03, F11.W03  
**Input:** Evidence context and rubric.  
**Deliverable:** Sufficiency decision and one-follow-up retrieval policy.  
**Acceptance F14.AC01:** Missing required attributes are explicit; at most one targeted follow-up occurs; partial support does not become a full answer; raw similarity is not confidence.  
**Verification:** Answerable, partial, absent, contradictory, and highly similar irrelevant fixtures produce expected decisions.

### F14.W02

**Verify claims and critical qualifiers**  
**Depends on:** F14.W01  
**Input:** F14.W01.  
**Deliverable:** Claim-support, numeric/unit/population checks and evaluated judge adapter.  
**Acceptance F14.AC02:** Invalid citations and critical substitutions in fixed fixtures block release; judge disagreements with human labels are measured.  
**Verification:** Run all critical fixtures and a stratified human-reviewed sample of both failing and passing claims.

### F14.W03

**Calibrate release and abstention**  
**Depends on:** F14.W02  
**Input:** F14.W02.  
**Deliverable:** Development-only threshold configuration and release controller.  
**Acceptance F14.AC03:** At most one revision occurs; unsupported claims are removed or withheld; factual content is not streamed before checks; outages remain distinct.  
**Verification:** Sweep thresholds on development folds, publish risk/coverage and calibration evidence, and test worst-case call/token budgets.

## F15

**Claim audit and conflicting evidence**  
**Roadmap phase:** 4  
**Feature outcome:** Practitioner audit and disagreement view.  
**Implementation status at baseline:** Planned.

### F15.W01

**Extract an attributable public claim**  
**Depends on:** F14.W03, F12.W02  
**Input:** Permitted article/blog/transcript snapshot.  
**Deliverable:** Claim-audit input and verbatim claim/span references.  
**Acceptance F15.AC01:** Claim wording and qualifiers preserve the source; audit follows only permitted references; uncertain claim extraction asks for confirmation or marks uncertainty.  
**Verification:** Audit fixtures include qualified, exaggerated, and ambiguous claims with original span inspection.

### F15.W02

**Compare evidence on matching attributes**  
**Depends on:** F15.W01  
**Input:** F15.W01.  
**Deliverable:** Support/contradiction/insufficient-evidence comparison.  
**Acceptance F15.AC02:** Population, formulation, dose, endpoint, and duration mismatches are explained; genuine conflict is retained; no forced consensus or false independence.  
**Verification:** Cases distinguish noncomparable findings from direct conflict and repeated reports of one study.

### F15.W03

**Present a traceable audit brief**  
**Depends on:** F15.W02  
**Input:** F15.W02.  
**Deliverable:** Practitioner audit and disagreement view.  
**Acceptance F15.AC03:** Each finding cites underlying evidence or identifies a gap; commentary proves what was said, not automatically a clinical effect.  
**Verification:** Reviewer walkthrough follows each conclusion to its evidence and limitations; record review gaps.

## F16

**Evaluation datasets and release decisions**  
**Roadmap phase:** 2–4  
**Feature outcome:** Release report with raw evidence and limitations.  
**Implementation status at baseline:** Planned.

### F16.W01

**Build the reusable evaluation harness**  
**Depends on:** F03.W03, F11.W03  
**Input:** Development labels and baseline outputs.  
**Deliverable:** Versioned run schema, metrics, and reproducible evaluator.  
**Acceptance F16.AC01:** Recall/nDCG, citation correctness/completeness, unsupported claims, coverage, abstention, latency, and costs have explicit denominators; clustered intervals are reproducible.  
**Verification:** Use hand-calculable metric fixtures and repeated seeds; incomplete relevance judgements are disclosed.

### F16.W02

**Freeze holdout and release gates**  
**Depends on:** F16.W01  
**Input:** F16.W01.  
**Deliverable:** Sealed 400-item test manifest and gate decision edition.  
**Acceptance F16.AC02:** Target composition is 150 direct, 80 comparative, 60 conflicting, 60 unanswerable, 50 robustness; study/query-family leakage is checked; gates freeze before test access.  
**Verification:** Audit partitions and gate record; if counts/review coverage cannot be met, document the shortfall before any release claim.

### F16.W03

**Run the release evaluation**  
**Depends on:** F16.W02, F14.W03, F15.W03, F19.W03  
**Input:** F16.W02, F14.W03, F15.W03, and F19.W03 (current exclusions/cache safety fixtures).  
**Deliverable:** Release report with raw evidence and limitations.  
**Acceptance F16.AC03:** G01–G05 targets are evaluated on untouched holdout with intervals; failures remain visible; tuning after inspection requires a fresh holdout.  
**Verification:** Reproduce run manifests and critical-error adjudication; failing gates keep the release explicitly limited rather than silently relaxing thresholds.

## F17

**Authorization and security boundaries**  
**Roadmap phase:** 2–5  
**Feature outcome:** Security verification record and remediation tasks.  
**Implementation status at baseline:** Planned.

### F17.W01

**Define threats and local security tests**  
**Depends on:** F04.W03, F02.W03  
**Input:** Domain interfaces and acquisition policy.  
**Deliverable:** Versioned threat model and applicable OWASP control mapping.  
**Acceptance F17.AC01:** Threats include prompt injection, poisoning, SSRF, parsing abuse, sensitive logs, unauthorized retrieval/cache access, and resource exhaustion.  
**Verification:** Map each exposed boundary to a control/test; no claim of certification from a checklist.

### F17.W02

**Implement identity and bounded access**  
**Depends on:** F17.W01, F11.W01  
**Input:** F17.W01 and F11.W01.  
**Deliverable:** Framework-backed identity/authorization, quotas, and secret configuration.  
**Acceptance F17.AC02:** Object/source access and request limits are enforced server-side; cloud model/tool credentials cannot be supplied by retrieved text.  
**Verification:** Unauthorized, cross-scope, throttled, invalid-session, and secret-redaction tests fail safely.

### F17.W03

**Validate exposed-service controls**  
**Depends on:** F17.W02  
**Input:** F17.W02.  
**Deliverable:** Security verification record and remediation tasks.  
**Acceptance F17.AC03:** Before external exposure, transport/storage protection, least privilege, controlled egress, parser isolation, dependency review, and input/output defenses pass scoped checks.  
**Verification:** Run local adversarial suites; record scan scope and unresolved high-severity issues; no external deployment while blocking controls fail.

## F18

**Observability and failure attribution**  
**Roadmap phase:** 2–7  
**Feature outcome:** Latency/error/freshness/backlog metrics and operational thresholds.  
**Implementation status at baseline:** Planned.

### F18.W01

**Instrument ingestion and query stages**  
**Depends on:** F11.W03, F08.W03  
**Input:** Pipeline and job contracts.  
**Deliverable:** OpenTelemetry-compatible trace/metric schema.  
**Acceptance F18.AC01:** Request/job IDs join timings, retrieval ranks, versions, token usage, retry count, and outcome; secrets/private content are excluded by default.  
**Verification:** Replay success, parse failure, retrieval miss, generator failure, and policy rejection with explainable stage traces.

### F18.W02

**Build operator accounting**  
**Depends on:** F18.W01  
**Input:** F18.W01.  
**Deliverable:** CLI or minimal dashboard for jobs and query outcomes.  
**Acceptance F18.AC02:** Discovered, quarantined, processed, published, failed, and retried counts reconcile; evidence gaps do not inflate infrastructure success.  
**Verification:** Compare trace/accounting totals with fixture manifests and injected errors.

### F18.W03

**Define alert and SLO measurements**  
**Depends on:** F18.W02  
**Input:** F18.W02.  
**Deliverable:** Latency/error/freshness/backlog metrics and operational thresholds.  
**Acceptance F18.AC03:** Targets use observed baselines; availability excludes correct evidence gaps but includes service failures; freshness starts at discovery.  
**Verification:** Run representative failure and backlog scenarios; demonstrate detection and record false-positive/unknown cases.

## F19

**Caching, source updates, and exclusion propagation**  
**Roadmap phase:** 5  
**Feature outcome:** Rollback/rebuild exclusion reconciliation.  
**Implementation status at baseline:** Planned.

### F19.W01

**Cache exact retrieval and approved answers**  
**Depends on:** F14.W03, F17.W03, F09.W03  
**Input:** Versioned query contract.  
**Deliverable:** Exact-key cache with policy-aware eligibility checks.  
**Acceptance F19.AC01:** Keys include scope, filters, physical index, retrieval and policy versions; answer keys also include prompt/model/verifier/schema versions.  
**Verification:** Different population, dose, scope, index, and policy versions cannot share an incorrect cached answer.

### F19.W02

**Propagate replacement and revocation**  
**Depends on:** F19.W01  
**Input:** F19.W01.  
**Deliverable:** Dependency invalidation and current eligibility checks.  
**Acceptance F19.AC02:** Replacement/retraction/deletion invalidates dependent caches; eligibility is rechecked before release even for in-flight queries and cache hits.  
**Verification:** Delete a source during query execution and test cached/live paths; revoked evidence is not released.

### F19.W03

**Preserve exclusions through rollback**  
**Depends on:** F19.W02  
**Input:** F19.W02.  
**Deliverable:** Rollback/rebuild exclusion reconciliation.  
**Acceptance F19.AC03:** An older index cannot resurrect revoked content; permitted historical views are explicit and separate from current evidence.  
**Verification:** Revoke evidence, roll back the alias, and confirm retrieval, generation, and cache output still honor current policy.

## F20

**Cloud portability and deployment design**  
**Roadmap phase:** 5; execution gated  
**Feature outcome:** Deployment/rollback/restore record and measured cost.  
**Implementation status at baseline:** Planned.

### F20.W01

**Package equivalent local/cloud contracts**  
**Depends on:** F17.W03, F18.W03, F19.W03  
**Input:** Local profile and provider decisions.  
**Deliverable:** Versioned containers, configuration contracts, and architecture ADR.  
**Acceptance F20.AC01:** ARM64 local and chosen cloud images preserve the same evidence schema; provider adapters have explicit differences and no hidden business logic.  
**Verification:** Build locally and run adapter contract tests; record any untested cloud architecture.

### F20.W02

**Define infrastructure and operating limits**  
**Depends on:** F20.W01  
**Input:** F20.W01 and decisions D03/D05.  
**Deliverable:** Terraform design, roles, network, storage, queues, limits, teardown plan.  
**Acceptance F20.AC02:** Resources, minimum permissions, maximum spend/replicas/runtime, secrets, and rollback steps are reviewable; Actions is absent.  
**Verification:** Run local validation/static review; do not provision or spend until explicit user authorization.

### F20.W03

**Rehearse authorized deployment and restore**  
**Depends on:** F20.W02  
**Input:** F20.W02 and explicit deployment authorization.  
**Deliverable:** Deployment/rollback/restore record and measured cost.  
**Acceptance F20.AC03:** Fresh deployment, health, trace continuity, configuration rollback, backup restoration, and teardown succeed under agreed budget.  
**Verification:** Execute only after authorization; report actual recovery time/cost and leave this unit blocked beforehand.

## F21

**Capacity and cost experiments**  
**Roadmap phase:** 6; large runs gated  
**Feature outcome:** Before/after targeted tuning report and capacity model.  
**Implementation status at baseline:** Planned.

### F21.W01

**Build an honest load harness**  
**Depends on:** F13.W03, F18.W03  
**Input:** Run manifests and measured baseline.  
**Deliverable:** Open-loop workload driver and corpus taxonomy.  
**Acceptance F21.AC01:** Reports distinguish documents/versions/chunks/vectors and real/synthetic data; errors, timeouts, queueing, and dropped work are counted.  
**Verification:** Verify offered load remains independent of server slowdown; test cold/warm and mixed-ingestion scenarios locally.

### F21.W02

**Execute the capacity ladder**  
**Depends on:** F21.W01, F20.W03  
**Input:** F21.W01, F20.W03 for cloud, and budget D05.  
**Deliverable:** Measured runs at declared corpus/load sizes.  
**Acceptance F21.AC02:** Use at least 30 steady minutes after warm-up with repeated query orders; offered 1/5/10/25 RPS are experiments, not promises; stop at caps.  
**Verification:** Record all failures and largest completed run; cloud stages remain blocked without authorization and budget.

### F21.W03

**Explain bottlenecks and ten-million projection**  
**Depends on:** F21.W02  
**Input:** F21.W02.  
**Deliverable:** Before/after targeted tuning report and capacity model.  
**Acceptance F21.AC03:** Projection includes measured chunk distribution, replicas, rebuild headroom, indexing/ANN overhead, memory versus disk, and cost; synthetic quality is not claimed.  
**Verification:** Re-run quality after ANN/vector changes; compare two authorized profiles and link every extrapolation to assumptions.

## F22

**Recovery and failure drills**  
**Roadmap phase:** 7  
**Feature outcome:** Runbooks and incident narratives.  
**Implementation status at baseline:** Planned.

### F22.W01

**Exercise ingestion and provider failures**  
**Depends on:** F18.W03, F19.W03, F21.W01  
**Input:** Failure taxonomy and bounded workload.  
**Deliverable:** Local disposable fault scenarios.  
**Acceptance F22.AC01:** Worker death, poison data, source timeout, model throttling, and queue pressure have bounded retries and visible outcomes; committed work is not lost.  
**Verification:** Run each injection and reconcile jobs, eligibility, latency, and recovery evidence.

### F22.W02

**Exercise search, index, and storage recovery**  
**Depends on:** F22.W01, F20.W03  
**Input:** F22.W01 and F20.W03 for cloud drills.  
**Deliverable:** Search interruption, failed rollout, backup restore, and exclusion drill records.  
**Acceptance F22.AC02:** Incomplete/revoked evidence never silently releases; degraded modes are explicit; restore integrity is verified.  
**Verification:** Measure recovery against predeclared objectives; cloud faults require authorized disposable environments.

### F22.W03

**Write incident and SLO reviews**  
**Depends on:** F22.W02  
**Input:** F22.W02.  
**Deliverable:** Runbooks and incident narratives.  
**Acceptance F22.AC03:** Each scenario has detection, diagnosis, mitigation, measured recovery, residual risk, and a justified follow-up.  
**Verification:** A fresh operator follows a runbook using the recorded scenario; no unobserved availability claim is made.

## F23

**Frontend release quality and discoverability**  
**Roadmap phase:** 5–8; publication gated  
**Feature outcome:** HTTPS, performance, indexing and Search Console evidence; backlink strategy draft.  
**Implementation status at baseline:** Planned.

### F23.W01

**Validate responsive and accessible UX**  
**Depends on:** F12.W03, F17.W03  
**Input:** Practitioner screens and content states.  
**Deliverable:** Keyboard/mobile/accessibility check record.  
**Acceptance F23.AC01:** Focus, labels, contrast, error/loading states, and navigation meet declared WCAG 2.2 AA scope; informative images have meaningful alt text.  
**Verification:** Test representative mobile/desktop sizes and keyboard flows; document manual and automated coverage.

### F23.W02

**Prepare public-page metadata and links**  
**Depends on:** F23.W01  
**Input:** F23.W01.  
**Deliverable:** Framework-backed sitemap, robots, canonical/meta/OG/schema configuration.  
**Acceptance F23.AC02:** Only intended public pages are indexable; private/staging pages remain restricted; one H1/logical hierarchy, valid slugs/internal links, accurate schema, and optimized images apply.  
**Verification:** Inspect generated pages and routes locally; check broken links, indexing boundaries, mobile layout, and performance budget.

### F23.W03

**Validate the authorized public release**  
**Depends on:** F23.W02  
**Input:** F23.W02 and explicit publication/domain authorization.  
**Deliverable:** HTTPS, performance, indexing and Search Console evidence; backlink strategy draft.  
**Acceptance F23.AC03:** HTTPS and public metadata are verified on the authorized domain; Core Web Vitals use measured data; noindex is never removed globally; outreach is not automatic.  
**Verification:** Run release review only when authorized; field data and Search Console remain not-run until available, and no messages are sent without permission.

## F24

**Reproducibility and portfolio evidence**  
**Roadmap phase:** 8  
**Feature outcome:** Practitioner demo, engineering walkthrough, release notes, and LinkedIn drafts.  
**Implementation status at baseline:** Planned.

### F24.W01

**Rehearse a fresh-clone demonstration**  
**Depends on:** F16.W03, F12.W03  
**Input:** Accepted local features and redistributable fixtures.  
**Deliverable:** README/setup, example config, and reproducible local demo.  
**Acceptance F24.AC01:** A fresh clone reaches a supported brief and correct abstention using documented commands; fixture/model licenses and resource needs are explicit.  
**Verification:** Execute the rehearsal without private paths or developer-only state; record failures and setup time.

### F24.W02

**Prepare engineering case studies**  
**Depends on:** F24.W01  
**Input:** F24.W01; scale/recovery reports when completed.  
**Deliverable:** Retrieval, verification, and operations narratives with evidence links.  
**Acceptance F24.AC02:** Every headline metric names run, corpus size, workload, hardware, model/config, date, and limitations; absent cloud results are labelled planned.  
**Verification:** Trace each published claim back to raw results; include failed experiments and tradeoffs.

### F24.W03

**Package reviewable presentation assets**  
**Depends on:** F24.W02  
**Input:** F24.W02.  
**Deliverable:** Practitioner demo, engineering walkthrough, release notes, and LinkedIn drafts.  
**Acceptance F24.AC03:** Reviewer can follow behavior → requirement → work unit → implementation → verification; no claim of ten-million-doc execution or clinical validation without evidence.  
**Verification:** Perform a link/license/claim review; posting and public deployment remain separately authorized actions.

## Decision register

Decisions are owned initially by the project owner, with domain/engineering review as indicated. A resolved decision is issued in a child edition targeting its D-ID; do not edit this register. None of the following is silently presumed answered.

- **D01 — Initial scope:** confirm supplement topics, question language, and practitioner workflow priorities before F01.W03. Current proposal: four topics and English-first.
- **D02 — Source admission:** choose actual source allowlist, permitted acquisition routes, license/redistribution basis, and reference-following policy before F03.W01/F05. ODS/eligible PMC content are candidates, not blanket permission.
- **D03 — Model access and data handling:** select permitted providers/local modes, outbound data policy, retention, and credential setup before any real inference call. Fixture/stub development can proceed without external calls.
- **D04 — Parser/embedding/reranker selections:** benchmark maintained candidates, pin revisions, and record hardware/license/compatibility before production use in F06/F09/F13. No model choice is accepted solely for domain branding.
- **D05 — Cloud authority and spend:** choose region/services, permitted resource limits, hard runtime/spend caps, and explicit deployment authorization before F20.W03 or paid scale/failure experiments. No budget currently exists.
- **D06 — Quality thresholds:** ratify G02/G03 and critical slice tolerances with development evidence before F16.W02 locks the holdout. Any later change needs a new edition and a new prospective evaluation decision.
- **D07 — Retention and privacy:** define permitted source/derived-artifact retention, log/feedback retention, deletion handling, and public/private boundaries before real acquisition and feedback storage.
- **D08 — Resource and recovery budgets:** measure local profile, choose model quotas, set per-stage budgets and recovery objectives before accepting performance/recovery results. Cloud targets remain proposals until an authorized profile exists.
- **D09 — Review capacity:** identify practitioner review availability, annotation/adjudication process, and any independent security review before claims based on those activities. If unavailable, proceed only with accurately labelled engineering evidence.

## Dependency and scope risks

Source rights/coverage may restrict the corpus; record gaps instead of padding it. Parsing can lose critical numbers and qualifiers; uncertain extraction is quarantined. Hosted-provider latency/quotas may dominate; record them as system constraints. Labels may be incomplete or expensive; report uncertainty and review coverage. Index generations, caches, and rollback can resurrect stale evidence; current exclusion checks are a release invariant. Broad feature scope may exceed initial estimates; split work through child editions, not speculative service proliferation.

A deferred cloud or publication unit is not permission to spend or publish. Optional graph traversal, fine-tuning, contextual embeddings, multimodal retrieval, semantic caching, and alternate vector backends require a new child edition motivated by observed error/cost classes. They are not hidden obligations in this baseline.

## Traceability and review contract

Every implementation child names its root master version, immediate parent edition, affected F/W/AC/P/G/D IDs, scope, rationale, before/after intent, dependency changes, migration/rollback impacts, and verification obligations. Additions receive new IDs; replacements identify prior IDs; retirement preserves tombstones and rationale. No child may silently discard inherited requirements.

Every verification record maps work-unit and acceptance IDs to commands or reviewed observations, pass/fail/not-run outcomes, versioned evidence, and limitations. The baseline status stays Planned forever as a historical snapshot; current completion belongs in execution records. Future estimates, scope changes, threshold decisions, and feature refinements belong in children. Read [the edition procedure](README.md) for sealing, lineage resolution, and local integrity checks.

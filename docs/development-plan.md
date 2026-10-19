# EvidenceLens phased development plan

Draft dated 19 October 2026. The project progresses through useful releases, with evaluation gates before larger infrastructure commitments. Estimates are planning ranges for one engineer, not delivery promises. Practitioner review, access constraints, and cloud provisioning may extend elapsed time.

The core portfolio release comprises Phases 0–5, approximately 28–43 focused engineering days. Phases 6–8 add approximately 19–31 days. The complete proposal is therefore 47–74 focused days before optional research extensions. At two to three focused days each week, plan roughly four to nine months, plus interruptions and external review. Re-estimate after Phase 2 using actual progress.

## Delivery workflow for every phase

All phases use the [Spec Kit + ECC workflow](agent-tooling.md), with feature scope and status tracked in the [feature index](../specs/README.md). Create focused specifications when each slice is ready, research reuse through ECC during planning, and require applicable verification before convergence. This applies throughout ingestion, RAG, practitioner UI, security, deployment, scaling, and operations. Roadmap phases are planning context; canonical feature tasks live under specs/.

## Phase 0 — Define the evidence contract

**Estimate: 2–3 days. Dependency: none.**

Agree the practitioner workflows, seed topics, source policy, and output schema. Draft 30 realistic questions spanning direct lookup, study comparison, public-claim verification, and absent evidence. Record what a useful answer must contain and what it must not infer. Collect roughly 100 eligible source documents with a deliberate mix of research and commentary; do not pad the sample just to reach a count.

Decide the available cloud spend, permitted model providers, data retention policy, and practitioner review availability. The current default is public material and AWS as the reference cloud. Select sources by evidence coverage and acquisition feasibility, not only fame.

**Deliverables:** product brief, source registry, evidence schema, initial annotation guide, corpus manifest, and architecture decision records covering scope and the proposed search backend.

**Exit gate:** every seed document has provenance and a collection/reuse decision; every seed question has an expected answerability label and evidence requirements. If practitioner review is unavailable, document that constraint and proceed with engineering evaluation without claiming clinical validation.

**Portfolio evidence:** explain how a domain workflow becomes a testable system contract.

## Phase 1 — Build the ingestion foundation

**Estimate: 5–7 days. Dependency: Phase 0.**

Implement source connectors, immutable snapshots, parser adapters, document versions, provenance spans, deterministic IDs, structured chunk manifests, and a durable job ledger. Start with permitted structured research content and HTML. Add a PDF fixture set containing tables, multi-column text, and scans to establish parser limitations early.

Implement exact deduplication, candidate near-duplicate links, retry budgets, worker leases, quarantine, and an outbox. Build a small operator view or CLI showing discovered, parsed, quarantined, embedded, and published counts. Document deletion and replacement events from the beginning.

**Deliverables:** replayable ingestion command, parser fixtures, provenance inspector, corpus manifest, and a failure-recovery demonstration.

**Exit gate:** replaying a completed batch creates no duplicate published chunks; interrupting and restarting a worker resumes correctly; malformed files enter quarantine; manually sampled citations resolve to the intended source passages. No document becomes searchable before its version is complete.

**Portfolio evidence:** replay the same batch, kill a worker, and show stable IDs and accounting after recovery.

## Phase 2 — Deliver a complete baseline

**Estimate: 4–6 days. Dependency: Phase 1.**

Implement the API, a minimal practitioner interface, BM25-only and vector-only retrieval profiles, structured answer generation, deterministic citation-ID validation, and explicit evidence-gap responses. Add source and passage inspection before visual polish.

Use approximately 500–2,000 eligible documents if the selected domain provides them. This is an acquisition target, not a reason to include irrelevant documents. Record baseline timing and costs and expand the development questions to 200. Freeze a separate evaluation design before optimization.

**Deliverables:** first usable evidence brief, reproducible baseline configuration, trace viewer, error taxonomy, and a short demonstration recording.

**Exit gate:** a clean environment can reproduce ingestion and answering on the licensed fixture corpus; all displayed citations resolve; raw evaluation outputs and failures are stored with corpus/model/config versions. Baseline shortcomings remain visible rather than being selectively omitted.

**Portfolio evidence:** show an actual failure and identify whether parsing, retrieval, context selection, or generation caused it.

## Phase 3 — Optimize retrieval with controlled experiments

**Estimate: 6–10 days. Dependency: Phase 2.**

Add hybrid retrieval, fusion, reranking, section-aware child/parent chunks, study-level deduplication, and alias normalization. Compare a general embedding model with a biomedical candidate using the same corpus and evaluation queries. Keep the generator fixed during retrieval comparisons.

Run an experiment ladder: BM25 versus dense; best single retrieval versus hybrid; hybrid versus hybrid plus reranking; fixed windows versus structure-aware chunks; then context diversity and parent expansion. Change one major factor at a time, and evaluate the final combined configuration separately because improvements may not add together.

Test numeric terms, ingredient aliases, formulation differences, and conflicting findings. Expand to approximately 5,000–20,000 relevant documents only as coverage justifies it. Record both the number of documents and the actual chunk count.

**Deliverables:** retrieval benchmark report, paired-query error analysis, selected pipeline configuration, and a decision record explaining each retained optimization.

**Exit gate:** the selected configuration improves the intended development metrics without an unacceptable regression in critical slices or operational budgets. Publish changes with uncertainty and failed experiments; an ineffective technique is removed or remains experimental.

**Portfolio evidence:** demonstrate why the retained pipeline is better than its baseline and what each improvement costs.

## Phase 4 — Add claim checks and calibrated abstention

**Estimate: 6–10 days. Dependency: Phase 3.**

Implement evidence sufficiency checks, claim-level citation support, numeric and unit validation, contradiction handling, bounded follow-up retrieval, and partial answers. Build the creator-claim audit workflow on top of the same pipeline. Link multiple publications to study records conservatively.

Create the locked test set described in the evaluation specification. Calibrate answer-release thresholds using development data only. Compare reliability against useful answer coverage; distinguish abstention caused by weak evidence from abstention caused by infrastructure failure. Sample automated verifier judgments for human review.

**Deliverables:** risk-versus-coverage report, verified brief schema, adversarial suite, citation checks, and a documented release policy.

**Exit gate:** meet the agreed evaluation gates on the locked test release, or publish the gap and keep the system in an explicitly limited release. No fabricated source ID is released, and no critical numeric/population error is accepted in the fixed safety fixtures. Those finite checks do not establish a universal zero-error guarantee.

**Portfolio evidence:** show a supported answer, a qualified disagreement, and a correct refusal with missing evidence explained.

## Phase 5 — Deploy a reproducible cloud pilot

**Estimate: 5–7 days. Dependency: Phase 4; infrastructure prototypes can begin after Phase 2.**

Package container images, Terraform, separate API and worker roles, S3 storage, RDS, OpenSearch, and SQS adapters. Add managed secrets, authentication, rate limits, telemetry, billing tags, budgets, and a teardown procedure. Pin versions and verify local ARM64 and cloud image compatibility. CI/CD is deferred; GitHub Actions must not be introduced without the user's explicit instruction, even when this phase is reached. This future deployment phase is not authorization to deploy during current development.

Implement exact-query caching with index/policy version keys. Demonstrate a source replacement and cache invalidation. Configure private networking for stateful services and least-privilege access. Establish the first cloud workload and test profile; validate throughput before enabling aggressive autoscaling.

**Deliverables:** cloud pilot, infrastructure code, deployment/rollback runbook, restore record, and operating-cost breakdown.

**Exit gate:** a clean deployment succeeds; configuration rollback works; request traces cross service boundaries; secrets are absent from source and logs; deleted or ineligible evidence disappears from live responses and cached answers; backups restore successfully. Report achieved recovery time.

**Portfolio evidence:** demonstrate the same evidence contract locally and in the cloud, including the changed deployment adapters.

## Phase 6 — Measure scale and bottlenecks

**Estimate: 7–12 days. Dependency: Phase 5 and an agreed experiment budget.**

Run the capacity ladder in the scaling document: real domain corpus, broader permitted research distractors, then explicitly synthetic systems workloads if needed. Keep the evidence-quality corpus and systems capacity corpus distinguishable in every report.

Sweep ANN parameters, candidate counts, reranker batch sizes, vector representations, ingestion batch sizes, cache settings, and worker counts. Test 1, 5, 10, and 25 query requests per second as offered loads and record where latency or error targets fail. These are experiments, not promised supported rates.

Measure index build/rebuild duration, memory, disk, source and model rate limits, queue recovery, saturation, and cost. Compare at least two deployment sizes. Profile the critical path before adding infrastructure.

**Deliverables:** reproducible load harness, dataset manifests, machine specifications, raw measurements, capacity curves, and a revised ten-million-document model.

**Exit gate:** another engineer can rerun a declared scenario and obtain comparable results; the largest actual test is clearly stated; every projected capacity number identifies assumptions. Do not claim a ten-million-document benchmark unless that benchmark was actually run.

**Portfolio evidence:** show where the system saturates and why, then demonstrate the improvement from one targeted change.

## Phase 7 — Exercise operational failures

**Estimate: 7–12 days. Dependency: Phase 6.**

Test worker termination, poison documents, source timeouts, model throttling, search-node interruption, full queues, and index-release failures in a disposable staging deployment. Add alert thresholds based on observed behavior, dependency timeouts, circuit breakers, bounded retries, and explicit degraded modes.

Exercise index rebuild and alias rollback, retraction/deletion propagation, and recovery from backups. Test cold caches, mixed ingestion/query traffic, skewed popular queries, and unavailable reranking. Tighten security tests for prompt injection and URL ingestion.

**Deliverables:** incident write-ups, runbooks, recovery timings, availability measurements, and a service-level objective review.

**Exit gate:** all declared failure scenarios have an observed and explainable outcome; no silent release of incomplete or revoked evidence occurs; recovery and freshness objectives are met or revised with evidence.

**Portfolio evidence:** a short operational incident narrative showing detection, diagnosis, mitigation, and prevention.

## Phase 8 — Publish the engineering case study

**Estimate: 5–7 days. Dependency: a stable release from Phases 5–7.**

Prepare a clean repository with an accurate README, architecture diagrams, setup instructions, permitted sample corpus, source acquisition manifest, test commands, evaluation datasets, reproducible benchmark configuration, raw-result links, and model/source limitations. Add a five-minute practitioner demo and a separate engineering walkthrough.

Write three case studies: retrieval optimization; evidence verification and abstention; cloud scaling and failure recovery. Every headline metric links to a run manifest and states corpus size, workload, hardware, model, and date. Include failed experiments and residual risks.

**Deliverables:** release candidate, portfolio narrative, interview walkthrough, and draft LinkedIn posts. Publishing or posting is a later action; this phase defines the assets.

**Exit gate:** a fresh-clone rehearsal succeeds, source redistribution has been checked, results are reproducible, and the public claims match measured evidence.

**Portfolio evidence:** a reviewer can trace a product behavior to architecture, code, test evidence, and an operational tradeoff.

## Optional extensions after the core system

Choose extensions by observed failure class. Do not implement all of them merely to increase the technology count.

- **Citation-graph traversal:** useful when questions need evidence several reference links away; compare it with bounded query decomposition before adopting a graph database.
- **Fine-tuned reranker:** appropriate after collecting sufficient human relevance judgments; split training and testing by study/topic family to avoid leakage.
- **Contextual embeddings:** evaluate when section headings or missing document context repeatedly cause retrieval failures; include preprocessing cost and the risk of generated context introducing errors.
- **Multimodal retrieval:** consider when information in figures or tables remains inaccessible after parsing; require evidence-region citations and a new evaluation slice.
- **Semantic caching:** consider only after exact caching is measured; validate dose, formulation, and population mismatches rigorously.
- **Alternate vector backend:** compare Qdrant or another engine when a measured search bottleneck justifies the operational cost.

## Repository structure to create during implementation

The current repository contains planning files only. The proposed implementation adds `apps/api`, `apps/web`, `workers/ingestion`, `packages/evidence`, `packages/retrieval`, `packages/generation`, `packages/evaluation`, `infra/compose`, `infra/terraform`, `tests`, `benchmarks`, and `data/manifests`. Keep source bytes and large generated indexes out of Git; include only fixtures whose licenses permit redistribution.

Create one architecture decision record for each consequential choice. Record context, options, chosen approach, measured evidence, consequences, and the condition that would reopen the decision. New tools must solve a documented need.

## First implementation iteration

Begin with one complete path: acquire one permitted document, create a versioned source snapshot, extract a cited passage, index it, answer one practitioner question, resolve its citation, and replay the ingestion without duplication. Alongside it, capture the 30 seed questions and source registry. This exposes the evidence-contract mistakes before infrastructure or UI work makes them expensive to change.

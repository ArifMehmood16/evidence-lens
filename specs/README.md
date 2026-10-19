# Feature index

All substantial work uses the shared [Spec Kit + ECC lifecycle](../docs/agent-tooling.md). The [original master](../docs/planning/master-plan-v1.0.0.md) now defines all 24 application features and 72 work units, with acceptance criteria and dependencies. Read accepted [child editions](../docs/planning/README.md) to resolve current intent. This index is navigation, not a second task list.

## Current feature

- [001 — Development workflow](001-development-workflow/spec.md): repository-wide Spec Kit/ECC integration. See its [verification](001-development-workflow/verification.md) for actual checks and limitations.

## Application coverage

The application capabilities below remain planned. Their canonical breakdown is in the master. Create focused implementation specs as child elaborations with original F/W/AC references; do not duplicate the whole master or rewrite sealed intent. Detailed library/API choices remain just-in-time decisions with explicit readiness gates.

- **Phase 0, evidence contract:** source admission, provenance, evidence schema, quality labels, corpus permissions, evaluation rubric. ECC research examines source/data and schema tooling; verification checks fixtures and evidence invariants.
- **Phase 1, ingestion:** connectors, parsing/OCR, deduplication, versions, idempotency, retry/recovery, deletion. Research parser/queue/storage libraries; verify replay, partial failure, and provenance.
- **Phase 2, practitioner baseline:** retrieval, answer API, citations, abstention, minimal UI. Research search/model/API/UI capabilities; verify an end-to-end evidence brief and source inspection.
- **Phase 3, retrieval experiments:** hybrid search, reranking, chunking, filtering, query strategies. Research existing capabilities; verify ablations with fixed datasets and cost/latency/quality comparisons.
- **Phase 4, grounded release:** claim checks, disagreement, calibrated abstention, adversarial evaluation. Research evaluators; verify on held-out data with reviewer calibration.
- **Phase 5, cloud deployment:** authentication, secrets, infrastructure, observability, reproducibility, frontend release. Research managed services/framework features; verify deployment, authorization, restore/rollback, and applicable SEO/accessibility.
- **Phase 6, scaling:** distributed ingestion, indexing, load generation, capacity and cost. Research scaling controls; verify measured throughput, tail latency, memory, and workload assumptions.
- **Phase 7, operations:** stale evidence, outages, backpressure, cache invalidation, index rollout, deletion propagation. Research failure-handling capabilities; verify fault injection and recovery.
- **Phase 8, case study:** reproducible experiments, diagrams, public documentation, demo. Research publishing tooling as needed; verify reproducibility, licensing, claims, and public-page checks.

Cross-cutting security, privacy, reliability, and frontend requirements belong in each affected feature. New substantial work follows this process even if it is not yet named in the roadmap.

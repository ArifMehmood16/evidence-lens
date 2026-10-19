---
name: rag-change-evaluation
description: Evaluate EvidenceLens retrieval, chunking, model, prompt, index, or answer-release changes against a versioned baseline. Use when evidence quality or provenance can change.
license: Apache-2.0
---

# Evaluate a RAG change

Read ../../../docs/evaluation.md and the relevant architecture contract. Use the existing harness when available; do not create a new evaluation framework for every change.

1. State the failure class or hypothesis and the affected stage. Identify the baseline, corpus manifest, question split, model revisions, and config hashes.
2. Select development examples and important slices: absent evidence, conflicting findings, repeated study coverage, numeric/unit qualifiers, source updates, and population/formulation mismatch as relevant.
3. Keep unrelated factors fixed. Compare retrieval relevance, citation support, useful answer coverage, latency, and cost according to the change. ANN approximation recall is not the same as domain relevance.
4. Inspect representative failures and human/judge disagreements. Preserve evidence locators and distinguish unsupported content from a source's own uncertain claim.
5. Tune on development data. Use the locked set for a release decision; if its failures inform tuning, disclose that and prepare a fresh holdout.
6. Report denominators, uncertainty where justified, regressions, and operational costs. No near-zero-hallucination or ten-million-document claim without the corresponding evidence.
7. Version the chosen configuration and document rollback, source exclusions, and cache invalidation when affected.

If no harness or labels exist yet, document the missing evidence and implement only the scoped prerequisite. Do not invent benchmark results or declare the quality gate passed.

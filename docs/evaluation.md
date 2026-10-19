# EvidenceLens evaluation specification

Draft dated 19 October 2026. All thresholds below are proposed release gates, not achieved results. Freeze the agreed gates after baseline characterization and before running the locked test; never lower them retrospectively to make a release appear successful.

## What reliability means

Evaluate retrieval relevance, evidence sufficiency, answer correctness, citation support, useful answer coverage, and operational reliability separately. An answer can be faithful to a poor source yet clinically misleading; a plausible answer can be unsupported by its citations. Source appraisal and domain review remain distinct from text entailment.

Citation evaluation should measure both whether a citation supports a claim and whether claims requiring support have citations. ALCE provides a research basis for separating correctness and citation quality; adapt its concepts to practitioner questions rather than treating an automated score as clinical validation. [ALCE](https://aclanthology.org/2023.emnlp-main.398/)

## Dataset and annotation design

Start with 30 seed questions and build 200 development questions. Add a separately locked 400-question test release: approximately 150 direct evidence questions, 80 comparison or multi-source questions, 60 conflicting-evidence questions, 60 genuinely unanswerable questions, and 50 robustness cases. These counts describe intended coverage, not collected data.

For each item, store the question, task category, corpus snapshot, answerability, acceptable evidence spans, relevant document/study IDs, required qualifiers, prohibited inferences, and reviewer rationale. Include both answerable and unanswerable robustness cases. Record disagreements and adjudication, and identify which labels received practitioner review.

Split related questions and study families across development and test partitions to prevent near-duplicate leakage. The retrieval corpus may contain the evidence needed for test answers; the locked information is the test question set, labels, and expected answers. Keep future time-based updates as an additional holdout slice. Model-generated questions are candidates until reviewed; do not use a model's own outputs as unquestioned ground truth.

Pool candidate evidence from several retrievers for relevance judging so the benchmark does not favor whichever retriever supplied the first annotations. Mark incomplete relevance judgments. Query families, sources, and extraction difficulties should be represented, not only easy FAQs.

Use development data for tuning. Open the locked test for a release decision, record the result, and create a fresh holdout if test failures guide further tuning. Repeatedly inspecting a test set turns it into development data.

## Metrics and initial gates

- **Evidence Recall@20:** fraction of labelled relevant evidence units represented in the first 20 results, macro-averaged over answerable questions. Proposed overall target: at least 0.90. Report study-level and passage-level versions separately, plus important slices. When relevance labels are incomplete, state that the measure covers annotated evidence.
- **nDCG@10:** ranked relevance with graded human judgments. Compare paired queries against the strongest single-retriever baseline. Do not claim that a tiny aggregate change improves every workflow.
- **Citation correctness:** fraction of cited claim–evidence links judged to support their associated claim. Proposed target: at least 0.95.
- **Citation completeness:** fraction of externally checkable factual claims with adequate supporting citations. Proposed target: at least 0.95. Invalid or merely topical citations do not count as support.
- **Unsupported claim rate:** unsupported factual claims divided by all factual claims released, including partially answered responses. Proposed target: at most 0.02. Also report the proportion of answers containing at least one unsupported claim so verbose answers cannot obscure failures.
- **Useful answer coverage:** fraction of gold-answerable questions receiving a sufficiently complete, correct answer under the annotation rubric. Proposed target: at least 0.70 while meeting the unsupported-claim target. A partial answer has separately scored coverage and does not automatically count as complete.
- **Correct abstention:** at least 0.90 of gold-unanswerable questions receive an appropriate evidence-gap response. Report false abstention on answerable questions and false answers on unanswerable questions. Infrastructure errors count separately.
- **Critical error fixtures:** zero invented citations and zero accepted critical dose/unit/population substitutions in the fixed release suite. This is a finite-suite gate, not a population error-rate guarantee.

Report sample sizes, denominators, and 95% confidence intervals. Use question-clustered bootstrap intervals for claim metrics and paired retrieval comparisons so correlated claims in one answer are not treated as independent observations. Present a risk-versus-coverage curve as the abstention threshold varies. A point estimate meeting a threshold with wide uncertainty should be described as preliminary.

Initially calibrate the release policy by sweeping sufficiency and verification thresholds on development examples and examining held-out development folds. If sufficient labels support a learned error predictor, compare a simple logistic model with isotonic calibration using out-of-fold predictions, then report reliability plots and Brier score on untouched data. Do not label a raw retrieval, reranker, or self-reported LLM score as a calibrated probability. Keep source-quality judgments visible rather than folding them into an unexplained percentage.

## Automated and human evaluation

Use deterministic checks for IDs, source-version existence, exact numeric values, schema validity, and citation locators. Use an independently evaluated judge/entailment model for support and sufficiency. Compare its decisions with human annotations on a stratified sample including errors; report disagreement rates and known weaknesses.

Where possible, use practitioner review for applicability, interpretation, and potential critical errors. Automated judges can screen large volumes but cannot establish source quality or clinical validity by themselves. Review all suspected critical errors and a random sample of passing answers.

## Controlled experiment ladder

1. BM25 and dense retrieval baselines with identical corpus snapshots.
2. Hybrid fusion, holding embedding and chunking fixed.
3. Reranking, holding first-stage retrieval fixed.
4. Chunking and parent expansion with an identical question set.
5. Evidence diversity and study deduplication.
6. Sufficiency checks and claim verification, with the generator held fixed where possible.
7. ANN tuning and quantization, comparing both nearest-neighbor approximation recall and domain evidence relevance.
8. Exact caching and batching under equivalent warm/cold workloads.

Every run stores a config hash, code revision, corpus manifest, random seed where applicable, model revisions, machine profile, raw outputs, stage timings, usage, and billing assumptions. Measure quality, p50/p95/p99 latency, throughput, memory, and cost. Select a quality/cost/latency tradeoff, not just the best accuracy number.

## Adversarial and operational cases

Include a plausible question whose answer is absent; irrelevant but high-similarity passages; conflicting findings; repeated articles about one study; old and replaced source versions; a retracted source; a table with units only in its header; OCR-corrupted numbers; different formulations; adult versus child populations; ingredient aliases; fabricated citations; and instructions embedded in retrieved pages.

Operational tests include duplicate queue delivery, worker death after a write but before acknowledgement, failed partial indexing, model throttling, reranker failure, cold-cache spikes, search-node interruption, deletion during an active query, and rollback after a source becomes ineligible. Assertions focus on observable correctness and recovery, not internal implementation details.

## Proposed cloud pilot service objectives

For a declared cloud profile with up to 100,000 chunks and 5 offered query requests per second: propose p95 retrieval plus reranking within 1.5 seconds, p95 verified brief within 15 seconds, and fewer than 1% infrastructure errors during a 30-minute steady test. Use a fixed model, 8,000-token maximum evidence budget, and 500-token maximum generated brief for this profile. Include verification calls and queueing in end-to-end latency. The external provider must have enough request/token quota; otherwise the run measures provider throttling rather than backend capacity.

Measure concurrency as well as arrival rate. At 5 requests per second and a 15-second average residence time, roughly 75 requests would be in flight; p95 latency is not a valid substitute for the average in this calculation. Record actual concurrency, output lengths, retry count, and request abandonment.

Propose 99.5% monthly API availability for the deployed pilot and ingestion-to-search freshness within 24 hours of discovery for supported sources under normal load. These require ongoing measurement and are not established by a short load test. Define availability failures independently of correct evidence abstention. Freshness starts at discovery, not at an external publisher's publication time.

## Release record

Each release reports the largest measured corpus and workload; quality and coverage with intervals; reviewed error slices; source and model limitations; infrastructure and inference costs; observed recovery times; and known regressions. Keep engineering benchmarks, practitioner usefulness feedback, and clinical validation claims separate.

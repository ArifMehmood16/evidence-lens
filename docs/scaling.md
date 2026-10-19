# EvidenceLens scaling and cost model

Draft dated 19 October 2026. The ten-million-document scenario is a capacity model. Nothing in this document represents a completed benchmark.

## Units and workload assumptions

Track source records, full-text documents, document versions, chunks, vectors, tokens, and bytes separately. Ten million abstracts are a different workload from ten million long PDFs. Corpus growth and concurrent use are separate scaling axes.

For illustration, assume 20 chunks per document, one 768-dimensional vector per chunk, and float32 storage at four bytes per component. Raw vector bytes equal document count × chunks per document × dimensions × bytes per component × number of copies. A replication count of two means two total copies, not two replicas plus a primary.

Under these assumptions, 10,000 documents produce 200,000 chunks and 0.6144 GB of raw vectors. One million documents produce 20 million chunks and 61.44 GB. Ten million documents produce 200 million chunks and 614.4 GB; two copies require 1.2288 TB. These are decimal units. With a separate full rebuild generation and two copies per generation, raw vectors alone reach 2.4576 TB.

This excludes HNSW structures, inverted indexes, stored text, metadata, caches, segment merges, raw files, backups, and OS/runtime memory. Disk consumption and resident RAM are different metrics. Quantization might reduce one representation while original vectors remain available for rescoring; never equate the smaller representation with total system savings.

At an assumed average of 400 embedded tokens per chunk, the ten-million-document example requires 80 billion embedding input tokens. At an illustrative aggregate sustained 100,000 tokens per second, embedding alone takes about 9.26 days. That throughput is an assumption, not a hardware benchmark; acquisition, parsing, indexing, retries, and rate limits add time.

## Capacity ladder

**Local correctness profile:** begin with about 100 seed documents and grow to 500–2,000 eligible documents. Record actual chunk distributions and laptop memory peaks. Use a small reproducible fixture snapshot for fast tests.

**Domain quality profile:** target approximately 5,000–20,000 relevant documents if available. Preserve source diversity and relevance; do not claim an exact corpus size before acquisition. Establish quality metrics on real material.

**Cloud systems profile:** test 100,000, 1 million, and then 10 million chunks as budget permits. Use broader permitted biomedical material as clearly identified distractors. A ten-million-chunk test is not a ten-million-document test.

**Large design scenario:** model 10 million documents using measured chunk-size distributions and per-stage throughput. Running the full scenario is an optional, separately budgeted experiment. If synthetic or replicated records are used for load, label them; they cannot validate domain retrieval quality and repeated embeddings distort ANN behavior and caching.

## Benchmark method

For each corpus size, sweep 1, 5, 10, and 25 offered query requests per second, stopping or throttling when safety and spend limits are reached. Use open-loop arrival generation so a slowing server does not accidentally reduce offered load and hide latency. Report successes, errors, timeouts, queueing, concurrency, and dropped work.

Run at least a 30-minute steady interval after warm-up, repeat with multiple query orders, and include cold-cache and mixed-ingestion runs. Use realistic query popularity and document lengths, not only uniformly random short queries. Publish machine type, region, software versions, model quotas, dataset hashes, ANN settings, and cache state.

Measure ingestion documents/hour, chunks/hour, tokens/second, failure/retry rates, queue age, indexing lag, source update delay, index build time, and recovery time. Query metrics include p50/p95/p99 stage latency, useful answers/second, retrieval quality, abstention, and inference usage. Quality is re-evaluated after ANN or vector representation changes.

## When to change the architecture

- **OCR backlog grows:** scale OCR workers separately and route machine-readable sources around OCR. Investigate parser failures before adding workers.
- **Embedding queue dominates:** use token-aware batches, content/model caches, and a separate inference pool. Respect provider quotas and measure aggregate throughput.
- **Search memory or I/O saturates:** profile resident structures, tune ANN effort and supported vector representations, then change node size or shard layout. Re-run retrieval quality tests after each change.
- **Shard distribution is uneven:** inspect routing and document sizes. Avoid routing all queries or documents for a popular ingredient to one hot shard without a measured reason.
- **Reranking dominates latency:** reduce redundant candidates, batch requests, compare a smaller model, and evaluate adaptive candidate budgets. Keep critical slice quality visible.
- **Generation or verification dominates:** reduce irrelevant context, bound output size, batch independent checks, and compare models under the same release policy.
- **Query traffic competes with ingestion:** isolate CPU, memory, model quotas, and search/indexing resources. Apply backpressure rather than allowing an unbounded queue.
- **Availability requires redundancy:** deploy copies across failure domains and perform failure tests. Replicas provide resilience and read capacity, but not a cure for poor shard design.

## Cost accounting and spend controls

For each experiment, calculate acquisition/processing cost, embedding cost, search node-hours, database and storage costs, inference cost, observability cost, and data transfer. Report both variable cost per query and amortized total cost at the measured utilization.

Embedding API cost equals input tokens divided by the provider's pricing unit times the current rate. GPU cost equals billed runtime times the current rate, including idle/startup time. Query model cost includes generation, verification, retries, and follow-up retrieval calls. Record rate source and date when pricing is actually selected; no live price estimate is asserted here.

Before a large run, set a maximum experiment spend, maximum worker count, input document/token cap, runtime cap, and automatic teardown. Budget alerts alone are not a hard stop. Keep long-lived search/database charges visible even when the API scales down. Prefer temporary large capacity runs over an unnecessarily large always-on demo.

## What may be claimed publicly

Use wording such as “tested on X documents / Y chunks at Z requests per second on this deployment, with these quality and latency results.” Describe the ten-million-document architecture as a projection until actually tested. A larger systems corpus does not establish practitioner usefulness; a high-quality small corpus does not establish distributed capacity.

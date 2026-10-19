import { useState, useHostTheme, Stack, Row, Grid, H1, H2, H3, Text, Pill, Button, Table, Card, CardHeader, CardBody, Link, Divider } from "cursor/canvas";

const phases = [
  { id: "0", title: "Evidence contract", days: "2–3", work: "Practitioner workflows, source registry, 30 seed questions, 100 eligible source documents, and evidence schemas.", gate: "Every seed source has provenance and an acquisition decision. Every question has evidence requirements and an answerability label.", proof: "A domain workflow translated into a testable engineering contract." },
  { id: "1", title: "Ingestion foundation", days: "5–7", work: "Versioned source snapshots, parsing, chunk manifests, durable jobs, deterministic IDs, quarantine, and retries.", gate: "Replay produces no duplicate published chunks. Worker interruption recovers. Citations resolve to source spans.", proof: "A live replay and worker-recovery demonstration." },
  { id: "2", title: "Usable baseline", days: "4–6", work: "BM25 and dense baselines, API, practitioner interface, cited briefs, tracing, 200 development questions.", gate: "Clean-environment reproduction works. Citations resolve. Baseline failures and raw outputs are recorded.", proof: "A useful brief plus a diagnosed end-to-end failure." },
  { id: "3", title: "Retrieval optimization", days: "6–10", work: "Hybrid fusion, reranking, chunking comparisons, model comparisons, parent context, and study deduplication.", gate: "Retained changes demonstrate useful improvement within quality, latency, and cost budgets.", proof: "Controlled experiments and paired-query error analysis." },
  { id: "4", title: "Evidence verification", days: "6–10", work: "Claim checks, bounded follow-up retrieval, partial answers, abstention calibration, creator-claim audits, and locked evaluation.", gate: "Release gates are met or gaps are documented. Finite safety fixtures contain no accepted critical substitutions.", proof: "Risk versus useful answer coverage, including justified abstention." },
  { id: "5", title: "Cloud pilot", days: "5–7", work: "Container deployment, Terraform, S3/RDS/OpenSearch/SQS/ECS, authentication, exact caching, telemetry, budgets, and restore drills.", gate: "Deployment and rollback work. Deletion invalidates cached evidence. Backups restore. Recovery is timed.", proof: "The same evidence contract operating locally and in the cloud." },
  { id: "6", title: "Scale experiments", days: "7–12", work: "Capacity ladder, offered-load sweeps, ANN tuning, batching, cache profiles, resource and cost measurements.", gate: "Declared experiments are reproducible. The largest actual workload and all projections are clearly identified.", proof: "A measured bottleneck and the effect of a targeted optimization." },
  { id: "7", title: "Failure recovery", days: "7–12", work: "Worker/node failures, throttling, corrupt inputs, source changes, index migration, rollback, and degraded modes.", gate: "Each declared failure has an observed outcome and runbook. Recovery and freshness objectives are validated or revised.", proof: "Incident case studies with detection, mitigation, and prevention." },
  { id: "8", title: "Portfolio release", days: "5–7", work: "Fresh-clone rehearsal, licensed fixtures, benchmark manifests, architecture walkthrough, five-minute demo, and case studies.", gate: "Public claims match measurements and a reviewer can reproduce the release.", proof: "Retrieval, evidence verification, and scaling case studies." }
];

const stages = [
  ["Ingestion", "Source policy → immutable snapshots → parse/OCR → normalization → structure-aware chunks → batch embeddings → validated index generation", "Separate worker pools and replayable jobs; incomplete source versions never enter the answer context."],
  ["Query serving", "Interpret → BM25 + dense ANN → fuse → deduplicate → rerank → assemble evidence → assess sufficiency → generate → verify → release", "Bound candidate counts, context, retries, and model calls. Evidence gaps and partial answers are explicit results."],
  ["Evidence control", "Source registry + PostgreSQL provenance + object storage + index manifests + current exclusion policy", "Pin source/index versions and keep citation locators. Rollback cannot revive revoked evidence."],
  ["Measurement", "OpenTelemetry traces + labelled evaluation + load harness + cost ledger + recovery drills", "Quality, coverage, latency, resource use, and failure behavior remain independently visible."]
];

const checks = [
  ["Evidence Recall@20", "≥ 0.90", "Annotated relevant evidence; report passage and study levels."],
  ["Citation correctness", "≥ 0.95", "Cited claim–evidence links actually support the claim."],
  ["Citation completeness", "≥ 0.95", "Factual claims have adequate supporting citations."],
  ["Unsupported claims", "≤ 0.02", "Released factual claims; also report affected answers."],
  ["Useful answer coverage", "≥ 0.70", "Gold-answerable questions receiving a sufficiently complete correct answer."],
  ["Correct abstention", "≥ 0.90", "Gold-unanswerable questions receiving an evidence-gap response."],
  ["Pilot retrieval + reranking p95", "≤ 1.5 seconds", "Proposed cloud profile: 100k chunks, 5 offered requests/second."],
  ["Pilot verified brief p95", "≤ 15 seconds", "Same profile, 8k evidence-token budget and 500-token brief cap."]
];

export default function EvidenceLensPlan() {
  const theme = useHostTheme();
  const [tab, setTab] = useState("Architecture");
  const [phase, setPhase] = useState(0);
  const [docs, setDocs] = useState(1000000);
  const [chunks, setChunks] = useState(20);
  const [dims, setDims] = useState(768);
  const [bytes, setBytes] = useState(4);
  const [copies, setCopies] = useState(2);
  const [generations, setGenerations] = useState(1);
  const count = docs * chunks;
  const rawGB = count * dims * bytes * copies * generations / 1e9;
  const root = "https://github.com/ArifMehmood16/evidence-lens/blob/main";
  const number = (n: number) => n.toLocaleString("en-GB", { maximumFractionDigits: 3 });
  const controlStyle = { color: theme.text.primary, background: theme.bg.editor, border: `1px solid ${theme.stroke.secondary}`, borderRadius: 4, padding: 6, width: "100%", boxSizing: "border-box" as const };
  const fields = [
    { label: "Documents", value: docs, set: setDocs, max: 100000000 },
    { label: "Average chunks per document", value: chunks, set: setChunks, max: 1000 },
    { label: "Vector dimensions", value: dims, set: setDims, max: 8192 },
    { label: "Bytes per component", value: bytes, set: setBytes, max: 8 },
    { label: "Total copies per generation", value: copies, set: setCopies, max: 5 },
    { label: "Concurrent index generations", value: generations, set: setGenerations, max: 3 }
  ];
  return (
    <Stack gap={20} style={{ maxWidth: 1120, margin: "0 auto", padding: 24 }}>
      <Row justify="space-between" wrap>
        <Text size="small" tone="secondary">ENGINEERING PLAN · 19 OCTOBER 2026</Text>
        <Pill>Draft · no benchmarks run</Pill>
      </Row>
      <H1>EvidenceLens</H1>
      <Text style={{ maxWidth: 820 }}>Traceable supplement evidence for practitioners, with measurable retrieval quality and a tested path from local development to cloud scale.</Text>
      <Grid columns="repeat(auto-fit, minmax(190px, 1fr))" gap={20}>
        <Stack gap={4}><H3>Practitioner workflow</H3><Text tone="secondary">Investigate a question, audit a claim, and inspect disagreement.</Text></Stack>
        <Stack gap={4}><H3>Core release</H3><Text tone="secondary">Phases 0–5 · 28–43 focused engineering days, estimated.</Text></Stack>
        <Stack gap={4}><H3>Full portfolio</H3><Text tone="secondary">Phases 0–8 · 47–74 focused days, before optional extensions.</Text></Stack>
      </Grid>
      <Divider />
      <Row wrap gap={8}>{["Architecture", "Development phases", "Quality gates", "Scale calculator"].map(name => <Pill key={name} active={tab === name} onClick={() => setTab(name)}>{name}</Pill>)}</Row>

      {tab === "Architecture" && <Stack gap={20}>
        <H2>One evidence contract across two pipelines</H2>
        {stages.map(([name, flow, rationale]) => <Grid key={name} columns="minmax(110px, 1fr) minmax(0, 4fr)" gap={20}>
          <H3>{name}</H3><Stack gap={6}><Text weight="medium">{flow}</Text><Text tone="secondary">{rationale}</Text></Stack>
        </Grid>)}
        <Divider />
        <H2>Proposed deployment choices</H2>
        <Table headers={["Responsibility", "Initial choice", "Reason"]} rows={[
          ["API and domain contracts", "Python + FastAPI", "Explicit, typed pipeline orchestration."],
          ["Provenance and job state", "PostgreSQL", "Versioned evidence, manifests, durable workflow state."],
          ["Original material", "Object storage adapter → S3", "Immutable source snapshots and parser artifacts."],
          ["Lexical and vector retrieval", "OpenSearch", "One search backend before considering dual-store operations."],
          ["Work execution", "Local leased jobs → SQS workers", "Replayable, idempotent stages with independent resource pools."],
          ["Reference cloud", "AWS ECS, RDS, S3, OpenSearch, SQS", "Concrete deployment path; vendor remains a project choice."],
          ["Models", "Versioned provider adapters", "Select embedding, reranking, and generation models by evaluation."],
          ["Observability", "OpenTelemetry", "Trace retrieval, evidence decisions, latency, usage, and failures."]
        ]} />
        <Text size="small" tone="secondary">Architecture choices are proposals. Model selection, cloud budget, exact versions, and source allowlists are Phase 0–3 decisions.</Text>
        <Card><CardHeader>Source reputation is context, not a truth score</CardHeader><CardBody><Text>Accept verified research and credible commentary while retaining source type, provenance, original evidence links, applicability, disclosed interests, and limitations. Distinguish ten reports about one study from ten independent studies. No source list is approved merely by this plan.</Text></CardBody></Card>
        <Link href={`${root}/docs/architecture.md`}>Read the full architecture and evidence contracts</Link>
      </Stack>}

      {tab === "Development phases" && <Stack gap={20}>
        <H2>Build through demonstrable release gates</H2>
        <Row wrap gap={6}>{phases.map((p, i) => <Pill key={p.id} active={phase === i} onClick={() => setPhase(i)}>Phase {p.id}</Pill>)}</Row>
        <H3>Phase {phases[phase].id} · {phases[phase].title}</H3>
        <Text tone="secondary">Estimated effort: {phases[phase].days} focused days. {phase === 0 ? "Starting phase." : `Depends on Phase ${phase - 1}; see the full plan for limited overlap.`}</Text>
        <Text>{phases[phase].work}</Text>
        <Card><CardHeader>Exit gate</CardHeader><CardBody><Text>{phases[phase].gate}</Text></CardBody></Card>
        <Text><strong>Portfolio evidence:</strong> {phases[phase].proof}</Text>
        <Row><Button disabled={phase === 0} onClick={() => setPhase(phase - 1)}>Previous phase</Button><Button disabled={phase === phases.length - 1} onClick={() => setPhase(phase + 1)}>Next phase</Button></Row>
        <Divider />
        <Table headers={["Phase", "Deliverable", "Focused days"]} rows={phases.map(p => [p.id, p.title, p.days])} />
        <Text tone="secondary">At two to three focused days per week, the complete plan is roughly four to nine months plus external review and interruptions. Re-estimate after the baseline. Ten-million-document execution is a separately budgeted optional experiment.</Text>
        <Link href={`${root}/docs/development-plan.md`}>Read phase tasks, dependencies, deliverables, and extension criteria</Link>
      </Stack>}

      {tab === "Quality gates" && <Stack gap={20}>
        <H2>Reliability must preserve useful coverage</H2>
        <Text>All values below are proposed targets. Agree and freeze gates before the locked test. Report sample size, uncertainty, slice failures, and infrastructure errors separately from correct abstention.</Text>
        <Table headers={["Metric", "Proposed target", "Definition or workload"]} rows={checks} />
        <Text size="small" tone="secondary">These are not observed metrics. The pilot latency profile requires a declared deployment and adequate model quotas. See the full evaluation specification for denominators and limitations.</Text>
        <Grid columns="repeat(auto-fit, minmax(230px, 1fr))" gap={20}>
          <Stack gap={8}><H3>Development evidence</H3><Text>200 questions for tuning, with grouped study/topic families and reviewed evidence labels.</Text></Stack>
          <Stack gap={8}><H3>Locked release test</H3><Text>400 questions: direct, multi-source, conflicting, unanswerable, and robustness cases. Refresh the holdout if its failures inform further tuning.</Text></Stack>
          <Stack gap={8}><H3>Human review</H3><Text>Validate automated judgments with stratified human review. Practitioner appraisal remains separate from citation entailment.</Text></Stack>
        </Grid>
        <Text>Critical fixtures require no invented citations or accepted critical dose/unit/population substitutions. Passing a finite suite does not establish zero hallucination or clinical validation.</Text>
        <Link href={`${root}/docs/evaluation.md`}>Read the evaluation protocol and proposed service objectives</Link>
      </Stack>}

      {tab === "Scale calculator" && <Stack gap={20}>
        <H2>Raw vector storage under explicit assumptions</H2>
        <Text>Explore capacity arithmetic. This is a storage lower-bound component, not total index storage, RAM, a provider quote, or an achieved benchmark.</Text>
        <Row wrap>
          {[10000, 1000000, 10000000].map(n => <Button key={n} onClick={() => setDocs(n)}>{number(n)} documents</Button>)}
        </Row>
        <Grid columns="repeat(auto-fit, minmax(210px, 1fr))" gap={16}>
          {fields.map(f => <label key={f.label} style={{ display: "flex", flexDirection: "column", gap: 6, color: theme.text.secondary, fontSize: 13 }}>{f.label}<input aria-label={f.label} type="number" min={1} max={f.max} step={1} value={f.value} onChange={e => { const v = Number(e.target.value); if (Number.isFinite(v)) f.set(Math.max(1, Math.min(f.max, Math.round(v)))); }} style={controlStyle} /></label>)}
        </Grid>
        <div style={{ background: theme.fill.tertiary, padding: 20, borderRadius: 6 }}>
          <H2 style={{ color: theme.accent.primary }}>{number(rawGB)} GB of raw vectors</H2>
          <Text>{number(count)} chunks × {number(dims)} dimensions × {bytes} bytes × {copies} total copies × {generations} index generations</Text>
          <Text size="small" tone="secondary">Decimal GB. Source: user-adjustable design assumptions and arithmetic; no measurement period applies.</Text>
        </div>
        <Text>Excluded: ANN structures, lexical indexes, text, metadata, caches, raw files, backups, runtime memory, and temporary merges. A second index generation represents rebuild overlap. Quantized search may retain original vectors, so this calculator does not predict total quantization savings.</Text>
        <Table headers={["Milestone", "What it establishes"]} rows={[
          ["100 → 2,000 eligible documents", "Correctness, provenance, and repeatable local development."],
          ["5,000 → 20,000 relevant documents", "Domain evidence quality, subject to actual source availability."],
          ["100k → 1m → 10m chunks", "Cloud systems experiments as budget permits; distinct from document count."],
          ["10m documents", "Capacity scenario until a full, declared benchmark is actually executed."]
        ]} />
        <Link href={`${root}/docs/scaling.md`}>Read workload design, cost accounting, and scale triggers</Link>
      </Stack>}
      <Divider />
      <Text size="small" tone="secondary">EvidenceLens planning artifacts only. The repository documents contain the full rationale and primary-source references. This overview is stored inside the project as requested; rendering requires a compatible cursor/canvas host.</Text>
    </Stack>
  );
}

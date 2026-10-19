# Spec Kit + ECC across EvidenceLens

Spec Kit owns the feature lifecycle; ECC contributes reuse research and verification inside it. This applies across the whole application, including ingestion, retrieval, generation, APIs, practitioner UI, evaluations, infrastructure, security, and operations. There is one specification and task list per feature.

AGENTS.md is the entry point for all agents. The [master plan](planning/master-plan-v1.0.0.md) and accepted [child editions](planning/README.md) define application intent. The [constitution](../.specify/memory/constitution.md) routes shared governance; the sealed [engineering standards](engineering-standards.md) supply baseline detail. Official editor integrations use the same constitution and overrides. The [feature index](../specs/README.md) connects this workflow to the master catalogue.

## Daily workflow

For substantial work, begin with the local preflight and actual stage/host. Its --context option prints the relevant skill bodies into the session; then follow them and record observable application evidence as described below. This operational contract is specified in [child edition 0001](planning/editions/0001/edition.md).

1. **Specify:** resolve the accepted planning lineage, then use speckit-specify in a new draft feature directory. Capture outcome, acceptance, failures, verification, original master/parent links, and F/W/AC IDs in spec.md. Use speckit-clarify for material ambiguity. Never run a rewriting command on a sealed spec/plan; create a child edition first.
2. **Plan with ECC:** use speckit-plan and read .agents/skills/search-first/SKILL.md. Record reuse decisions, upstream sources, alternatives, licenses, and reasons for custom code in research.md. Plan.md consumes that research and defines actual interfaces, budgets, recovery, and checks.
3. **Tasks:** use speckit-tasks. Tasks trace to requirements and include applicable testing and verification. Use speckit-analyze before substantial implementation to catch inconsistent or missing requirements.
4. **Implement with ECC:** use speckit-implement for the scoped tasks. Read .agents/skills/verification-loop/SKILL.md and record commands, results, acceptance mappings, and limitations in verification.md. Apply rag-change-evaluation and frontend-release-review when relevant.
5. **Converge:** use speckit-converge after implementation. Inspect actual behavior and the verification report against spec, plan, tasks, and constitution. Missing work or evidence becomes appended tasks. Implement fixes, update evidence, and converge again.
6. **Review and release:** link the feature artifacts and evidence in the PR. Deployment, publication, and external actions remain subject to the user's authorized scope.

For Codex, invoke skills as `$speckit-specify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-implement`, and `$speckit-converge`. Claude Code and Cursor use their installed `/speckit-...` skills. Discovery can depend on the host version or opening a new session; explicitly reference the relevant SKILL.md if it is not listed.

The four canonical project skills remain under .agents/skills. Claude Code has thin, project-prefixed /evidencelens-search-first, /evidencelens-verification-loop, /evidencelens-rag-change-evaluation, and /evidencelens-frontend-release-review entry points. Each instructs the agent to read the canonical file; no procedural body is duplicated. Current Cursor documentation supports .agents/skills directly, so no duplicate Cursor project-skill set is added. Other host settings or global skills can still affect what a session lists; use exact project paths when ambiguous.

## Reliable skill loading and evidence

Here, a host means the editor/agent environment, such as Codex, Claude Code, or Cursor, including its workspace/session settings. A committed skill proves only that guidance exists in the checkout. Discovery, context loading, and applying it to the task are separate events.

Run from the repository root, choosing the actual host and stage:

```sh
python3 tools/agent_preflight.py --host codex --stage plan --context
python3 tools/agent_preflight.py --host claude --stage verify --rag --context
python3 tools/agent_preflight.py --host cursor --stage verify --frontend --context
```

The examples are alternatives, not instructions to claim three live-host tests. Stages are specify, plan, tasks, implement, verify, and converge. Add --rag or --frontend only when relevant. Output checks planning integrity, canonical/native routes, the selected upstream command hash, and disabled event configuration. It reports file paths/hashes and explicitly labels host discovery and application as unobserved/unverified. The --host argument is declared context, not authentication of the running editor.

With --context, the command prints selected skill contents, giving the current agent an explicit loading path even if automatic discovery is unavailable. It does not invoke a model, run an entire workflow, or demonstrate that the agent followed the instructions. Apply the guidance and record path/hash, how it was loaded, concrete actions, and result/evidence locations in the feature verification report. For example, search-first should produce a real reuse decision in research.md; verification-loop should produce actual check commands and outcomes.

For each host/version you use, a manual smoke prompt can establish session observations:

> Read AGENTS.md. Run the local preflight for this host at stage verify with --context. Identify the canonical verification skill and its hash, then run the planning-integrity check. Report the observed result and distinguish configured skills, explicitly loaded context, and concrete application evidence. Do not modify files or claim results for another host.

Keep the session/tool-output reference with the verification record. A successful session is evidence for that host/version/task, not all future sessions. Ordinary chats without repository/tool access need the relevant documents supplied through their available context workflow. No automatic hooks or GitHub Actions are required.

Primary discovery references checked on 2026-10-19: [OpenAI skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), and [Cursor skills](https://cursor.com/docs/skills).

## Feature selection and completion

For an existing feature, tell the agent its directory before working. Script users can explicitly select it with:

```sh
export SPECIFY_FEATURE_DIRECTORY="$PWD/specs/001-development-workflow"
bash .specify/scripts/bash/check-prerequisites.sh --json --require-spec --require-tasks
```

The current-feature pointer, .specify/feature.json, is local and ignored. Do not rely on another contributor's last selection. Git branching is managed normally; the optional Spec Kit Git extension is not installed.

Small behavior-preserving fixes can keep scope and verification in the PR. Changes to accepted behavior, contracts, estimates, or criteria require a new child edition referencing the original master and immediate parent. Drafts may be refined before issuance; sealed spec/plan files are immutable. Task status and verification results track execution without rewriting intent. Follow [the edition procedure](planning/README.md), including local integrity checks and manifest sealing.

## Sources of truth and customization

- .specify/memory/constitution.md: EvidenceLens governance, original Apache-2.0 material.
- .specify/templates/overrides/: shared specification, plan, task, and verification templates. Spec Kit's resolver gives these precedence over bundled templates.
- docs/planning/: original frozen master, baseline manifest, and future child editions. Existing supporting planning documents are sealed as part of the baseline.
- specs/FEATURE/: derived feature intent with root/parent/edition references, research, tasks, and verification. Accepted intent is sealed by an edition manifest; status/evidence remain execution records. Optional data-model/contracts artifacts need a concrete purpose.
- docs/templates/architecture-decision.md: lasting decisions only; feature research links rather than duplicates them.
- .agents/skills/search-first and verification-loop: selected ECC adaptations, integrated into the shared templates and constitution.
- .agents/skills/rag-change-evaluation and frontend-release-review: original project skills, invoked within the same feature.
- .agents/skills/speckit-*, .claude/skills/speckit-*, .cursor/skills/speckit-*: official generated agent integrations; keep project policy out of these managed files.

These are agent instructions and review gates, not a claim that an LLM is mechanically prevented from ignoring them. Local checks cover template resolution, prerequisite behavior, preservation of existing plans, upstream file integrity, and authored Markdown. Application tests and security/evaluation gates must be added with the corresponding implementation.

GitHub Actions is disabled throughout project development until the user explicitly requests it. Do not create, enable, dispatch, or restore workflows based on toolkit suggestions or roadmap milestones. Verification stays local; the absence of remote CI is intentional, not a release-evidence gap.

Markdown style checks exclude generated upstream skills and core templates so upgrades do not require unrelated formatting patches. Manifest hashes check those managed assets; project policy, overrides, and adapted ECC skills remain linted.

No global settings, automatic event hooks, ECC MCP servers, or autonomous workflow execution are enabled. The upstream bundled workflow is retained as an asset; the documented command-by-command process above includes EvidenceLens verification and convergence. It has not been executed as an autonomous workflow.

## Versions, licenses, and adaptations

[GitHub Spec Kit](https://github.com/github/spec-kit) is pinned to release **1.2.2**, commit `74be0a63e93c7087c5b06556b7561810d8f78a45`. Official assets are recorded in .specify/integrations/*.manifest.json, with the bundled workflow and constitution-template metadata retained. Its [MIT license](../third_party/spec-kit/LICENSE) is preserved. EvidenceLens overrides are separate; no generated upstream commands or scripts were patched.

[ECC](https://github.com/affaan-m/ECC) is pinned to commit `76aaa77df6adc5b889e689007bf99b9a4f74af34`. Adapted sources are skills/search-first/SKILL.md and skills/verification-loop/SKILL.md, retaining the [MIT license](../third_party/ecc/LICENSE). Adaptations remove mandatory delegation, global settings inspection, hardcoded npm commands, arbitrary coverage targets, and repeated checks without changes. They add the shared Spec Kit research and verification artifact contracts. The whole ECC distribution is not installed.

## Local CLI setup and maintenance

The committed integrations and shell helpers work without installing the Python CLI. For integration management, install the pinned CLI locally using Python 3.11+ and Git:

```sh
python3 -m venv .tools/spec-kit
.tools/spec-kit/bin/python -m pip install -r tools/spec-kit-requirements.txt
.tools/spec-kit/bin/specify version
```

.tools/ is ignored. The source revision is pinned; this requirements file is not a fully locked, cross-platform transitive dependency environment. The CLI is development tooling, not an application runtime dependency.

The repository was initialized with these commands; **do not reinitialize an ordinary clone**:

```sh
.tools/spec-kit/bin/specify init --here --force --non-interactive --integration codex --script sh --ignore-agent-tools --integration-options='--events false'
.tools/spec-kit/bin/specify integration install claude --integration-options='--events false'
.tools/spec-kit/bin/specify integration install cursor-agent --integration-options='--events false'
```

For upgrades, use a branch, review the chosen upstream release and license, update the pin, install it locally, and follow that version's integration upgrade instructions for all three editors. Preserve the constitution, overrides, ECC adaptations, and disabled events. Review generated manifests and all diffs before committing; never auto-update from main or manually refresh hashes to conceal changed upstream files.

Run the tooling tests and lint after changes:

```sh
python3 -m unittest discover -s tests/tooling -v
python3 tools/check_planning.py
npx --yes markdownlint-cli2@0.18.1
for script in .specify/scripts/bash/*.sh; do
  bash -n "$script" || exit 1
done
git diff --check
```

Ordinary ChatGPT chats do not automatically load repository files. Supply AGENTS.md, the constitution, relevant feature artifacts, and skills through the available repository/document workflow. Use the explicit preflight/context path and observable verification evidence above to reduce reliance on automatic discovery; record untested host behavior honestly.

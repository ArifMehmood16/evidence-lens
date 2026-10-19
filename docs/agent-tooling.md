# Spec Kit + ECC across EvidenceLens

Spec Kit owns the feature lifecycle; ECC contributes reuse research and verification inside it. This applies across the whole application, including ingestion, retrieval, generation, APIs, practitioner UI, evaluations, infrastructure, security, and operations. There is one specification and task list per feature.

AGENTS.md is the entry point for all agents. The [constitution](../.specify/memory/constitution.md) defines shared governance; [engineering standards](engineering-standards.md) supply detail. Official editor integrations read the same constitution and resolve the same project template overrides. The [feature index](../specs/README.md) connects this workflow to the roadmap.

## Daily workflow

1. **Specify:** use speckit-specify to capture a focused outcome, acceptance criteria, failure behavior, and required verification in specs/FEATURE/spec.md. Use speckit-clarify when material ambiguity remains.
2. **Plan with ECC:** use speckit-plan and read .agents/skills/search-first/SKILL.md. Record reuse decisions, upstream sources, alternatives, licenses, and reasons for custom code in research.md. Plan.md consumes that research and defines actual interfaces, budgets, recovery, and checks.
3. **Tasks:** use speckit-tasks. Tasks trace to requirements and include applicable testing and verification. Use speckit-analyze before substantial implementation to catch inconsistent or missing requirements.
4. **Implement with ECC:** use speckit-implement for the scoped tasks. Read .agents/skills/verification-loop/SKILL.md and record commands, results, acceptance mappings, and limitations in verification.md. Apply rag-change-evaluation and frontend-release-review when relevant.
5. **Converge:** use speckit-converge after implementation. Inspect actual behavior and the verification report against spec, plan, tasks, and constitution. Missing work or evidence becomes appended tasks. Implement fixes, update evidence, and converge again.
6. **Review and release:** link the feature artifacts and evidence in the PR. Deployment, publication, and external actions remain subject to the user's authorized scope.

For Codex, invoke skills as `$speckit-specify`, `$speckit-plan`, `$speckit-tasks`, `$speckit-implement`, and `$speckit-converge`. Claude Code and Cursor use their installed `/speckit-...` skills. Discovery can depend on the host version or opening a new session; explicitly reference the relevant SKILL.md if it is not listed.

For an existing feature, tell the agent its directory before working. Script users can explicitly select it with:

```sh
export SPECIFY_FEATURE_DIRECTORY="$PWD/specs/001-development-workflow"
bash .specify/scripts/bash/check-prerequisites.sh --json --require-spec --require-tasks
```

The current-feature pointer, .specify/feature.json, is local and ignored. Do not rely on another contributor's last selection. Git branching is managed normally; the optional Spec Kit Git extension is not installed.

Small behavior-preserving fixes can keep scope and verification in the PR. Changed behavior or contracts require updating the affected specification or creating a focused feature. Specs are living intent; Git preserves their history. Do not rewrite them to hide failed acceptance criteria.

## Sources of truth and customization

- .specify/memory/constitution.md: EvidenceLens governance, original Apache-2.0 material.
- .specify/templates/overrides/: shared specification, plan, task, and verification templates. Spec Kit's resolver gives these precedence over bundled templates.
- specs/FEATURE/: canonical intent, reuse research, delivery tasks, and verification evidence. Optional data-model/contracts artifacts need a concrete purpose.
- docs/templates/architecture-decision.md: lasting decisions only; feature research links rather than duplicates them.
- .agents/skills/search-first and verification-loop: selected ECC adaptations, integrated into the shared templates and constitution.
- .agents/skills/rag-change-evaluation and frontend-release-review: original project skills, invoked within the same feature.
- .agents/skills/speckit-*, .claude/skills/speckit-*, .cursor/skills/speckit-*: official generated agent integrations; keep project policy out of these managed files.

These are agent instructions and review gates, not a claim that an LLM is mechanically prevented from ignoring them. CI checks template resolution, prerequisite behavior, preservation of existing plans, upstream file integrity, and authored Markdown. Application tests and security/evaluation gates must be added with the corresponding implementation.

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
npx --yes markdownlint-cli2@0.18.1
```

Ordinary ChatGPT chats do not automatically load repository files. Supply AGENTS.md, the constitution, relevant feature artifacts, and skills through the available repository/document workflow. Editor discovery and model adherence require review; a committed skill is not proof that every host executed it.

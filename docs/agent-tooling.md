# Project-local agent tooling

EvidenceLens uses one shared policy in AGENTS.md. CLAUDE.md and the Cursor rule refer to it. Task-specific guidance lives in .agents/skills, so the always-loaded rules remain short.

## Selected skills

- **search-first:** compare repository capabilities and maintained libraries before substantial custom implementation.
- **verification-loop:** run applicable checks and report actual verification evidence.
- **rag-change-evaluation:** compare evidence-affecting changes using versioned baselines and the project evaluation specification.
- **frontend-release-review:** check public/private indexing boundaries, accessibility, SEO, performance, and deployment evidence.

The first two are adaptations of [affaan-m/ECC](https://github.com/affaan-m/ECC), pinned to commit `76aaa77df6adc5b889e689007bf99b9a4f74af34`. Their source paths are `skills/search-first/SKILL.md` and `skills/verification-loop/SKILL.md`. The upstream MIT license and copyright are retained in [third_party/ecc/LICENSE](../third_party/ecc/LICENSE). The other two skills are original Apache-2.0 project guidance.

## Deliberate adaptations

The research skill retains reuse-first decisions and tool-availability honesty, but removes mandatory delegation, global configuration inspection, and unrelated example tooling. The verification skill keeps build/type/lint/test/security/diff review where applicable, but removes hardcoded npm commands, arbitrary 80% coverage, simplistic security grep as an audit, and periodic rechecking without a change.

No ECC hooks, MCP servers, executable scripts, global settings, or blanket agent collection are installed. Skill text is reviewed guidance, not authority to perform external actions. Maintain attribution when updating adapted files.

## Using the skills across tools

Codex can discover project-local .agents/skills when supported by the host. Cursor reads .cursor/rules/evidencelens.mdc and can follow the same skill paths. Claude Code reads CLAUDE.md and can follow those paths. If automatic skill discovery differs in a tool/version, explicitly reference the relevant SKILL.md; do not assume all chat products load repository files automatically.

For ordinary ChatGPT use, supply the relevant repository documents or connect the repository using the available product workflow. Merely adding a file to GitHub does not guarantee it is loaded into every conversation.

When updating ECC adaptations, review the upstream diff, dependencies, links, scope, and license at a new pinned revision. Preserve project-specific constraints, validate skill frontmatter, and commit the reviewed changes. Do not auto-update from main.

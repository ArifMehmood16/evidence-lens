---
name: search-first
description: Research existing EvidenceLens code and maintained libraries before adding a dependency, integration, or substantial custom utility. Use for reuse decisions, not every small edit.
license: MIT
metadata:
  origin: ECC
---

# Search before implementation

Adapted from affaan-m/ECC at 76aaa77df6adc5b889e689007bf99b9a4f74af34.
See ../../../third_party/ecc/LICENSE and ../../../docs/agent-tooling.md.

1. Define the concrete capability and constraints from the current task. Search relevant repository modules and tests first.
2. Check which search tools are available. Use official package documentation, registries, and upstream repositories for relevant candidates. Report unavailable channels without claiming a comprehensive search.
3. Compare fit, maintenance, security, license, dependency weight, operational cost, and compatibility with the existing stack. Prefer existing dependencies and framework features where suitable.
4. Choose reuse, a thin adapter, composition, or custom code. A library is not automatically better if it adds more complexity than the problem warrants.
5. For a consequential choice, record the rationale using the repository ADR template. For a small change, explain it in the PR.
6. Implement the smallest useful integration and validate observable behavior.

Do not install tools just to complete this checklist. Do not create wrappers that merely rename every library method. Do not change global MCP servers, hooks, editor settings, or credentials. Ordinary research can run inline; this skill does not require delegation.

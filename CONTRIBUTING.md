# Contributing to EvidenceLens

The repository currently contains the design and engineering foundation. Begin with README.md, AGENTS.md, and docs/development-plan.md. There is no application test/build command yet; commands will be documented alongside the first runnable implementation. The Documentation workflow currently checks Markdown, including project skills and agent rules. It does not claim to run application tests or a security audit.

For substantial behavior, describe the practitioner problem and acceptance criteria using docs/templates/feature-spec.md. Small fixes can capture the same essentials in the issue or PR. Record a dependency or architectural decision only when it is consequential, using docs/templates/architecture-decision.md.

Reuse existing code and maintained libraries. Keep changes focused, preserve evidence provenance, and include tests appropriate to observable behavior. RAG configuration changes require relevant evaluation results and corpus/model/config identifiers. Do not report synthetic capacity tests as domain-quality validation.

Before submission, review the diff for unrelated changes, secrets, licensed source material, and personal paths. Explain what changed, why, what checks ran, and any limitations. Check the applicable controls in docs/engineering-standards.md. Security reporting follows SECURITY.md.

Project rules are shared through AGENTS.md. ECC-derived skills retain their MIT notices; original project contributions use Apache-2.0 unless explicitly agreed otherwise. Do not copy third-party code, models, or data without checking its license and preserving required notices.

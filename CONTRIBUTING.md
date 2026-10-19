# Contributing to EvidenceLens

The repository currently contains the design and engineering foundation. Begin with README.md, AGENTS.md, and docs/development-plan.md. There is no application test/build command yet; commands will be documented alongside the first runnable implementation. Run authored Markdown checks, tooling smoke tests, upstream asset integrity checks, and bundled shell syntax checks locally using docs/agent-tooling.md. These do not constitute application tests or a security audit.

GitHub Actions is disabled for project development. Do not add, enable, or dispatch workflows until the project owner explicitly requests it. Keep local verification evidence with each change.

For substantial behavior across any part of the application, follow the [Spec Kit + ECC workflow](docs/agent-tooling.md): specify → plan with ECC research → tasks → implement with ECC verification → converge. The [constitution](.specify/memory/constitution.md) governs completion. Keep requirements, decisions, tasks, and verification evidence together under specs/FEATURE/; use the [feature index](specs/README.md) to find existing work. Small behavior-preserving fixes may capture scope and evidence in the PR. Record lasting architectural decisions using docs/templates/architecture-decision.md.

Reuse existing code and maintained libraries. Keep changes focused, preserve evidence provenance, and include tests appropriate to observable behavior. RAG configuration changes require relevant evaluation results and corpus/model/config identifiers. Do not report synthetic capacity tests as domain-quality validation.

Before submission, review the diff for unrelated changes, secrets, licensed source material, and personal paths. Explain what changed, why, what checks ran, and any limitations. Check the applicable controls in docs/engineering-standards.md. Security reporting follows SECURITY.md.

Project rules are shared through AGENTS.md. Spec Kit assets and ECC-derived skills retain their MIT notices; original project contributions use Apache-2.0 unless explicitly agreed otherwise. Do not copy third-party code, models, or data without checking its license and preserving required notices.

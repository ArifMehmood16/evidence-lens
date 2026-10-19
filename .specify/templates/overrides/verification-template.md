# Verification: [FEATURE]

**Date**: [DATE] | **Checked scope**: [revision and any uncommitted changes]

**Planning lineage**: [master version, child edition, and F/W/AC IDs]. Run python3 tools/check_planning.py locally. Keep accepted intent unchanged; scope changes need a new child edition.

## Acceptance evidence

[Map FR/SC/story identifiers to tests, commands, measurements, and evidence paths.]

## Guidance used

[Declared host/version if known; preflight command and outcome; canonical skill paths and SHA-256 values; explicit read/invocation or observed discovery; concrete decisions/actions and evidence links. Keep file configuration, actual loading, and application evidence distinct. Mark other hosts not observed. A self-report or preflight pass alone is not proof of compliance.]

## Check outcomes

Record local checks. GitHub Actions is deferred until the user explicitly requests it; its absence is not a missing verification result.

- **[Check] — passed/failed/not run**: [command or manual procedure, outcome, reason if not run].

Include applicable build/types/lint, behavior, security, diff/license, recovery, RAG baseline/candidate versions, and frontend checks. Explain N/A. Never include secrets, private questions, or licensed full source documents.

## Limitations and remaining work

[Missing tools, untested platforms, external dependencies, unresolved risks, or exceptions with owner and expiry.]

## Convergence assessment

[Map implementation to spec/plan/tasks; list gaps and appended task references or explain why none remain. Tooling checks do not establish application quality.]

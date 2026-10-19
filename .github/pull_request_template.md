# Pull request

## Problem and resulting behavior

Describe the requirement or failure and the observable result of this change.

Link the original master F/W/AC IDs, parent/child edition, feature spec, and tasks for substantial work, or explain the small-fix scope. Changed intent requires a new child; never rewrite sealed specifications. Link reuse decisions in research.md when dependencies or custom infrastructure change.

## Verification

List relevant checks actually run, their outcomes, and anything not run. For RAG changes, link the corpus/config/model versions and baseline comparison.

Include the local planning-integrity check; confirm previously sealed files and manifests are unchanged. GitHub Actions remains disabled until explicitly requested.

Link the ECC verification report in specs/FEATURE/verification.md and state the convergence outcome. Missing required checks remain incomplete. Include applicable frontend, security, deployment, or recovery evidence.

## Review considerations

Describe material security, data/license, dependency, migration, rollback, or frontend visibility implications. Omit categories that do not apply. Link the feature spec or ADR when relevant.

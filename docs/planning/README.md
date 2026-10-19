# Master plan and child editions

The original is [EL-MASTER-1.0.0](master-plan-v1.0.0.md). It contains 24 features, 72 work units, 72 acceptance criteria, dependencies, release gates, and open decisions. [baseline.json](baseline.json) seals its bytes and its supporting documents. A sealed baseline is a record of intent, not evidence that implementation or practitioner validation is complete.

## What is frozen

Never edit the master, the baseline manifest, any file sealed by a manifest, or an already issued child manifest. This includes typo corrections, new estimates, threshold changes, refinements, and retirement. Make a child edition instead. The original supporting architecture, evaluation, scaling, roadmap, and engineering-standard files are frozen too; their draft headings are historical, not permission to change them.

Drafts can be edited before issuance. Use docs/planning/drafts/ for unsealed proposals. Drafts are not effective requirements. Root navigation files, agent routing, tooling templates, task completion status, and measured verification records are working material; changing them must not alter accepted intent. Requirements, acceptance criteria, and dependencies belong in sealed intent files. Where a working guide conflicts, the effective planning lineage governs.

## Linear edition lineage

The baseline is edition 0. Each accepted child gets the next contiguous number: docs/planning/editions/0001/, then 0002/, and so on. Each directory contains edition.md and manifest.json. It may also seal new feature spec/plan files under specs/. A child references both the immutable root and its immediate predecessor. Draft alternatives do not create parallel accepted histories.

Resolve current intent by reading the baseline and applying children in numeric order. Each child inherits unchanged intent and explicitly adds, replaces, or retires named IDs. Later children supersede only those named targets; they do not replace the entire master implicitly. Retired IDs remain tombstones and are never reused. Fixes to an issued child need a new child of the latest edition, even when the correction concerns an older ancestor.

A standalone feature elaboration is an additive child: give its additional requirements distinct IDs and reference the original F/W/AC IDs. If it changes an existing criterion rather than elaborating it, declare a replacement. Use the existing master and immediate-parent links instead of copying the entire master into every feature.

## Author a child

1. Read the root and all accepted children. Run the integrity checker before modifying anything.
2. Draft an edition using [the child template](../templates/planning-edition.md). Identify reason, scope, target IDs, root and parent references, exact before/after intent, dependencies, verification, and compatibility or migration effects.
3. Use Spec Kit for its feature artifacts, with ECC research and verification in the same feature directory. Each spec/plan names the root, parent, edition, and affected IDs. Convergence may append execution tasks; it cannot change sealed spec/plan intent.
4. Resolve blocking ambiguity within the user's authorized scope. Record material assumptions and pending decisions honestly. A sealed planning edition does not grant cloud spend, deployment, Actions, publication, or practitioner approval.
5. Put the finalized edition in the next numbered directory. Create manifest.json with the structure below. Include all newly accepted intent files and their SHA-256 hashes. Do not include mutable task status or result logs in the sealed set.
6. Run local integrity, link, Markdown, and relevant behavior checks. Review the diff for any edit to previously sealed paths. Commit the new files together. The parent manifest digest and Git history make lineage changes reviewable.

Example manifest shape (placeholders must be replaced; this is not an issued edition):

```json
{
  "schema_version": 1,
  "edition": 1,
  "root": "docs/planning/master-plan-v1.0.0.md",
  "parent": "docs/planning/baseline.json",
  "parent_sha256": "SHA256_OF_PARENT_MANIFEST_BYTES",
  "files": {
    "docs/planning/editions/0001/edition.md": "SHA256_OF_EDITION_BYTES",
    "specs/002-evidence-contract/spec.md": "SHA256_OF_SPEC_BYTES",
    "specs/002-evidence-contract/plan.md": "SHA256_OF_PLAN_BYTES"
  },
  "changes": [
    {
      "operation": "add",
      "target": "F01.FR001",
      "references": ["F01", "F01.W01", "F01.AC01"],
      "reason": "Elaborate the seed-question contract without changing its acceptance criterion."
    }
  ]
}
```

Every reference must already exist in inherited intent or be introduced earlier in the same child. Replacements and retirements target existing active IDs; additions use new IDs. Document changes in readable prose as well as manifest metadata. The checker validates identity and lineage, not clinical meaning or logical equivalence of prose; review still matters.

## Local checks and limits

```sh
python3 tools/check_planning.py
python3 -m unittest discover -s tests/tooling -v
npx --yes markdownlint-cli2@0.18.1
git diff --check
```

The checker verifies sealed file hashes, parent digests, contiguous edition numbering, stable change references, catalogue dependency references/cycles, and that already committed manifests have not changed or disappeared relative to HEAD. It cannot prevent a person bypassing local checks or rewriting Git history. There are no GitHub Actions or automatic hooks. Do not claim filesystem-level immutability.

If a frozen file or manifest changes accidentally, recover the exact committed bytes and move the intended change into a child. Do not regenerate its hash to bless the edit. Only newly issued files receive new hashes. No active child exists at baseline issuance; the master is then the effective plan.

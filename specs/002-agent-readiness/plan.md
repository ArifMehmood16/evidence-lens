# Implementation Plan: Agent skill readiness

**Feature:** DEV-002 | **Spec:** [spec.md](spec.md) | **Edition:** [0001](../../docs/planning/editions/0001/edition.md).  
**Root/parent:** EL-MASTER-1.0.0 and docs/planning/baseline.json; P05/P08/G07.

## Research and design

Follow [research.md](research.md). Keep one canonical .agents skill body. Add four small, project-prefixed Claude entries that point to those bodies. Current Cursor documentation already supports .agents/skills, so avoid duplicate Cursor copies. Preserve official Spec Kit files and disabled event settings.

Use a standard-library Python preflight, reusing the existing planning-integrity checker. Host and stage select the relevant official command and ECC skill. Optional flags include domain skills. Output declares file-level configuration evidence and can expose the selected bodies directly to the current agent session. No host/model process is launched and no receipt falsely attests that a model obeyed instructions.

## Work units

- **DEV002.W01:** native Claude routing entries; acceptance AC1. Input: canonical skills and official host docs. Output: four small SKILL.md routes.
- **DEV002.W02:** local preflight; acceptance AC2. Depends on W01. Output: read-only path/hash/context command and regressions for missing routes, stale context hashes, and modified upstream commands.
- **DEV002.W03:** shared workflow and verification evidence; acceptance AC3. Depends on W02. Output: guidance, evidence-report fields, a manual live-host smoke prompt, and the actual local verification record.

## Constitution and gates

Pass: additive child lineage, canonical reuse, small implementation, meaningful local tests, and honest limitations. Existing master/supporting files are unchanged. Source/security/clinical and public-page behavior checks are N/A; no application functionality changes. Planning integrity and upstream hashes remain required.

## Verification and rollback

Run preflight for all three declared host paths, print relevant verification context in this session, run tooling tests, skill frontmatter validation, Markdown lint, local links, and diff checks. These validate configuration, not interactive sessions in all three editors. Record exactly what was observed in verification.md.

Rollback implementation using Git while retaining the issued planning history; a reversal of accepted intent requires a subsequent child edition. No domain schemas or external API contracts are needed for this developer-tooling feature.

# EvidenceLens

Read and follow AGENTS.md as the shared repository guidance. Read only the relevant design documents and project-local skills from .agents/skills. Use docs/engineering-standards.md for detailed policy. Do not duplicate those instructions here or assume configured checks have run.

Use the official .claude/skills/speckit-* commands with the shared constitution and overrides in .specify/. ECC research and verification feed the same feature artifacts; see docs/agent-tooling.md.

The /evidencelens-search-first, /evidencelens-verification-loop, /evidencelens-rag-change-evaluation, and /evidencelens-frontend-release-review entries route to canonical .agents skills. Run python3 tools/agent_preflight.py --host claude --stage plan --context for planning (select the actual stage for other work); report concrete application evidence rather than treating discovery as execution.

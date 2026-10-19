# Research: Agent skill discovery and use

ECC search-first reviewed the current project before adding new tooling. Existing assets include canonical .agents skills, three official Spec Kit integrations, thin AGENTS/CLAUDE/Cursor routing, a local planning checker, and offline tooling tests.

The actionable gap is Claude Code's native discovery path for the four project-specific skills. Current Cursor documentation explicitly includes .agents/skills, so duplicating them in .cursor/skills adds little benefit. Claude routes use an evidencelens- prefix to reduce ambiguity with similarly named global skills; session settings can still affect discovery.

Primary sources inspected on 2026-10-19:

- [Official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills): repo discovery under .agents/skills and the distinction between skill metadata and loaded instructions.
- [Claude Code skills](https://code.claude.com/docs/en/skills): native .claude/skills discovery, explicit invocation, workspace/session restrictions, and precedence.
- [Cursor skills](https://cursor.com/docs/skills): .agents/skills support and explicit selection.

Chosen approach: minimal native routes, explicit context loading, and observable verification evidence. A checksum demonstrates file identity and freshness, not comprehension or compliance. Host smoke prompts remain manual until actually exercised.

Reuse Python's standard library and the existing check_planning helper. No new package, autonomous model invocation, global configuration, hook, or hosted automation is needed. Existing ECC adaptation notices remain; the new thin routing text and tool are original project material.

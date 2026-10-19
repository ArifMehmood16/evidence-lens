# Research: Shared development workflow

ECC search-first applied to the existing repository, official source, and CLI behavior.

- **Reuse decision:** keep the two reviewed ECC adaptations already present. A wholesale ECC installation would add unrelated agents, hooks, and configuration without serving this integration.
- **Spec Kit:** use official [release v1.2.2](https://github.com/github/spec-kit/releases/tag/v1.2.2), source commit 74be0a63e93c7087c5b06556b7561810d8f78a45. Inspect CLI help and installed source before selecting integration flags.
- **Customization:** common.sh supports .specify/templates/overrides/ with highest precedence. Constitution and overrides can govern every installed editor without patching generated commands or maintaining a custom orchestration framework.
- **Integrations:** official codex, claude, and cursor-agent integrations render skills into their native directories. Events are explicitly disabled. The core Git extension is optional and is not installed.
- **Alternative considered:** the lean preset reduces instruction volume but removes useful lifecycle detail. Keep the official core with concise project overrides instead.
- **Verification:** use Python unittest plus shipped Bash helpers in temporary fixtures. This needs no application framework, network, cloud, or model calls. Preserve upstream hashes to catch accidental changes during future upgrades.
- **Licensing:** Spec Kit and ECC are MIT; retain both notices. Original EvidenceLens policy and tests remain Apache-2.0.
- **Limits:** the CLI source is pinned, while its transitive packages are not fully locked. No supported-editor interactive session or autonomous workflow is claimed as tested.

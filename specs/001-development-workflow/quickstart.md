# Validate the development workflow

From the repository root, run:

```sh
python3 -m unittest discover -s tests/tooling -v
npx --yes markdownlint-cli2@0.18.1
```

The suite creates temporary fixtures, uses official scripts to create a feature and select templates, verifies reruns preserve an existing plan, checks prerequisite errors, and verifies all registered upstream assets. No model, corpus, or cloud credentials are required.

To inspect the templates without creating feature state:

```sh
bash .specify/scripts/bash/resolve-template.sh plan-template
bash .specify/scripts/bash/resolve-template.sh tasks-template
```

Expected: the project override contents include ECC research and verification obligations. Existing real feature files remain unchanged by the test suite.

Follow [agent-tooling.md](../../docs/agent-tooling.md) for optional CLI installation and editor commands. An actual editor session must read the constitution and relevant ECC skills; successful shell tests alone do not prove that behavior.

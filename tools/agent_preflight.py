"""Check local agent configuration and explicitly expose task-relevant guidance."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

from check_planning import check_planning


ROOT = Path(__file__).resolve().parents[1]
PROJECT_SKILLS = ("search-first", "verification-loop", "rag-change-evaluation",
                  "frontend-release-review")
HOSTS = {"codex": (".agents", "codex"), "claude": (".claude", "claude"),
         "cursor": (".cursor", "cursor-agent")}
STAGES = ("specify", "plan", "tasks", "implement", "verify", "converge")


def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect_setup(root, host, stage):
    """Check files on disk, not whether an editor discovered or used them."""
    root = Path(root)
    for name in PROJECT_SKILLS:
        canonical = root / ".agents/skills" / name / "SKILL.md"
        if not canonical.is_file():
            raise ValueError(f"Missing canonical skill: {canonical.relative_to(root)}")
        adapter = root / ".claude/skills" / f"evidencelens-{name}" / "SKILL.md"
        reference = f"../../../.agents/skills/{name}/SKILL.md"
        if not adapter.is_file() or f"]({reference})" not in adapter.read_text():
            raise ValueError(f"Missing/broken Claude entry point for {name}")
        if (adapter.parent / reference).resolve() != canonical.resolve():
            raise ValueError(f"Incorrect canonical target for {name}")
    directory, integration = HOSTS[host]
    manifest_path = root / ".specify/integrations" / f"{integration}.manifest.json"
    manifest = json.loads(manifest_path.read_text())
    settings = json.loads((root / ".specify/integration.json").read_text())
    if settings["integration_settings"][integration]["parsed_options"]["events"] != "false":
        raise ValueError(f"Automatic events must remain disabled for {host}")
    if stage != "verify":
        skill = f"{directory}/skills/speckit-{stage}/SKILL.md"
        expected = manifest["files"].get(skill)
        if not expected or fingerprint(root / skill) != expected:
            raise ValueError(f"Missing/modified upstream skill: {skill}")


def build_context(root, host, stage, rag=False, frontend=False):
    inspect_setup(root, host, stage)
    names = []
    if stage == "plan":
        names.append("search-first")
    if stage in {"implement", "verify", "converge"}:
        names.append("verification-loop")
    if rag:
        names.append("rag-change-evaluation")
    if frontend:
        names.append("frontend-release-review")
    paths = [f".agents/skills/{name}/SKILL.md" for name in names]
    if stage != "verify":
        paths.insert(0, f"{HOSTS[host][0]}/skills/speckit-{stage}/SKILL.md")
    return [{"path": path, "sha256": fingerprint(Path(root) / path)} for path in paths]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=HOSTS, required=True,
                        help="Declared editor; does not authenticate its identity")
    parser.add_argument("--stage", choices=STAGES, required=True)
    parser.add_argument("--rag", action="store_true", help="Include RAG change guidance")
    parser.add_argument("--frontend", action="store_true", help="Include frontend guidance")
    parser.add_argument("--context", action="store_true",
                        help="Print skill contents for explicit loading in this session")
    args = parser.parse_args()
    try:
        check_planning(ROOT)
        skills = build_context(ROOT, args.host, args.stage, args.rag, args.frontend)
        revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT,
                                           text=True).strip()
        print(json.dumps({"configuration": "passed", "declared_host": args.host,
                          "stage": args.stage, "revision": revision,
                          "host_discovery": "not_observed",
                          "skill_application": "not_verified", "skills": skills}, indent=2))
        print("Read AGENTS.md, the effective master/child lineage, and the selected skills.")
        print("Report path/hash, a concrete action, evidence, and limitations in verification.md.")
        if args.context:
            for skill in skills:
                print(f"\n--- CONTEXT: {skill['path']} | SHA256: {skill['sha256']} ---")
                print((ROOT / skill["path"]).read_text())
        return 0
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f"Agent preflight failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

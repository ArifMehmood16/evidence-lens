"""Validate the frozen planning baseline and append-only edition lineage locally."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
BASELINE = "docs/planning/baseline.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_path(root, name):
    path = Path(name)
    require(not path.is_absolute() and ".." not in path.parts,
            f"Expected a repository-relative path: {name}")
    resolved = (root / path).resolve()
    require(resolved.is_relative_to(root.resolve()), f"Path escapes repository: {name}")
    return resolved


def check_catalogue(text):
    features = re.findall(r"^## (F\d{2})$", text, re.M)
    blocks = re.findall(r"^### (F\d{2}\.W\d{2})\n(.*?)(?=^### |^## |\Z)",
                        text, re.M | re.S)
    units = dict(blocks)
    require(len(features) == len(set(features)), "Duplicate feature ID")
    require(len(units) == len(blocks) and units, "Missing or duplicate work-unit IDs")
    graph = {}
    for unit, body in blocks:
        require(unit.split(".")[0] in features, f"Unknown feature for {unit}")
        acceptance = unit.replace(".W", ".AC")
        require(f"**Acceptance {acceptance}:**" in body,
                f"Missing matching acceptance criterion for {unit}")
        for field in ("Input", "Deliverable", "Verification", "Depends on"):
            require(f"**{field}:**" in body, f"Missing {field} for {unit}")
        dependency_line = re.search(r"\*\*Depends on:\*\*([^\n]*)", body).group(1)
        graph[unit] = re.findall(r"F\d{2}\.W\d{2}", dependency_line)
        require(all(dep in units for dep in graph[unit]), f"Unknown dependency for {unit}")
    visited, active = set(), set()

    def visit(unit):
        require(unit not in active, f"Dependency cycle at {unit}")
        if unit in visited:
            return
        active.add(unit)
        for dependency in graph[unit]:
            visit(dependency)
        active.remove(unit)
        visited.add(unit)

    for unit in graph:
        visit(unit)
    return len(features), len(units)


def check_committed_manifests(root, manifests):
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", "--", "docs/planning"],
        cwd=root, capture_output=True, text=True, check=False,
    )
    require(result.returncode == 0, "Cannot inspect committed planning history")
    for name in result.stdout.splitlines():
        if name != BASELINE and not re.fullmatch(
                r"docs/planning/editions/\d{4}/manifest\.json", name):
            continue
        require(name in manifests, f"Committed manifest removed: {name}")
        previous = subprocess.check_output(["git", "show", f"HEAD:{name}"], cwd=root)
        require((root / name).read_bytes() == previous,
                f"Committed manifest changed: {name}; create a child edition")


def check_planning(root=ROOT, check_git=True):
    root = Path(root)
    children = sorted((root / "docs/planning/editions").glob("*/manifest.json"))
    manifests = [BASELINE] + [path.relative_to(root).as_posix() for path in children]
    if check_git:
        check_committed_manifests(root, manifests)
    baseline = json.loads((root / BASELINE).read_text())
    master_name = baseline["root"]
    master = local_path(root, master_name).read_text()
    features, units = check_catalogue(master)
    known = set(re.findall(r"\b(?:F\d{2}(?:\.(?:W|AC)\d{2})?|[PGD]\d{2})\b", master))
    active = set(known)
    sealed = set()
    previous = None
    for number, name in enumerate(manifests):
        manifest = json.loads((root / name).read_text())
        require(manifest["schema_version"] == 1, f"Unknown schema: {name}")
        require(manifest["edition"] == number, f"Noncontiguous edition: {name}")
        require(manifest["root"] == master_name, f"Changed root: {name}")
        require(manifest["parent"] == previous, f"Incorrect parent: {name}")
        files = manifest["files"]
        require(isinstance(files, dict) and files, f"No sealed files: {name}")
        if number == 0:
            require(master_name in files, "Baseline does not seal its master")
        else:
            expected_name = f"docs/planning/editions/{number:04d}/manifest.json"
            require(name == expected_name, f"Incorrect edition directory: {name}")
            require(manifest["parent_sha256"] == digest(root / previous),
                    f"Parent digest mismatch: {name}")
            require(str(Path(name).with_name("edition.md")) in files,
                    f"Missing sealed edition.md: {name}")
            changes = manifest.get("changes", [])
            require(changes, f"No declared changes: {name}")
            targets = set()
            for change in changes:
                operation, target = change["operation"], change["target"]
                require(target not in targets, f"Ambiguous repeated target: {target}")
                targets.add(target)
                require(change.get("reason") and change.get("references"),
                        f"Missing reason or references: {target}")
                require(all(ref in known for ref in change["references"]),
                        f"Unknown inherited reference: {target}")
                if operation == "add":
                    require(target not in known, f"Reused identifier: {target}")
                    known.add(target)
                    active.add(target)
                else:
                    require(operation in {"replace", "retire"}, f"Unknown operation: {operation}")
                    require(target in active, f"Inactive/unknown target: {target}")
                    if operation == "retire":
                        active.remove(target)
        for file_name, expected in files.items():
            require(file_name not in sealed and file_name not in manifests,
                    f"Cannot reseal an ancestor or manifest: {file_name}")
            require(digest(local_path(root, file_name)) == expected,
                    f"Frozen file changed: {file_name}; restore it and create a child")
            sealed.add(file_name)
        previous = name
    return features, units, len(manifests) - 1, len(sealed)


if __name__ == "__main__":
    try:
        features, units, children, files = check_planning()
        print(f"Planning integrity passed: {features} features, {units} units, "
              f"{children} child editions, {files} sealed files.")
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f"Planning integrity failed: {error}", file=sys.stderr)
        sys.exit(1)

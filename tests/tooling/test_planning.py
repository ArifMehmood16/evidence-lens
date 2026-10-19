"""Regression checks for accidental baseline edits and broken edition lineage."""

import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


MODULE = Path(__file__).resolve().parents[2] / "tools/check_planning.py"
SPEC = importlib.util.spec_from_file_location("check_planning", MODULE)
planning = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(planning)


class PlanningIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.master = self.root / "docs/planning/master.md"
        self.master.parent.mkdir(parents=True)
        self.master.write_text("## F01\n\n### F01.W01\n\n**Depends on:** None\n"
                               "**Input:** Request\n**Deliverable:** Plan\n"
                               "**Acceptance F01.AC01:** Traceable\n**Verification:** Review\n")
        self.baseline = self.root / planning.BASELINE
        self.data = {"schema_version": 1, "edition": 0, "parent": None,
                     "root": "docs/planning/master.md",
                     "files": {"docs/planning/master.md": planning.digest(self.master)}}
        self.baseline.write_text(json.dumps(self.data))

    def test_baseline_edit_is_rejected(self):
        self.assertEqual(planning.check_planning(self.root, check_git=False), (1, 1, 0, 1))
        self.master.write_text(self.master.read_text() + "\nChanged intent\n")
        with self.assertRaisesRegex(ValueError, "Frozen file changed"):
            planning.check_planning(self.root, check_git=False)

    def test_child_inherits_root_and_rejects_wrong_parent_digest(self):
        folder = self.root / "docs/planning/editions/0001"
        folder.mkdir(parents=True)
        edition = folder / "edition.md"
        edition.write_text("Child referencing the original F01.AC01 requirement.\n")
        child = {"schema_version": 1, "edition": 1, "root": self.data["root"],
                 "parent": planning.BASELINE, "parent_sha256": planning.digest(self.baseline),
                 "files": {edition.relative_to(self.root).as_posix(): planning.digest(edition)},
                 "changes": [{"operation": "replace", "target": "F01.AC01",
                              "references": ["F01"], "reason": "New user requirement"}]}
        manifest = folder / "manifest.json"
        manifest.write_text(json.dumps(child))
        self.assertEqual(planning.check_planning(self.root, check_git=False), (1, 1, 1, 2))
        child["parent_sha256"] = "0" * 64
        manifest.write_text(json.dumps(child))
        with self.assertRaisesRegex(ValueError, "Parent digest mismatch"):
            planning.check_planning(self.root, check_git=False)

    def test_rehashing_committed_baseline_is_rejected(self):
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                        "-c", "commit.gpgsign=false", "commit", "-qm", "Seal baseline"],
                       cwd=self.root, check=True)
        self.master.write_text(self.master.read_text() + "\nRewritten intent\n")
        self.data["files"][self.data["root"]] = planning.digest(self.master)
        self.baseline.write_text(json.dumps(self.data))
        with self.assertRaisesRegex(ValueError, "Committed manifest changed"):
            planning.check_planning(self.root)

    def test_cyclic_unit_dependency_is_rejected(self):
        text = self.master.read_text().replace("Depends on:** None", "Depends on:** F01.W01")
        with self.assertRaisesRegex(ValueError, "Dependency cycle"):
            planning.check_catalogue(text)


if __name__ == "__main__":
    unittest.main()

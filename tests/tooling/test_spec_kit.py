"""Exercise the shipped Spec Kit helpers without touching active feature state."""

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]


class SpecKitWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="evidencelens-tooling-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / ".specify", self.root / ".specify",
                        ignore=shutil.ignore_patterns("feature.json", "workflow-runs"))
        self.env = {key: value for key, value in os.environ.items()
                    if not key.startswith(("SPECIFY_", "SPECKIT_"))}
        self.env["SPECIFY_INIT_DIR"] = str(self.root)

    def run_helper(self, name, *args, success=True):
        result = subprocess.run(
            ["bash", str(self.root / ".specify/scripts/bash" / name), *args],
            cwd=self.root, env=self.env, capture_output=True, text=True,
            timeout=20, check=False,
        )
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def create_feature(self):
        result = self.run_helper(
            "create-new-feature.sh", "--json", "--short-name", "workflow-test",
            "Validate shared development workflow",
        )
        feature = Path(json.loads(result.stdout)["SPEC_FILE"]).parent
        self.assertTrue(feature.is_relative_to(self.root))
        self.env["SPECIFY_FEATURE_DIRECTORY"] = str(feature)
        return feature

    def test_creation_uses_project_overrides_and_task_setup(self):
        feature = self.create_feature()
        overrides = self.root / ".specify/templates/overrides"
        self.assertEqual((feature / "spec.md").read_text(),
                         (overrides / "spec-template.md").read_text())
        self.run_helper("setup-plan.sh", "--json")
        self.assertEqual((feature / "plan.md").read_text(),
                         (overrides / "plan-template.md").read_text())
        tasks = json.loads(self.run_helper("setup-tasks.sh", "--json").stdout)
        self.assertEqual(Path(tasks["TASKS_TEMPLATE"]), overrides / "tasks-template.md")
        self.assertEqual(tasks["TASKS_TEMPLATE_CONTENT"],
                         (overrides / "tasks-template.md").read_text())
        (feature / "tasks.md").write_text(tasks["TASKS_TEMPLATE_CONTENT"])
        result = self.run_helper("check-prerequisites.sh", "--json",
                                 "--require-spec", "--require-tasks", "--include-tasks")
        self.assertIn("tasks.md", json.loads(result.stdout)["AVAILABLE_DOCS"])

    def test_plan_setup_preserves_existing_edits(self):
        feature = self.create_feature()
        self.run_helper("setup-plan.sh", "--json")
        plan = feature / "plan.md"
        edited = plan.read_text() + "\nContributor decision: preserve this design.\n"
        plan.write_text(edited)
        self.run_helper("setup-plan.sh", "--json")
        self.assertEqual(plan.read_text(), edited)

    def test_missing_prerequisites_fail_without_creating_tasks(self):
        feature = self.create_feature()
        result = self.run_helper("setup-tasks.sh", "--json", success=False)
        self.assertIn("plan.md", result.stderr)
        self.assertFalse((feature / "tasks.md").exists())
        self.run_helper("setup-plan.sh", "--json")
        result = self.run_helper("check-prerequisites.sh", "--json",
                                 "--require-spec", "--require-tasks", success=False)
        self.assertIn("tasks.md", result.stderr)

    def test_managed_assets_and_disabled_event_settings(self):
        state = json.loads((ROOT / ".specify/integration.json").read_text())
        self.assertEqual(set(state["installed_integrations"]),
                         {"codex", "claude", "cursor-agent"})
        for settings in state["integration_settings"].values():
            self.assertEqual(settings["parsed_options"]["events"], "false")
        manifests = list((ROOT / ".specify/integrations").glob("*.manifest.json"))
        self.assertEqual({path.name for path in manifests},
                         {f"{name}.manifest.json" for name in
                          ("codex", "claude", "cursor-agent", "speckit")})
        for manifest_path in manifests:
            manifest = json.loads(manifest_path.read_text())
            for name, expected in manifest["files"].items():
                with self.subTest(integration=manifest["integration"], file=name):
                    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                    self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

"""Check discovery routing failures and canonical context freshness."""

import importlib.util
from pathlib import Path
import shutil
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
SPEC = importlib.util.spec_from_file_location("agent_preflight", ROOT / "tools/agent_preflight.py")
preflight = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(preflight)


class AgentPreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in (".agents", ".claude", ".cursor"):
            shutil.copytree(ROOT / name, self.root / name)
        shutil.copytree(ROOT / ".specify/integrations", self.root / ".specify/integrations")
        shutil.copy(ROOT / ".specify/integration.json", self.root / ".specify/integration.json")

    def test_missing_claude_entry_point_fails(self):
        (self.root / ".claude/skills/evidencelens-search-first/SKILL.md").unlink()
        with self.assertRaisesRegex(ValueError, "Claude entry point"):
            preflight.inspect_setup(self.root, "claude", "plan")

    def test_context_reflects_current_canonical_skill(self):
        before = preflight.build_context(self.root, "codex", "plan")
        canonical = self.root / ".agents/skills/search-first/SKILL.md"
        canonical.write_text(canonical.read_text() + "\nNew reviewed guidance.\n")
        after = preflight.build_context(self.root, "codex", "plan")
        self.assertEqual(before[-1]["path"], after[-1]["path"])
        self.assertNotEqual(before[-1]["sha256"], after[-1]["sha256"])

    def test_modified_upstream_command_fails(self):
        skill = self.root / ".cursor/skills/speckit-plan/SKILL.md"
        skill.write_text(skill.read_text() + "\nUnexpected modification.\n")
        with self.assertRaisesRegex(ValueError, "upstream skill"):
            preflight.inspect_setup(self.root, "cursor", "plan")


if __name__ == "__main__":
    unittest.main()

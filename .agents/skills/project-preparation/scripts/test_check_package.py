"""Behavioral checks for promised artifacts and design-pending handoffs."""

import tempfile
import unittest
from pathlib import Path

from check_package import inspect


class PackageChecks(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name).resolve()
        (self.root / "docs").mkdir()
        (self.root / "README.md").write_text("# Project\n", encoding="utf-8")
        (self.root / "AGENTS.md").write_text("# Instructions\n", encoding="utf-8")

    def test_unlinked_promised_artifact_must_exist(self):
        issues, _ = inspect(self.root, None, ("docs/workflow.md",))
        self.assertIn("missing promised document: docs/workflow.md", issues)

    def test_document_directory_does_not_satisfy_promised_file(self):
        (self.root / "docs" / "workflow.md").mkdir()
        issues, _ = inspect(self.root, None, ("docs/workflow.md",))
        self.assertIn("missing promised document: docs/workflow.md", issues)

    def test_empty_promised_document_fails(self):
        (self.root / "docs" / "workflow.md").write_text(" \n", encoding="utf-8")
        issues, _ = inspect(self.root, None, ("docs/workflow.md",))
        self.assertIn("empty promised document: docs/workflow.md", issues)

    def test_promised_document_cannot_leave_package(self):
        issues, _ = inspect(self.root, None, ("../outside.md",))
        self.assertIn("document path leaves package root: ../outside.md", issues)

    def test_design_pending_package_needs_no_screen_inventory(self):
        for name in ("flows.md", "plan.md", "workflow.md"):
            (self.root / "docs" / name).write_text(
                "# Contract\nUI designs are pending subsequent design work.\n",
                encoding="utf-8",
            )
        (self.root / "AGENTS.md").write_text(
            "Read [flows](docs/flows.md), [plan](docs/plan.md) "
            "and [workflow](docs/workflow.md).\n", encoding="utf-8",
        )
        issues, _ = inspect(
            self.root, None,
            ("docs/flows.md", "docs/plan.md", "docs/workflow.md"),
        )
        self.assertEqual([], issues)

    def test_existing_missing_design_reference_still_fails(self):
        (self.root / "AGENTS.md").write_text(
            "Read [screens](docs/screens.md).\n", encoding="utf-8",
        )
        issues, _ = inspect(self.root, None)
        self.assertTrue(any("unresolved local reference docs/screens.md" in i for i in issues))


if __name__ == "__main__":
    unittest.main()

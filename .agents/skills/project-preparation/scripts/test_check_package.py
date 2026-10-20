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

    def test_proposed_inventory_and_kickoff_allow_pending_designs(self):
        for name in ("flows.md", "plan.md", "workflow.md"):
            (self.root / "docs" / name).write_text(
                "# Contract\nUI designs are pending subsequent design work.\n",
                encoding="utf-8",
            )
        (self.root / "docs" / "ui").mkdir()
        (self.root / "docs" / "ui" / "screen-inventory.md").write_text(
            "# Screens\n"
            "| Screen | Name | Flow steps | Design |\n"
            "| --- | --- | --- | --- |\n"
            "| SCR-012 | Invoice details | FL-004.S03, FL-005.S01 | Pending |\n"
            "Required variants: Desktop Default, Desktop Error, Mobile Default.\n",
            encoding="utf-8",
        )
        (self.root / "PROJECT_INITIATION_PROMPT.md").write_text(
            "Read [instructions](AGENTS.md), [plan](docs/plan.md) and "
            "[workflow](docs/workflow.md). Select current ready work from the plan. "
            "For UI work use [flows](docs/flows.md) and "
            "[screens](docs/ui/screen-inventory.md).\n", encoding="utf-8",
        )
        (self.root / "AGENTS.md").write_text(
            "Read [flows](docs/flows.md), [plan](docs/plan.md) "
            "and [workflow](docs/workflow.md).\n", encoding="utf-8",
        )
        issues, _ = inspect(
            self.root, None,
            ("docs/flows.md", "docs/plan.md", "docs/workflow.md",
             "docs/ui/screen-inventory.md", "PROJECT_INITIATION_PROMPT.md"),
        )
        self.assertEqual([], issues)

    def test_missing_kickoff_or_inventory_is_reported(self):
        for document in ("PROJECT_INITIATION_PROMPT.md", "docs/ui/screen-inventory.md"):
            with self.subTest(document=document):
                issues, _ = inspect(self.root, None, (document,))
                self.assertIn(f"missing promised document: {document}", issues)

    def test_non_ui_package_does_not_require_inventory(self):
        (self.root / "PROJECT_INITIATION_PROMPT.md").write_text(
            "Read [instructions](AGENTS.md). This project provides a CLI.\n",
            encoding="utf-8",
        )
        issues, _ = inspect(self.root, None, ("PROJECT_INITIATION_PROMPT.md",))
        self.assertEqual([], issues)

    def test_existing_missing_design_reference_still_fails(self):
        (self.root / "AGENTS.md").write_text(
            "Read [screens](docs/screens.md).\n", encoding="utf-8",
        )
        issues, _ = inspect(self.root, None)
        self.assertTrue(any("unresolved local reference docs/screens.md" in i for i in issues))


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_docs.py"
SPEC = importlib.util.spec_from_file_location("validate_docs", SCRIPT)
assert SPEC and SPEC.loader
validate_docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validate_docs)


class ValidateDocsTest(unittest.TestCase):
    def test_valid_document_set(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "guide.md").write_text(
                "# Guide\n\n## Install the tool\n\n"
                "Use the command:\n\n```bash\ntool install\n```\n\n"
                "See the [reference](reference.md#configuration-fields).\n",
                encoding="utf-8",
            )
            (root / "reference.md").write_text(
                "# Reference\n\n## Configuration fields\n\nExact values.\n",
                encoding="utf-8",
            )

            files, discovery_errors = validate_docs.markdown_files([root])
            errors = list(discovery_errors)
            for path in files:
                errors.extend(validate_docs.validate_file(path, check_fragments=True))

            self.assertEqual(errors, [])

    def test_reports_structure_links_fences_and_images(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "bad.md"
            path.write_text(
                "## Bad start\n\n#### Skipped level\n\n"
                "[Missing](missing.md)\n\n![](image.png)\n\n```text\nopen\n",
                encoding="utf-8",
            )

            errors = validate_docs.validate_file(path, check_fragments=False)
            joined = "\n".join(errors)

            self.assertIn("first heading must be level one", joined)
            self.assertIn("expected one level-one heading, found 0", joined)
            self.assertIn("heading level skips", joined)
            self.assertIn("broken local link", joined)
            self.assertIn("image needs alternative text", joined)
            self.assertIn("unclosed fenced code block", joined)

    def test_reports_missing_fragment(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "page.md"
            path.write_text(
                "# Page\n\nSee [missing section](#not-present).\n",
                encoding="utf-8",
            )

            errors = validate_docs.validate_file(path, check_fragments=True)

            self.assertTrue(any("missing heading target" in error for error in errors))

    def test_allows_confirmed_decorative_image(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "page.md"
            path.write_text("# Page\n\n![](divider.svg)\n", encoding="utf-8")

            errors = validate_docs.validate_file(
                path, check_fragments=False, allow_empty_alt=True
            )

            self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()

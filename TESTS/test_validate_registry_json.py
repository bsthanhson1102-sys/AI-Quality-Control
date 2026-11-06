import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parents[1] / "TOOLS"
sys.path.insert(0, str(TOOLS_DIR))
from validate_registry_json import validate_document


VALID = {
    "skills": [
        {
            "id": "coding-master",
            "status": "active",
            "path": "SKILLS/coding-master/SKILL.md",
        }
    ]
}


class ValidateDocumentTests(unittest.TestCase):
    def test_valid_document(self):
        self.assertEqual(validate_document(VALID), [])

    def test_duplicate_ids(self):
        doc = {
            "skills": VALID["skills"]
            + [{**VALID["skills"][0], "path": "other.md"}]
        }
        self.assertTrue(any("duplicates" in error for error in validate_document(doc)))

    def test_invalid_status(self):
        doc = {"skills": [{**VALID["skills"][0], "status": "unknown"}]}
        self.assertTrue(any("status" in error for error in validate_document(doc)))

    def test_missing_path(self):
        doc = {"skills": [{"id": "x", "status": "active"}]}
        self.assertTrue(any("path" in error for error in validate_document(doc)))

    def test_missing_skills_array(self):
        self.assertTrue(any("skills" in error for error in validate_document({})))

    def test_non_object_top_level(self):
        self.assertTrue(any("Top-level" in error for error in validate_document([])))

    def test_malformed_record(self):
        doc = {"skills": [None]}
        self.assertTrue(any("must be an object" in error for error in validate_document(doc)))

    def test_empty_or_whitespace_id_rejected(self):
        doc = {"skills": [{"id": "  ", "status": "active", "path": "x.md"}]}
        self.assertTrue(any(".id" in error for error in validate_document(doc)))

    def test_boolean_is_not_a_valid_status(self):
        doc = {"skills": [{"id": "x", "status": True, "path": "x.md"}]}
        self.assertTrue(any("status" in error for error in validate_document(doc)))


class CliTests(unittest.TestCase):
    def run_cli(self, content):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry.json"
            path.write_text(content, encoding="utf-8")
            script = TOOLS_DIR / "validate_registry_json.py"
            return subprocess.run(
                [sys.executable, str(script), str(path)],
                text=True,
                capture_output=True,
                check=False,
            )

    def test_cli_valid_input(self):
        result = self.run_cli(json.dumps(VALID))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("VALID: 1", result.stdout)

    def test_cli_malformed_json(self):
        result = self.run_cli('{"skills": [}')
        self.assertEqual(result.returncode, 2)
        self.assertIn("Malformed JSON", result.stderr)

    def test_cli_invalid_registry(self):
        doc = {"skills": [{"id": "x", "status": "bad", "path": ""}]}
        result = self.run_cli(json.dumps(doc))
        self.assertEqual(result.returncode, 1)
        self.assertIn("status", result.stderr)
        self.assertIn("path", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)

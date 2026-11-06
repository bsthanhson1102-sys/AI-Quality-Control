import json
import tempfile
import unittest
from pathlib import Path

import t09_isolation_harness as harness


class IsolationHarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.bundle = Path(self.temp.name) / "bundle"
        harness.prepare(self.bundle)

    def make_valid_evidence(self):
        (self.bundle / "artifacts" / "solution.py").write_text("print('ok')\n", encoding="utf-8")
        transcript = self.bundle / "transcript.md"
        transcript.write_text("Fresh isolated evaluation transcript.\n", encoding="utf-8")
        evidence = dict(harness.TEMPLATE)
        evidence["fresh_conversation_created"] = True
        evidence["prior_conversation_context_injected"] = False
        evidence["registry_or_skill_files_attached"] = False
        evidence["github_connector_available"] = False
        evidence["web_or_browser_retrieval_available"] = False
        evidence["network_retrieval_available"] = False
        evidence["source_access_mode"] = "tools_not_provided"
        evidence["registry_access_result"] = "tool_not_available"
        evidence["skill_access_result"] = "tool_not_available"
        evidence["task_prompt_sha256"] = harness.sha256_file(self.bundle / "prompt.md")
        evidence["transcript_sha256"] = harness.sha256_file(transcript)
        evidence["artifact_files"] = ["artifacts/solution.py"]
        evidence["test_exit_code"] = 0
        evidence["tests_run"] = 2
        evidence["tests_passed"] = 2
        evidence["tests_failed"] = 0
        evidence["tests_errored"] = 0
        evidence["human_attestation"] = {
            "evaluator": "test",
            "attests_fresh_session_and_no_prior_context": True,
            "attests_no_registry_or_skill_payload_was_injected": True,
            "notes": "test fixture"
        }
        (self.bundle / "evidence.json").write_text(
            json.dumps(evidence), encoding="utf-8"
        )

    def test_prepare_creates_minimal_bundle_without_registry_or_skill_files(self):
        names = {p.name for p in self.bundle.iterdir()}
        self.assertEqual(names, {"prompt.md", "evidence.template.json", "README.txt", "artifacts"})
        self.assertFalse((self.bundle / "REGISTRY").exists())
        self.assertFalse((self.bundle / "SKILLS").exists())

    def test_valid_evidence_passes_structure_check(self):
        self.make_valid_evidence()
        self.assertEqual(harness.verify(self.bundle), 0)

    def test_missing_evidence_is_blocked(self):
        self.assertEqual(harness.verify(self.bundle), 2)

    def test_prior_context_true_fails(self):
        self.make_valid_evidence()
        path = self.bundle / "evidence.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["prior_conversation_context_injected"] = True
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(harness.verify(self.bundle), 1)

    def test_registry_payload_attached_fails(self):
        self.make_valid_evidence()
        path = self.bundle / "evidence.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["registry_or_skill_files_attached"] = True
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(harness.verify(self.bundle), 1)

    def test_transcript_hash_mismatch_fails(self):
        self.make_valid_evidence()
        path = self.bundle / "evidence.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["transcript_sha256"] = "0" * 64
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(harness.verify(self.bundle), 1)

    def test_inconsistent_test_counts_fail(self):
        self.make_valid_evidence()
        path = self.bundle / "evidence.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["tests_passed"] = 1
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(harness.verify(self.bundle), 1)

    def test_artifact_path_traversal_fails(self):
        self.make_valid_evidence()
        path = self.bundle / "evidence.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["artifact_files"] = ["../outside.py"]
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(harness.verify(self.bundle), 1)

    def test_transcript_path_traversal_fails(self):
        self.make_valid_evidence()
        path = self.bundle / "evidence.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["transcript_file"] = "../outside.md"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertEqual(harness.verify(self.bundle), 1)


if __name__ == "__main__":
    unittest.main()

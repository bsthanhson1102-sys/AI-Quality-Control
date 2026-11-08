import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from test_release_gate import BASE
from check_release_candidates import inspect

class TestCandidateIntegration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "RELEASES" / "pending").mkdir(parents=True)
        (self.root / "RELEASES" / "approvals").mkdir(parents=True)

    def tearDown(self):
        self.tmp.cleanup()

    def write_candidate(self, ledger=None):
        p = self.root / "RELEASES" / "pending" / "sample.json"
        p.write_text(json.dumps(ledger or BASE), encoding="utf-8")

    def write_approval(self, ledger=None):
        ledger = ledger or BASE
        a = {"artifact_sha256": hashlib.sha256(ledger["artifact"].encode()).hexdigest(),
             "decision": "APPROVED", "reviewer": "Operator", "evidence": "Documented manual review",
             "domain_review": "PASS", "technical_review": "PASS"}
        (self.root / "RELEASES" / "approvals" / "sample.json").write_text(json.dumps(a), encoding="utf-8")

    def test_no_candidates(self):
        self.assertEqual(inspect(self.root)["decision"], "NO_CANDIDATES")

    def test_missing_approval_blocks(self):
        self.write_candidate()
        self.assertEqual(inspect(self.root)["decision"], "BLOCKED")

    def test_valid_approval_record(self):
        self.write_candidate()
        self.write_approval()
        self.assertEqual(inspect(self.root)["decision"], "APPROVAL_RECORDS_ACCEPTED")

    def test_changed_artifact_blocks(self):
        self.write_approval()
        ledger = copy.deepcopy(BASE)
        ledger["artifact"] += " modified"
        self.write_candidate(ledger)
        self.assertEqual(inspect(self.root)["decision"], "BLOCKED")

    def test_unresolved_major_blocks(self):
        ledger = copy.deepcopy(BASE)
        ledger["recheck"]["M1"] = "UNRESOLVED"
        self.write_candidate(ledger)
        self.write_approval(ledger)
        self.assertEqual(inspect(self.root)["decision"], "BLOCKED")

    def test_invalid_json_blocks(self):
        (self.root / "RELEASES" / "pending" / "sample.json").write_text("{")
        self.assertEqual(inspect(self.root)["decision"], "BLOCKED")

if __name__ == "__main__":
    unittest.main()

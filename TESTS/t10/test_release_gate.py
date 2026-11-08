import copy
import unittest
from release_gate import decide

BASE = {
    "brief": "Facebook post about rhinoplasty",
    "candidate": "A generic hook with no useful payoff.",
    "artifact": "A specific insight with a useful payoff.",
    "critic": [{"id": "M1", "severity": "MAJOR", "passage": "generic hook", "reason": "No specific payoff"}],
    "editor_changes": [{"finding_id": "M1", "before": "generic hook", "after": "specific insight"}],
    "recheck": {"M1": "RESOLVED"},
    "final_auditor": {"scores": [23, 19, 14, 14, 9, 9, 5],
                      "technical_gate": "PASS", "domain_gate": "PASS",
                      "evidence_complete": True, "regression_clear": True},
    "rounds": 2
}
class TestReleaseGate(unittest.TestCase):
    def check_block(self, change):
        ledger = copy.deepcopy(BASE)
        change(ledger)
        self.assertEqual(decide(ledger)["decision"], "NOT PASS")
    def test_valid_schema_is_not_approval(self):
        self.assertEqual(decide(BASE)["decision"], "SCHEMA_ACCEPTED_REVIEW_REQUIRED")
    def test_missing_critic(self):
        self.check_block(lambda x: x.pop("critic"))
    def test_missing_editor(self):
        self.check_block(lambda x: x.pop("editor_changes"))
    def test_unresolved_major(self):
        self.check_block(lambda x: x["recheck"].update(M1="UNRESOLVED"))
    def test_missing_final_auditor(self):
        self.check_block(lambda x: x.pop("final_auditor"))
    def test_low_score(self):
        self.check_block(lambda x: x["final_auditor"].update(scores=[20, 16, 10, 12, 7, 8, 5]))
    def test_five_rounds(self):
        self.check_block(lambda x: x.update(rounds=5))
    def test_domain_not_run(self):
        self.check_block(lambda x: x["final_auditor"].update(domain_gate="NOT RUN"))
    def test_fake_edit(self):
        self.check_block(lambda x: x.update(artifact="No change to original"))
    def test_blank_finding(self):
        self.check_block(lambda x: x["critic"][0].update(passage=""))
    def test_finding_not_in_candidate(self):
        self.check_block(lambda x: x["critic"][0].update(passage="not actually present"))
    def test_invalid_score_bool(self):
        self.check_block(lambda x: x["final_auditor"].update(scores=[True, 19, 14, 14, 9, 9, 5]))
if __name__ == "__main__":
    unittest.main()

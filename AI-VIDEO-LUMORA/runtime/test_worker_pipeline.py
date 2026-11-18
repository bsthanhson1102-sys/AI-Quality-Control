import unittest
from worker_pipeline import execute, score_review, MAX_ROUNDS

def auditor(brief, artifact, findings):
    return {"scores": [95] * 7, "findings": []}

class WorkerPipelineTests(unittest.TestCase):
    def test_weighted_score(self):
        self.assertEqual(score_review({"scores": [100, 0, 0, 0, 0, 0, 0]})["score"], 25)
    def test_critical_blocks_high_score(self):
        self.assertFalse(score_review({"scores": [100]*7, "findings": [{"severity": "Critical", "code": "UNSAFE"}]})["pass"])
    def test_major_blocks_high_score(self):
        self.assertFalse(score_review({"scores": [100]*7, "findings": [{"severity": "Major", "code": "NO_VIDEO"}]})["pass"])
    def test_under_90_blocks(self):
        self.assertFalse(score_review({"scores": [89]*7})["pass"])
    def test_clean_pass(self):
        r = execute({}, lambda b: "artifact", lambda b,a: [], lambda b,a,f: a, lambda b,a: True, auditor)
        self.assertEqual((r["status"], r["rounds_used"]), ("PASS", 1))
    def test_regression_blocks(self):
        r = execute({}, lambda b: "artifact", lambda b,a: [], lambda b,a,f: a, lambda b,a: False, auditor)
        self.assertEqual((r["status"], r["rounds_used"]), ("NOT_PASS", MAX_ROUNDS))
    def test_four_round_cap(self):
        r = execute({}, lambda b: "artifact", lambda b,a: [{"severity":"Major","code":"X"}], lambda b,a,f: a, lambda b,a: True, auditor)
        self.assertEqual(len(r["history"]), 4)
    def test_editor_can_fix(self):
        r = execute({}, lambda b: 0, lambda b,a: [] if a == 1 else [{"severity":"Major","code":"FIX"}], lambda b,a,f: a+1, lambda b,a: True, auditor)
        self.assertEqual((r["status"], r["rounds_used"]), ("PASS", 2))
    def test_no_publish(self):
        r = execute({"publish": True}, lambda b: "artifact", None, None, None, None)
        self.assertEqual(r["status"], "BLOCKED")
    def test_no_credits(self):
        r = execute({"buy_credits": True}, lambda b: "artifact", None, None, None, None)
        self.assertEqual(r["status"], "BLOCKED")
    def test_missing_scores_rejected(self):
        with self.assertRaises(ValueError):
            score_review({"scores": [90]})
    def test_independence_not_claimed(self):
        r = execute({}, lambda b: "artifact", lambda b,a: [], lambda b,a,f: a, lambda b,a: True, auditor)
        self.assertFalse(r["independent_agents_verified"])

if __name__ == "__main__":
    unittest.main()

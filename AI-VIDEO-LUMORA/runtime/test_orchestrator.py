import tempfile
import unittest
from orchestrator import run, MAX_ROUNDS

BRIEF = {"subject": "Lumora filler thái dương", "realistic_video": True}

class PilotTests(unittest.TestCase):
    def test_no_generator_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            r = run(BRIEF, d)
            self.assertEqual(r["status"], "BLOCKED")
            self.assertFalse(r["video_created"])
    def test_no_spending(self):
        with tempfile.TemporaryDirectory() as d:
            r = run(dict(BRIEF, buy_credits=True), d, {"realistic_video_generator": True})
            self.assertEqual(r["findings"], ["AUTHORIZATION_REQUIRED"])
    def test_no_publish(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(run(dict(BRIEF, publish=True), d)["status"], "BLOCKED")
    def test_no_fake_render(self):
        with tempfile.TemporaryDirectory() as d:
            r = run(BRIEF, d, {"realistic_video_generator": True})
            self.assertEqual(r["status"], "NOT_PASS")
            self.assertIn("NO_RENDERED_ARTIFACT", r["findings"])
    def test_idempotence(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(run(BRIEF, d), run(BRIEF, d))
    def test_no_fake_score(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(run(BRIEF, d)["evidence"][-1]["result"]["qc_score"])
    def test_round_limit(self):
        self.assertEqual(MAX_ROUNDS, 4)

if __name__ == "__main__":
    unittest.main()

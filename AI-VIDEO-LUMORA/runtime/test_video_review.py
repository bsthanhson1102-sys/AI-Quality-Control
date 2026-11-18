import tempfile
import unittest
from pathlib import Path
from video_review import review_candidate

class VideoIntegrationTests(unittest.TestCase):
    def test_missing_video_not_pass(self):
        with tempfile.TemporaryDirectory() as d:
            r = review_candidate({}, str(Path(d) / "missing.mp4"))
            self.assertEqual(r["status"], "NOT_PASS")
            self.assertEqual(r["rounds_used"], 4)
            self.assertIn("MISSING_VIDEO", [f["code"] for f in r["history"][0]["findings"]])
    def test_missing_consent_blocks_even_with_high_score(self):
        with tempfile.TemporaryDirectory() as d:
            r = review_candidate({}, str(Path(d) / "missing.mp4"), [100]*7, medical_review=True)
            self.assertEqual(r["status"], "NOT_PASS")
            self.assertIn("CONSENT_NOT_VERIFIED", [f["code"] for f in r["history"][0]["findings"]])
    def test_no_medical_review_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            r = review_candidate({}, str(Path(d) / "missing.mp4"), [100]*7, consent_verified=True)
            self.assertIn("MEDICAL_VISUAL_REVIEW_MISSING", [f["code"] for f in r["history"][0]["findings"]])
    def test_publish_blocked(self):
        r = review_candidate({"publish": True}, "missing.mp4")
        self.assertEqual(r["status"], "BLOCKED")

if __name__ == "__main__":
    unittest.main()

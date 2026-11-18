"""Regression cases discovered during 2026-11-19 runtime review."""
import unittest
from orchestrator import inspect_video
from worker_pipeline import score_review


class EdgeCases(unittest.TestCase):
    def test_nan_rejected(self):
        with self.assertRaises(ValueError):
            score_review({"scores": [float("nan")] * 7})

    def test_positive_infinity_rejected(self):
        with self.assertRaises(ValueError):
            score_review({"scores": [float("inf")] * 7})

    def test_negative_infinity_rejected(self):
        with self.assertRaises(ValueError):
            score_review({"scores": [float("-inf")] * 7})

    def test_none_video_path_handled(self):
        self.assertEqual(inspect_video(None)["reason"], "INVALID_VIDEO_PATH")

    def test_empty_video_path_handled(self):
        self.assertEqual(inspect_video("")["reason"], "INVALID_VIDEO_PATH")


if __name__ == "__main__":
    unittest.main()

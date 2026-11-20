import unittest
from camera_catalog import CAMERA_TERMS, COMBOS, GROUPS, build_camera_prompt, validate_catalog

class CameraCatalogTests(unittest.TestCase):
    def test_120_unique_terms(self):
        self.assertTrue(validate_catalog())
        self.assertEqual(len(CAMERA_TERMS), 120)
    def test_11_groups(self):
        self.assertEqual(len(GROUPS), 11)
    def test_5_combos(self):
        self.assertEqual(len(COMBOS), 5)
    def test_valid_prompt(self):
        p = build_camera_prompt("A clinic corridor", ["slow push in", "shallow depth of field"], medical=True)
        self.assertIn("slow push in", p["prompt"])
        self.assertFalse(p["rendered"])
        self.assertTrue(p["medical_review_required"])
    def test_too_many_moves(self):
        with self.assertRaises(ValueError):
            build_camera_prompt("Scene", ["pan left", "tilt up", "zoom in"])
    def test_unknown_move(self):
        with self.assertRaises(ValueError):
            build_camera_prompt("Scene", ["teleport camera"])
    def test_empty_scene(self):
        with self.assertRaises(ValueError):
            build_camera_prompt("", ["pan left"])
    def test_distortion_blocked_for_medical(self):
        with self.assertRaises(ValueError):
            build_camera_prompt("Patient", ["fisheye lens"], medical=True)
    def test_prompt_not_render(self):
        self.assertFalse(build_camera_prompt("Clinic", ["gimbal shot"])["rendered"])

if __name__ == "__main__":
    unittest.main()

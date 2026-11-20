import unittest
from tool_adapters import adapt_shot

class ToolAdaptersTests(unittest.TestCase):
    def test_capcut_keyframes(self):
        r = adapt_shot("Clinic", ["slow push in"], "capcut")
        self.assertEqual(r["mode"], "timeline_plan")
        self.assertIn("keyframes", r["instructions"][0])
        self.assertFalse(r["capability_verified"])
    def test_canva_plan(self):
        r = adapt_shot("Clinic", ["pan left"], "canva")
        self.assertEqual(r["mode"], "timeline_plan")
    def test_ai_prompt(self):
        r = adapt_shot("Clinic", ["slow push in"], "kling")
        self.assertEqual(r["mode"], "prompt")
    def test_orbit_requires_more_than_2d(self):
        r = adapt_shot("Clinic", ["orbit 360"], "capcut")
        self.assertTrue(r["limitations"])
    def test_unsupported_tool(self):
        with self.assertRaises(ValueError):
            adapt_shot("Clinic", ["pan left"], "unknown")
    def test_medical_guard(self):
        with self.assertRaises(ValueError):
            adapt_shot("Face", ["fisheye lens"], "canva", medical=True)

if __name__ == "__main__":
    unittest.main()

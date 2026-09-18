import unittest

from src.motion_sensor import motion_detected


class MotionDetectedTests(unittest.TestCase):
    def test_detects_change_at_threshold(self):
        self.assertTrue(motion_detected(100, 120, threshold=20))

    def test_ignores_sensor_noise_below_threshold(self):
        self.assertFalse(motion_detected(100, 112, threshold=20))

    def test_detects_motion_in_both_directions(self):
        self.assertTrue(motion_detected(120, 100, threshold=20))

    def test_rejects_non_positive_threshold(self):
        with self.assertRaisesRegex(ValueError, "threshold must be greater than zero"):
            motion_detected(100, 101, threshold=0)


if __name__ == "__main__":
    unittest.main()

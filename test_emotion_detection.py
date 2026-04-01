# test_emotion_detection.py

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Unit tests for emotion_detector function."""

    def test_joy(self):
        """Test for joy emotion."""
        text = "I am glad this happened"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Test for anger emotion."""
        text = "I am really mad about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Test for disgust emotion."""
        text = "I feel disgusted just hearing about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Test for sadness emotion."""
        text = "I am so sad about this"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Test for fear emotion."""
        text = "I am really afraid that this will happen"
        result = emotion_detector(text)
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()

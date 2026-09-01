import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestJoy(unittest.TestCase):
    def test_joy(self):
        result_joy = emotion_detector("I am glad this happened")
        emotion_joy = result_joy['dominant_emotion']
        self.assertEqual(emotion_joy, 'joy')

class TestAnger(unittest.TestCase):
    def test_anger(self):
        result_anger = emotion_detector("I am really mad about this")
        emotion_anger = result_anger['dominant_emotion']
        self.assertEqual(emotion_anger, 'anger')

class TestDisgust(unittest.TestCase):
    def test_disgust(self):
        result_disgust = emotion_detector("I feel disgusted just hearing about this")
        emotion_disgust = result_disgust['dominant_emotion']
        self.assertEqual(emotion_disgust, 'disgust')

class TestSadness(unittest.TestCase):
    def test_sadness(self):
        result_sadness = emotion_detector("I am so sad about this")
        emotion_sadness = result_sadness['dominant_emotion']
        self.assertEqual(emotion_sadness, 'sadness')

class TestFear(unittest.TestCase):
    def test_fear(self):
        result_fear = emotion_detector("I am really afraid that this will happen")
        emotion_fear = result_fear['dominant_emotion']
        self.assertEqual(emotion_fear, 'fear')

if __name__ == '__main__':
    unittest.main()
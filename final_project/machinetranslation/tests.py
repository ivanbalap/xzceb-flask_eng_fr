import unittest
from translator import englishToFrench, frenchToEnglish

ENGLISH_TEXT_1="Hello"
FRENCH_TEXT_1="Bonjour"

ENGLISH_TEXT_2="Thank you"
FRENCH_TEXT_2="Mercy"

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(ENGLISH_TEXT_1),FRENCH_TEXT_1)
        self.assertNotEqual(englishToFrench(ENGLISH_TEXT_2),FRENCH_TEXT_1)

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(FRENCH_TEXT_1),ENGLISH_TEXT_1)
        self.assertNotEqual(frenchToEnglish(FRENCH_TEXT_2),ENGLISH_TEXT_1)

unittest.main()
import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):


    def test_phrase(self):
        phrase = "hello world"
        translator = PigLatin(phrase)
        self.assertEqual(translator.get_phrase(),phrase)







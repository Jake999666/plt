import unittest
from tokenize import triple_quoted

from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):


    def test_phrase(self):
        phrase = "hello world"
        translator = PigLatin(phrase)
        self.assertEqual(translator.get_phrase(),phrase)

    def test_empty_string(self):
        phrase = ""
        translator = PigLatin(phrase)
        self.assertEqual(translator.translate(), "nil")

    def test_starting_nay(self):
        phrase = "any"
        translator = PigLatin(phrase)
        self.assertEqual(translator.translate(),"anynay")

    def test_ending_yay(self):
        phrase = "apple"
        translator = PigLatin(phrase)
        self.assertEqual(translator.translate(),"appleyay")

    def test_ending_ay(self):
        phrase = "ask"
        translator = PigLatin(phrase)
        self.assertEqual(translator.translate(),"askay")



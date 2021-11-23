import unittest
import vowel_counter

class TestVowelCount(unittest.TestCase):
    def test_vowel_count(self):
        self.assertEqual(vowel_counter.count_vowels('maisy'),2)


if __name__== 'main':
    unittest.main()
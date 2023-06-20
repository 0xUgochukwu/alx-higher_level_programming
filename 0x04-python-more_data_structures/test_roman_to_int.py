#!/usr/bin/python3

import unittest


roman_to_int = __import__('12-roman_to_int').roman_to_int


class RomanToIntTestCase(unittest.TestCase):
    def test_valid_roman_numerals(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_invalid_roman_numerals(self):
        self.assertEqual(roman_to_int('ABC'), 0)
        self.assertEqual(roman_to_int(None), 0)
        self.assertEqual(roman_to_int(123), 0)

if __name__ == '__main__':
    unittest.main()

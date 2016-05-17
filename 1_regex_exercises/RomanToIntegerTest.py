'''Test suite for roman_to_int'''
from unittest import TestCase
from roman_to_int import roman_to_int

class RomanToIntTestCase(TestCase):
	'''Test case for roman_to_int.'''

	def test_invalid_input(self):
		'''Test for invalid input.'''
		self.assertEqual(roman_to_int('MCMXXL'), 'Invalid Roman Numeral')

	def test_thousands(self):
		'''Test for thousands.'''
		self.assertEqual(roman_to_int('MCMLXXX'), 1980)

	def test_inverted(self):
		'''Test for switched order.'''
		self.assertEqual(roman_to_int('MCMXCIX'), 1999)

'''Test suite for roman_to_int'''
from unittest import TestCase
from roman_to_int import roman_to_int

class RomanToIntTestCase(TestCase):
	'''Test case for roman_to_int.'''

	def test_thousands(self):
		'''Test for thousands.'''
		self.assertEqual(roman_to_int('MDCL'), 1650)

	def test_inverted(self):
		'''Test for switched order.'''
		self.assertEqual(roman_to_int('MCMXCIX'), 1999)

"""
A set of simple, quick tests for the purposes of testing HTML output.
"""

from django.test import TestCase

class MathTest(TestCase):
	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		self.failUnlessEqual(1 + 1, 2)

	def test_basic_subtraction(self):
		"""
		Tests that 4 - 2 always equals 2.
		"""
		self.failUnlessEqual(4 - 2, 2)

	def test_basic_multiplication(self):
		"""
		Tests that 2 * 2 always equals 4.
		"""
		self.failUnlessEqual(2 * 2, 4)

	def test_basic_division(self):
		"""
		Tests that 2 / 2 always equals 1.
		"""
		self.failUnlessEqual(2 / 2, 1)

"""
A set of simple, quick tests for the purposes of testing HTML output.
"""

from django.test import TestCase

class StringTest(TestCase):
	def test_basic_concatenation(self):
		"""
		Tests that "a" + "b" always equals "ab".
		"""
		self.failUnlessEqual(1 + 1, 2)

	def test_basic_slicing(self):
		"""
		Tests that slicing the first 3 characters of "Hello" always "Hel".
		"""
		self.failUnlessEqual("Hello"[:3], "Hel")
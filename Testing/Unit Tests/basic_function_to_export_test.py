#!/usr/bin/env python3

from basic_function_to_export import rearrange_name
import unittest  # import test module for testing

# The unittest module providesa TestCase class with a number of testing methods built-in

class TestRearrange(unittest.TestCase): # this is our custom class that inherits from TestCase
	def test_basic(self):
		testcase = "Smith, John"
		expected = "John Smith"
		self.assertEqual(rearrange_name(testcase), expected)

#unittest.main() to run the test
unittest.main()


# in terminal, "chmod +x basic_function_to_export.py"
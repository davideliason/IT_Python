#!/usr/bin/env python3

import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
	def test_valid(self):
		self.assertEqual(validate_user("validuser",3), True)
	def test_too_short(self):
		self.assertEqual(validate_user("inv", 5), False)
	def test_invalid_characters(self):
		self.assertEqual(validate_user("invalid_user",1), False)
	def test_invalid_minlen(self):
		self.assertRaises(ValueError, validate_user, "user",-1)
		#assertRaises method is different than assertEqual method
		#first, error we expect the function to raise,
		#then, function name and any parameters to be passed
unittest.main()

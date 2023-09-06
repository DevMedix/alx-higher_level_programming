#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_basic(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-4, -2, -1, -5]), -1)

    def test_max_integer_mixed(self):
        self.assertEqual(max_integer([-4, 5, -1, 0]), 5)

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_single_element(self):
        self.assertEqual(max_integer([42]), 42)

#!/usr/bin/python3
"""Unittest for max_integer([..])
i"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_at_end(self):
        """Test for max at the end"""
        max_at_end = [3, 4, 5, 6]
        self.assertEqual(max_integer(max_at_end), 6)

    def test_max_at_begginning(self):
        """Test for max at the beginning"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_one_negative_in_list(self):
        """Test for one negative number in the list"""
        one_negative = [-3, 3, 2, 1]
        self.assertEqual(max_integer(one_negative), 3)

    def test_max_in_middle(self):
        """Test for max in the middle"""
        max_in_middle = [6, 8, 10, 4, 7]
        self.assertEqual(max_integer(max_in_middle), 10)

    def test_all_negative(self):
        all_negative = [-2, -4, -6, -8]
        self.assertEqual(max_integer(all_negative), -2)

    def test_list_is_empty(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element(self):
        one_number = [7]
        self.assertEqual(max_integer(one_number), 7)
    
if __name__ == '__main__':
    unittest.main()

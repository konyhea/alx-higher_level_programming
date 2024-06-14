#!/usr/bin/python3
''' unittest for max_integer '''
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_ordered(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_integer_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer_strings(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_max_integer_negative_int(self):
        self.assertEqual(max_integer([-1, -9, -8]), -1)

    def test_max_integer_floats(self):
        self.assertEqual(max_integer([-1.7, -9.9, -8]), -1.7)

    def test_max_integer_singular(self):
        self.assertEqual(max_integer([1]), 1)
    
if __name__ == "__main__":
    unittest.main()

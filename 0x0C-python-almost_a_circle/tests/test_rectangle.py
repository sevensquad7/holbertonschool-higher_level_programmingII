#!/usr/bin/python3
'''File Test class Rectangle'''


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Class test of Rectangle'''

    def test_id(self):
        '''Test id'''
        r1 = Rectangle(10, 2)
        id = r1.id
        self.assertEqual(id, 2)
        r3 = Rectangle(10, 2, 0, 0, 10)
        id = r3.id
        self.assertEqual(id, 10)

    def test_validate(self):
        '''Validate integer'''
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(TypeError, Rectangle, "q", 3)
        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, -2, 6)
        self.assertRaises(ValueError, Rectangle, 9, 6, 1, -1)

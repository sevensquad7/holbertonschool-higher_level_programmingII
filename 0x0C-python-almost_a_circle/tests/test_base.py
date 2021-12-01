#!/usr/bin/python3
'''File to test class Base'''


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Create class to test'''

    def test_id(self):
        b1 = Base()
        id = b1.id
        self.assertEqual(id, 1)

        b4 = Base(12)
        id = b4.id
        self.assertEqual(id, 12)

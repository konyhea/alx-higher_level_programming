#!/usr/bin/python3
""" Module for Base test using unit tests."""
import unittest
from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square


class TestBase(unittest.TestCase):
    """Base class test."""

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_nb_object_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_objects_initialized_zero(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

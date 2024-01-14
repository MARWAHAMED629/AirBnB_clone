#!/usr/bin/python3
"""
Module for the BaseModel unittest
"""
import models
import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """
    Unittest for BaseModel
    """

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """
        Test for an init.
        """
        my_mdl = BaseModel()

        self.assertIsNotNone(my_mdl.id)
        self.assertIsNotNone(my_mdl.created_at)
        self.assertIsNotNone(my_mdl.updated_at)

    def test_save(self):
        """
        Tests to save the method.
        """
        my_mdl = BaseModel()

        initial_updated_at = my_mdl.updated_at

        current_updated_at = my_mdl.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Tests for the to_dict method.
        """
        my_mdl = BaseModel()

        mdl_dic = my_mdl.to_dict()

        self.assertIsInstance(mdl_dic, dict)

        self.assertEqual(mdl_dic["__class__"], 'BaseModel')
        self.assertEqual(mdl_dic['id'], my_mdl.id)
        self.assertEqual(mdl_dic['created_at'], my_mdl.created_at.isoformat())
        self.assertEqual(mdl_dic["updated_at"], my_mdl.updated_at.isoformat())

    def test_str(self):
        """
        Test for the string representation.
        """
        my_mdl = BaseModel()

        self.assertTrue(str(my_mdl).startswith('[BaseModel]'))

        self.assertIn(my_mdl.id, str(my_mdl))

        self.assertIn(str(my_mdl.__dict__), str(my_mdl))


if __name__ == "__main__":
    unittest.main()

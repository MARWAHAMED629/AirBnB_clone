#!/usr/bin/python3
"""
Module for the FilStorage unittest
"""
import os
import json
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    Unittests for testing methods of the FileStorage class.
    """

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        my_model = BaseModel()
        my_ur = User()
        my_st = State()
        _place = Place()
        my_cy = City()
        ame = Amenity()
        my_rw = Review()
        models.storage.new(my_model)
        models.storage.new(my_ur)
        models.storage.new(my_st)
        models.storage.new(my_place)
        models.storage.new(my_cy)
        models.storage.new(ame)
        models.storage.new(my_rw)
        self.assertIn("BaseModel." + my_model.id, models.storage.all().keys())
        self.assertIn(my_model, models.storage.all().values())
        self.assertIn("User." + my_ur.id, models.storage.all().keys())
        self.assertIn(my_ur, models.storage.all().values())
        self.assertIn("State." + my_st.id, models.storage.all().keys())
        self.assertIn(my_st, models.storage.all().values())
        self.assertIn("Place." + _place.id, models.storage.all().keys())
        self.assertIn(_place, models.storage.all().values())
        self.assertIn("City." + my_cy.id, models.storage.all().keys())
        self.assertIn(my_cy, models.storage.all().values())
        self.assertIn("Amenity." + ame.id, models.storage.all().keys())
        self.assertIn(ame, models.storage.all().values())
        self.assertIn("Review." + my_rw.id, models.storage.all().keys())
        self.assertIn(my_rw, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        my_model = BaseModel()
        my_ur = User()
        my_st = State()
        _place = Place()
        my_cy = City()
        ame = Amenity()
        my_rw = Review()
        models.storage.new(my__model)
        models.storage.new(my_ur)
        models.storage.new(my_st)
        models.storage.new(_place)
        models.storage.new(my_cy)
        models.storage.new(ame)
        models.storage.new(my_rw)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + my_model.id, save_text)
            self.assertIn("User." + my_ur.id, save_text)
            self.assertIn("State." + my_st.id, save_text)
            self.assertIn("Place." + _place.id, save_text)
            self.assertIn("City." + my_cy.id, save_text)
            self.assertIn("Amenity." + ame.id, save_text)
            self.assertIn("Review." + my_rw.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        my_model = BaseModel()
        my_ur = User()
        my_st = State()
        _place = Place()
        my_cy = City()
        ame = Amenity()
        my_rw = Review()
        models.storage.new(my_model)
        models.storage.new(my_ur)
        models.storage.new(my_st)
        models.storage.new(_place)
        models.storage.new(my_cy)
        models.storage.new(ame)
        models.storage.new(my_rw)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + my_model.id, objs)
        self.assertIn("User." + my_ur.id, objs)
        self.assertIn("State." + my_st.id, objs)
        self.assertIn("Place." + _place.id, objs)
        self.assertIn("City." + my_cy.id, objs)
        self.assertIn("Amenity." + ame.id, objs)
        self.assertIn("Review." + my_rw.id, objs)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

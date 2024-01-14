#!/usr/bin/python3
"""
Module for THE User class
"""
import models
import os
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the User class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_ids(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_two_users_different_created_at(self):
        u1 = User()
        sleep(0.05)
        u2 = User()
        self.assertLess(u1.created_at, u2.created_at)

    def test_two_users_different_updated_at(self):
        u1 = User()
        sleep(0.05)
        u2 = User()
        self.assertLess(u1.updated_at, u2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        u1 = User()
        u1.id = "777777"
        u1.created_at = u1.updated_at = my_date
        u1_str = u1.__str__()
        self.assertIn("[User] (777777)", u1_str)
        self.assertIn("'id': '777777'", u1_str)
        self.assertIn("'created_at': " + my_date_repr, u1_str)
        self.assertIn("'updated_at': " + my_date_repr, u1_str)

    def test_args_unused(self):
        u1 = User(None)
        self.assertNotIn(None, u1.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        u1 = User(id="777", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(u1.id, "777")
        self.assertEqual(u1.created_at, my_date)
        self.assertEqual(u1.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        ur = User()
        sleep(0.05)
        first_updated_at = ur.updated_at
        ur.save()
        self.assertLess(first_updated_at, ur.updated_at)

    def test_two_saves(self):
        ur = User()
        sleep(0.05)
        first_updated_at = ur.updated_at
        ur.save()
        second_updated_at = ur.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        ur.save()
        self.assertLess(second_updated_at, ur.updated_at)

    def test_save_with_arg(self):
        ur = User()
        with self.assertRaises(TypeError):
            ur.save(None)

    def test_save_updates_file(self):
        ur = User()
        ur.save()
        userid = "User." + ur.id
        with open("file.json", "r") as f:
            self.assertIn(userid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for the testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        ur = User()
        self.assertIn("id", ur.to_dict())
        self.assertIn("created_at", ur.to_dict())
        self.assertIn("updated_at", ur.to_dict())
        self.assertIn("__class__", ur.to_dict())

    def test_to_dict_contains_added_attributes(self):
        ur = User()
        ur.middle_name = "Holberton"
        ur.my_number = 98
        self.assertEqual("Holberton", ur.middle_name)
        self.assertIn("my_number", ur.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        ur = User()
        ur_dict = ur.to_dict()
        self.assertEqual(str, type(ur_dict["id"]))
        self.assertEqual(str, type(ur_dict["created_at"]))
        self.assertEqual(str, type(ur_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        ur = User()
        ur.id = "777777"
        ur.created_at = ur.updated_at = my_date
        tdict = {
            'id': '777777',
            '__class__': 'User',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(ur.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        ur = User()
        self.assertNotEqual(ur.to_dict(), ur.__dict__)

    def test_to_dict_with_arg(self):
        ur = User()
        with self.assertRaises(TypeError):
            ur.to_dict(None)


if __name__ == "__main__":
    unittest.main()

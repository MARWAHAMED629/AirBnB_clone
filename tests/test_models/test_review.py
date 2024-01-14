#!/usr/bin/python3
"""
Module for testing THE Review.
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """
    Unittests for THE testing an instantiation of the Review class.
    """

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_class_attribute(self):
        rw = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rw))
        self.assertNotIn("place_id", rw.__dict__)

    def test_user_id_is_public_class_attribute(self):
        rw = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rw))
        self.assertNotIn("user_id", rw.__dict__)

    def test_text_is_public_class_attribute(self):
        rw = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rw))
        self.assertNotIn("text", rw.__dict__)

    def test_two_reviews_unique_ids(self):
        rw1 = Review()
        rw2 = Review()
        self.assertNotEqual(rw1.id, rw2.id)

    def test_two_reviews_different_created_at(self):
        rw1 = Review()
        sleep(0.05)
        rw2 = Review()
        self.assertLess(rw1.created_at, rw2.created_at)

    def test_two_reviews_different_updated_at(self):
        rw1 = Review()
        sleep(0.05)
        rw2 = Review()
        self.assertLess(rw1.updated_at, rw2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_repr = repr(my_date)
        rw = Review()
        rw.id = "777777"
        rw.created_at = rw.updated_at = my_date
        review_str = rw.__str__()
        self.assertIn("[Review] (777777)", review_str)
        self.assertIn("'id': '777777'", review_str)
        self.assertIn("'created_at': " + my_date_repr, review_str)
        self.assertIn("'updated_at': " + my_date_repr, review_str)

    def test_args_unused(self):
        rw = Review(None)
        self.assertNotIn(None, rw.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        my_date_iso = my_date.isoformat()
        rw = Review(id="777", created_at=my_date_iso, updated_at=my_date_iso)
        self.assertEqual(rw.id, "777")
        self.assertEqual(rw.created_at, my_date)
        self.assertEqual(rw.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_save(unittest.TestCase):
    """
    Unittests for testing save method of the Review class.
    """

    @classmethod
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

    def test_one_save(self):
        rw = Review()
        sleep(0.05)
        first_updated_at = rw.updated_at
        rw.save()
        self.assertLess(first_updated_at, rw.updated_at)

    def test_two_saves(self):
        rw = Review()
        sleep(0.05)
        first_updated_at = rw.updated_at
        rw.save()
        second_updated_at = rw.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        rw.save()
        self.assertLess(second_updated_at, rw.updated_at)

    def test_save_with_arg(self):
        rw = Review()
        with self.assertRaises(TypeError):
            rw.save(None)

    def test_save_updates_file(self):
        rw = Review()
        rw.save()
        review_id = "Review." + rw.id
        with open("file.json", "r") as f:
            self.assertIn(review_id, f.read())


class TestReview_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Review class.
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        rw = Review()
        self.assertIn("id", rw.to_dict())
        self.assertIn("created_at", rw.to_dict())
        self.assertIn("updated_at", rw.to_dict())
        self.assertIn("__class__", rw.to_dict())

    def test_to_dict_contains_added_attributes(self):
        rw = Review()
        rw.middle_name = "Johnson"
        rw.my_number = 777
        self.assertEqual("Johnson", rw.middle_name)
        self.assertIn("my_number", rw.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        rw = Review()
        review_dict = rw.to_dict()
        self.assertEqual(str, type(review_dict["id"]))
        self.assertEqual(str, type(review_dict["created_at"]))
        self.assertEqual(str, type(review_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        rw = Review()
        rw.id = "777777"
        rw.created_at = rw.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Review',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(rw.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        rw = Review()
        self.assertNotEqual(rw.to_dict(), rw.__dict__)

    def test_to_dict_with_arg(self):
        rw = Review()
        with self.assertRaises(TypeError):
            rw.to_dict(None)


if __name__ == "__main__":
    unittest.main()

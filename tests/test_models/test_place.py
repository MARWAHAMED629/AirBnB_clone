#!/usr/bin/python3
"""
Module for Place class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Place class.
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

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(_place))
        self.assertNotIn("city_id", _place.__dict__)

    def test_user_id_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(_place))
        self.assertNotIn("user_id", _place.__dict__)

    def test_name_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(_place))
        self.assertNotIn("name", _place.__dict__)

    def test_description_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(_place))
        self.assertNotIn("desctiption", _place.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(_place))
        self.assertNotIn("number_rooms", _place.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(_place))
        self.assertNotIn("number_bathrooms", _place.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(_place))
        self.assertNotIn("max_guest", _place.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(_place))
        self.assertNotIn("price_by_night", _place.__dict__)

    def test_latitude_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(_place))
        self.assertNotIn("latitude", _place.__dict__)

    def test_longitude_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(_place))
        self.assertNotIn("longitude", _place.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        _place = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(_place))
        self.assertNotIn("amenity_ids", _place.__dict__)

    def test_two_places_unique_ids(self):
        m_place1 = Place()
        m_place2 = Place()
        self.assertNotEqual(m_place1.id, m_place2.id)

    def test_two_places_different_created_at(self):
        m_place1 = Place()
        sleep(0.05)
        m_place2 = Place()
        self.assertLess(m_place1.created_at, m_place2.created_at)

    def test_two_places_different_updated_at(self):
        m_place1 = Place()
        sleep(0.05)
        m_place2 = Place()
        self.assertLess(m_place1.updated_at, m_place2.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        date_rep = repr(my_date)
        _place = Place()
        _place.id = "777777"
        _place.created_at = _place.updated_at = my_date
        _place_str = _place.__str__()
        self.assertIn("[Place] (777777)", _place_str)
        self.assertIn("'id': '777777'", _place_str)
        self.assertIn("'created_at': " + date_rep, _place_str)
        self.assertIn("'updated_at': " + date_rep, _place_str)

    def test_args_unused(self):
        _place = Place(None)
        self.assertNotIn(None, _place.__dict__.values())

    def test_instantiation_with_kwargs(self):
        my_date = datetime.today()
        date_is = my_date.isoformat()
        _place = Place(id="777", created_at=date_is, updated_at=date_is)
        self.assertEqual(_place.id, "777")
        self.assertEqual(_place.created_at, my_date)
        self.assertEqual(_place.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
    """
    Unittests for testing save method of the Place class.
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

    def test_one_save(self):
        _place = Place()
        sleep(0.05)
        first_updated_at = _place.updated_at
        _place.save()
        self.assertLess(first_updated_at, _place.updated_at)

    def test_two_saves(self):
        _place = Place()
        sleep(0.05)
        first_updated_at = _place.updated_at
        _place.save()
        second_updated_at = _place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        _place.save()
        self.assertLess(second_updated_at, _place.updated_at)

    def test_save_with_arg(self):
        _place = Place()
        with self.assertRaises(TypeError):
            _place.save(None)

    def test_save_updates_file(self):
        _place = Place()
        _place.save()
        _place_id = "Place." + _place.id
        with open("file.json", "r") as f:
            self.assertIn(_place_id, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Place class.
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

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        _place = Place()
        self.assertIn("id", _place.to_dict())
        self.assertIn("created_at", _place.to_dict())
        self.assertIn("updated_at", _place.to_dict())
        self.assertIn("__class__", _place.to_dict())

    def test_to_dict_contains_added_attributes(self):
        _place = Place()
        _place.middle_name = "Johnson"
        _place.my_number = 777
        self.assertEqual("Johnson", _place.middle_name)
        self.assertIn("my_number", _place.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        _place = Place()
        place_dict = _place.to_dict()
        self.assertEqual(str, type(place_dict["id"]))
        self.assertEqual(str, type(place_dict["created_at"]))
        self.assertEqual(str, type(place_dict["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        _place = Place()
        _place.id = "777777"
        _place.created_at = _place.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Place',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(_place.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        _place = Place()
        self.assertNotEqual(_place.to_dict(), _place.__dict__)

    def test_to_dict_with_arg(self):
        _place = Place()
        with self.assertRaises(TypeError):
            _place.to_dict(None)


if __name__ == "__main__":
    unittest.main()

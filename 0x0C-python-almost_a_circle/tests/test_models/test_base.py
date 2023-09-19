#!/usr/bin/python3
"""Defines unittests for base.py."""
import unittest
import json
import os
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Unit tests for the Base class."""

    def setUp(self):
        """Set up common test data."""
        Base._Base__nb_objects = 0
        self.obj1 = Base()
        self.obj2 = Base(42)
        self.obj3 = Base()

    def test_init_with_default_id(self):
        """Test initialization of Base class with default id."""
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj3.id, 3)

    def test_init_with_custom_id(self):
        """Test initialization of Base class with custom id."""
        self.assertEqual(self.obj2.id, 42)

    def test_to_json_string_empty_list(self):
        """Test to_json_string method with an empty list of dictionaries."""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        """Test to_json_string method with a non-empty list of dictionaries."""
        data = [{"key1": "value1"}, {"key2": "value2"}]
        result = Base.to_json_string(data)
        expected_result = json.dumps(data)
        self.assertEqual(result, expected_result)

    def test_save_to_file_with_none_list(self):
        """Test save_to_file method with None as the list."""
        filename = "Base.json"
        Base.save_to_file(None)
        with open(filename, "r") as file:
            file_content = file.read()
        self.assertEqual(file_content, "[]")

    def test_save_to_file_with_empty_list(self):
        """Test save_to_file method with an empty list."""
        filename = "Base.json"
        Base.save_to_file([])
        with open(filename, "r") as file:
            file_content = file.read()
        self.assertEqual(file_content, "[]")

    def test_from_json_string_empty_string(self):
        """Test from_json_string method with an empty JSON string."""
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        """Test from_json_string method with a non-empty JSON string."""
        json_string = '[{"key1": "value1"}, {"key2": "value2"}]'
        result = Base.from_json_string(json_string)
        expected_result = json.loads(json_string)
        self.assertEqual(result, expected_result)

    def test_create_rectangle(self):
        """Test create method for creating a Rectangle instance."""
        dictionary = {"width": 3, "height": 4, "id": 5}
        result = Base.create(**dictionary)
        self.assertTrue(isinstance(result, Base))
        self.assertEqual(result.width, 3)
        self.assertEqual(result.height, 4)
        self.assertEqual(result.id, 5)

    def test_create_square(self):
        """Test create method for creating a Square instance."""
        dictionary = {"size": 2, "id": 6}
        result = Base.create(**dictionary)
        self.assertTrue(isinstance(result, Base))
        self.assertEqual(result.size, 2)
        self.assertEqual(result.id, 6)

    def test_create_invalid_class(self):
        """Test create method with an invalid class name."""
        dictionary = {"invalid_key": "value"}
        with self.assertRaises(ValueError):
            Base.create(**dictionary)

    def test_load_from_file_non_existing_file(self):
        """Test load_from_file method with a non-existing JSON file."""
        result = Base.load_from_file()
        self.assertEqual(result, [])

    def tearDown(self):
        """Clean up after each test."""
        filename = "Base.json"
        try:
            with open(filename, "r") as file:
                file_content = file.read()
            if file_content == "[]":
                os.remove(filename)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    unittest.main()


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_constructor_with_id(self):
        base_instance = Base(10)
        self.assertEqual(base_instance.id, 10)

    def test_constructor_without_id(self):
        base_instance = Base()
        self.assertIsNotNone(base_instance.id)

    # def test_to_json_string_with_none(self):
    #     json_str = Base.to_json_string(None)
    #     self.assertEqual(json_str, "[]")
    #
    # def test_to_json_string_with_empty_list(self):
    #     json_str = Base.to_json_string([])
    #     self.assertEqual(json_str, "[]")

    def test_to_json_string_with_data(self):
        data = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
        json_str = Base.to_json_string(data)
        expected_json = '[{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]'
        self.assertEqual(json_str, expected_json)


if __name__ == '__main__':
    unittest.main()

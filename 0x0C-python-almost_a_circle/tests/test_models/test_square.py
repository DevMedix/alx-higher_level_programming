import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        square = Square(5)
        # self.assertIsNone(square.id)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_str_method(self):
        square = Square(5, 1, 2, 10)
        self.assertEqual(str(square), "[Square] (10) 1/2 - 5")

    def test_size_property(self):
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_size_property_invalid_type(self):
        square = Square(5)
        with self.assertRaises(TypeError):
            square.size = "invalid"

    def test_size_property_invalid_value(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.size = -3

    def test_update_method_args(self):
        square = Square(5)
        square.update(1, 7, 3, 4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_method_kwargs(self):
        square = Square(5)
        square.update(id=1, size=7, x=3, y=4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary_method(self):
        square = Square(5, 1, 2, 10)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 10, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()

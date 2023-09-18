import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    def test_constructor_with_id(self):
        rect = Rectangle(4, 5, id=1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)

    def test_constructor_without_id(self):
        rect = Rectangle(4, 5)
        self.assertIsNotNone(rect.id)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)

    def test_area(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    # def test_display(self):
    #     rect = Rectangle(3, 2)
    #     expected_output = "###\n###\n"
    #     with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
    #         rect.display()
    #         self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_method(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        expected_str = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(rect), expected_str)

    def test_update_method_args(self):
        rect = Rectangle(4, 5)
        rect.update(1, 6, 7, 8, 9)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 9)

    def test_update_method_kwargs(self):
        rect = Rectangle(4, 5)
        rect.update(id=1, width=6, height=7, x=8, y=9)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 9)

    def test_to_dictionary_method(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        rect_dict = rect.to_dictionary()
        expected_dict = {'id': 10, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(rect_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()

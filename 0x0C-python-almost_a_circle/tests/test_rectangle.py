#!/usr/bin/pyton3
"""
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Rectangle_instantiation(unittest.TestCase):
    """
    """
    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_width_getter(self):
        r = Rectangle(7, 8, 8, 5, 3)
        self.assertEqual(r.width, 7)

    def test_width_setter(self):
        r = Rectangle(7, 8, 8, 5, 3)
        r.width = 19
        self.assertEqual(r.width, 19)

    def test_height_getter(self):
        r = Rectangle(7, 8, 8, 5, 3)
        self.assertEqual(r.height, 8)

    def test_height_setter(self):
        r = Rectangle(7, 8, 8, 5, 3)
        r.height = 14
        self.assertEqual(r.height, 14)

    def test_x_getter(self):
        r = Rectangle(7, 8, 8, 5, 3)
        self.assertEqual(r.x, 8)

    def test_x_setter(self):
        r = Rectangle(7, 8, 8, 5, 3)
        r.x = 12
        self.assertEqual(r.x, 12)

    def test_y_getter(self):
        r = Rectangle(7, 8, 8, 5, 3)
        self.assertEqual(r.y, 5)

    def test_y_setter(self):
        r = Rectangle(7, 8, 8, 5, 3)
        r.y = 9
        self.assertEqual(r.y, 9)

    def test_private_attribute_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 8, 8, 5, 3).__width)

    def test_private_attribute_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 8, 8, 5, 3).__height)

    def test_private_attribute_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 8, 8, 5, 3).__x)

    def test_private_attribute_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(7, 8, 8, 5, 3).__y)

    def test_with_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(7)

    def test_with_two_args_sets_unique_ids(self):
        r1 = Rectangle(6, 4)
        r2 = Rectangle(4, 6)
        self.assertEqual(r2.id - 1, r1.id)

    def test_with_three_args_sets_unique_ids(self):
        r1 = Rectangle(9, 9, 5)
        r2 = Rectangle(5, 5, 9)
        self.assertEqual(r2.id - 1, r1.id)

    def test_four_arguments_sets_unique_ids(self):
        r1 = Rectangle(2, 3, 4, 5 )
        r2 = Rectangle(4, 4, 3, 2 )
        self.assertEqual(r2.id - 1, r1.id)

class Test_Rectangle_Height(unittest.TestCase):
    """
    """

    def test_None_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, None)

    def test_str_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "eddy")

    def test_float_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, 3.5)

    def test_complex_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {"a": 3, "b": 4})

    def test_list_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [1, 2, 3])

    def test_set_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {1, 2, 3})

    def test_tuple_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (1, 2, 3))

    def test_frozenset_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, frozenset({2, 3, 4, 2}))

    def test_range_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, range(10))

    def test_bytes_type_as_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, b'Python')

    def test_invalid_type_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, bytearray(b'abcd'))

    def test_invalid_type_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, memoryview(b'abcd'))

    def test_invalid_value_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'))

    def test_invalid_value_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('nan'))

    def test_invalid_value_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -2)

    def test_invalid_value_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0)
    
class Test_Rectangle_Width(unittest.TestCase):
    """
    """
    
    def test_negative_integer_as_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 4)

    def test_invalid_value_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

    def test_None_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4)

    def test_str_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("eddy", 4)

    def test_float_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.5, 4)

    def test_complex_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 4)

    def test_dict_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 4)

    def test_bool_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 11)

    def test_list_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([3, 4, 5], 4)

    def test_set_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({3, 4, 5}, 4)

    def test_tuple_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((3, 4, 5), 4)

    def test_frozenset_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({2, 3, 4, 2}), 4)

    def test_range_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(7), 4)

    def test_bytes_type_as_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 4)

    def test_invalid_type_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcd'), 4)

    def test_invalid_type_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcd'), 4)

    def test_invalid_value_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 4)

    def test_invalid_value_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 4)

class Test_Rectangle_X(unittest.TestCase):
    """
    """

    def test_negative_integer_as_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, x=-1, y=0)

    def test_none_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=None)

    def test_string_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x="eddy", y=2)

    def test_float_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=5.5, y=7)

    def test_complex_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=complex(5))

    def test_dict_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x={"a": 1, "b": 2}, y=7)

    def test_bool_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=True, y=7)

    def test_list_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=[1, 2, 3], y=7)

    def test_set_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x={1, 2, 3}, y=7)

    def test_tuple_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=(1, 2, 3), y=7)

    def test_frozenset_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=frozenset({1, 2, 3, 1}), y=7)

    def test_range_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=range(5), y=7)

    def test_bytes_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=b'Python', y=7)

    def test_bytearray_type_as_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=bytearray(b'abcdefg'), y=7)

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=memoryview(b'abced'), y=7)

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=float('inf'), y=7)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(4, 3, x=float('nan'), y=7)


class Test_Rectangle_Y(unittest.TestCase):
    """
    """
    def test_negative_integer_as_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 3, 0, y=-5)

    def test_none_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=None)

    def test_complex_type_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=complex(5))

    def test_dict_type_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y={"a": 1, "b": 2})

    def test_string_type_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y="eddy")

    def test_float_type_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=3.5)

    def test_list_type_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=[1, 2, 3])

    def test_set_type_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y={1, 2, 3})

    def test_tuple_type_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=(1, 2, 3))

    def test_frozenset_type_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=frozenset({1, 2, 3, 1}))

    def test_range_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=range(10))

    def test_bytes_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=b'Python')

    def test_bytearray_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=bytearray(b'abcde'))

    def test_memoryview_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=memoryview(b'abcef'))

    def test_inf_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 3, 7, y=float('inf'))

    def test_nan_as_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, y=float('nan'))

    
if __name__ == "__main__":
    unittest.main()

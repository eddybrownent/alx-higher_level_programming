#!/usr/bin/python3
"""
This module has test cases for
the base module
"""
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Base_instatiating(unittest.TestCase):
    """
    Test cases for class Base
    """

    def test_with_no_id(self):
        """
        passing the Base without arguments
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id -1)

    def test_id_negative(self):
        """
        passing a negatiev integer
        """
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_id_is_zero(self):
        """
        passing 0 as the argument
        """
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_two_args(self):
        """
        passing two arguments
        """
        with self.assertRaises(TypeError):
            b1 = Base(1, 3)

    def test_with_id(self):
        """
        passing a valid id as argument
        """
        b1 = Base(7)
        self.assertEqual(b1.id, 7)


    def test_id_as_float(self):
        """
        """
        b1 = Base(4.7)
        self.assertEqual(b1.id, 4.7)

    def test_string_as_id(self):
        """
        passing a sting as an argument
        """
        b1 = Base("eddy")
        self.assertEqual(b1.id, "eddy")

    def test_list_as_id(self):
        """
        passing a list a an argument
        """
        b1 = Base([2, 5, 4])
        self.assertEqual(b1.id, [2, 5, 4])

    def test_tuple_as_id(self):
        """
        passing a tuple as the argument
        """
        b1 = Base((3, 2))
        self.assertEqual(b1.id, (3, 2))

    def test_set_as_id(self):
        """
        pass a set as the argument
        """
        b1 = Base({5, 74, 8, 0})
        self.assertEqual(b1.id, {5, 74, 8, 0})

    def test_dict_as_id(self):
        """
        passing a dict type as the argument
        """
        b1 = Base({"name": 'eddy', "a": 1, "b": 3})
        self.assertEqual(b1.id, {"name": 'eddy', "a": 1, "b": 3})

    def test_class_instaces(self):
        """
        Testing the ids for many instances
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(17)
        self.assertEqual(b4.id, 17)

        b5 = Base()
        self.assertEqual(b5.id, b3.id + 1)

        b6 = Base(6)
        self.assertEqual(b6.id, 6)

    def test_None_as_id(self):
        """
        passing None as the argument
        """
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_bool_as_id(self):
        """
        testing with the bool True
        """
        b1 = Base(True)
        self.assertTrue(b1.id)

class Test_Base_to_json_string(unittest.TestCase):
    """
    """
    def test_to_json_string_empty_list(self):
        """
        """
        list = Base.to_json_string([])
        self.assertEqual(list, "[]")

    def test_to_json_string_null_list(self):
        """
        """
        list = Base.to_json_string(None)
        self.assertEqual(list, "[]")

    def test_to_json_string_more_than_one_arg(self):
        """
        """
        with self.assertRaises(TypeError):
            Base.to_json_string([], 3)

    def tes_to_json_string_no_args(self):
        """
        """
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_valid_list(self):
        """
        """
        data = [{"key1": "value1"}, {"key2": "value2"}]
        json = Base.to_json_string(data)
        self.assertEqual(json, '[{"key1": "value1"}, {"key2": "value2"}]')
    
    def test_to_json_string_square_type(self):
        s = Square(11, 5, 6, 9)
        json = Base.to_json_string([s.to_dictionary()])
        self.assertEqual(str, type(json))

    def test_to_json_string_square_dict(self):
        """
        """
        square = Square(4, 6, 7, 10)

        json = Base.to_json_string([square.to_dictionary()])
        self.assertEqual(len(json) , 39)

    def test_to_json_string_two_square_dicts(self):
        """
        checks if the to_json_string method returns 
        the correct JSON string representation for a list of two Square objects
        """
        s1 = Square(5, 8, 10, 13)
        s2 = Square(1, 2, 3, 5,)
        dicts = [s1.to_dictionary(), s2.to_dictionary()]
        json = Base.to_json_string(dicts)

        self.assertEqual(len(json), 78)

    def test_to_json_string_Rectangle_type(self):
        """
        """
        rectangle = Rectangle(5, 4, 7, 9, 6)

        json = Base.to_json_string([rectangle.to_dictionary()])
        self.assertEqual(str, type(json))

    def test_to_json_string_rectangle_two_dicts(self):
        """
        """
        r1 = Rectangle(11, 7, 5, 9, 4)
        r2 = Rectangle(3, 7, 2, 1, 16)
        dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json = Base.to_json_string(dicts)

        self.assertIsInstance(json, str)
        self.assertEqual(len(json), 106)

class Test_Base_save_to_file(unittest.TestCase):
    """
    """

    @classmethod
    def clean_up_files(self):
        """
        Deletes any files created during tesing
        """
        files_to_remove = ["Rectangle.json", "Square.json", "Base.json"]
        for file_name in files_to_remove:
            try:
                os.remove(file_name)
            except FileNotFoundError:
                pass

    def test_save_to_file_no_args(self):
        """
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_args(self):
        """
        """
        with self.assertRaises(TypeError):
            Square.save_to_file()

    def test_save_file_with_None(self):
        """
        """
        Square.save_to_file(None)

        with open("Square.json", "r") as my_file:
            self.assertEqual(my_file.read(), "[]")


    def test_save_to_file_empty_list(self):
        """
        """
        Rectangle.save_to_file([])

        with open("Rectangle.json", "r") as my_file:
                  self.assertEqual(my_file.read(), "[]")

    def test_save_to_file_cls_name_for_filename(self):
        """
        """
        r = Rectangle(5, 10, 2, 8)
        Base.save_to_file([r])

        with open("Base.json", "r") as my_file:
            content = my_file.read()
            self.assertEqual(len(content), 54)

    def test_save_to_file_overwrite(self):
        """
        """
        s1 = Square(6, 5, 24, 7)
        Square.save_to_file([s1])

        s2 = Square(8, 4, 17, 9)
        Square.save_to_file([s1])

        with open("Square.json", "r") as my_file:
            contents = my_file.read()
            self.assertEqual(len(contents), 39)

    def test_save_to_file_two_rectangles(self):
        """
        """
        r1 = Rectangle(12, 6, 4, 8)
        r2 = Rectangle(6, 8, 9, 55)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as my_file:
            contents = my_file.read()
            self.assertEqual(len(contents), 108)

class Test_Base_from_json_string(unittest.TestCase):
    """
    """
    def test_from_json_string_more_than_one_args(self):
        """
        """
        with self.assertRaises(TypeError):
            Base.from_json_string([], 2)

    def test_from_json_string_no_args(self):
        """
        """
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_None_input(self):
        """
        """
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list_input(self):
        """
        """
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_returns_list_type(self):
        """
        """
        list_input = [{"id": 4, "width": 14, "height": 7}]
        json = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_two_rectangles(self):
        """
        """
        list_input = [
                {"id": 32, "width": 5, "height": 10, "x": 4, "y": 7},
                {"id": 54, "width": 9, "height": 18, "x": 1, "y": 5},
            ]
        json = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        """
        """
        list_input = [
            {"id": 76, "size": 15, "height": 5},
            {"id": 12, "size": 8, "height": 4}
        ]
        json = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json)
        self.assertEqual(list_input, list_output)

class Test_Base_create(unittest.TestCase):
    """
    """
    def test_create_no_arguments(self):
            r = Rectangle.create()
            self.assertEqual(r.width, 1)
            self.assertEqual(r.height, 1)
            self.assertEqual(r.x, 0)
            self.assertEqual(r.y, 0)


    def test_create_more_than_one_argument(self):
        with self.assertRaises(TypeError):
            Base.create(10, 20)

    def test_crarte_rectangle_from_dictionary(self):
        r1 = Rectangle(17, 8, 2, 4, 11)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r2), "[Rectangle] (11) 2/4 - 17/8")

    def test_create_rectangle_object_is_unique(self):
        r1 = Rectangle(8, 6, 2, 4, 10)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_objects_not_equal(self):
        r1 = Rectangle(8, 6, 2, 4, 10)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_create_square_from_dictionary(self):
        s1 = Square(7, 9, 2, 4)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual("[Square] (4) 9/2 - 7", str(s2))

    def test_create_square_objects_not_equal(self):
        s1 = Square(5, 3, 2, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

    def test_create_objects_is_unique(self):
        s1 = Square(7, 9, 2, 4)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)

class Test_Base_load_from_file(unittest.TestCase):
    """
    """
    @classmethod
    def clean_up_files(self):
        """
        Deletes any created files in testing
        """
        try:
            os.remove("rectangle.json")
        except IOError:
            pass
        try:
            os.remove("square.json")
        except IOError:
            pass

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([], 2)

    def test_load_file_no_file(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        output = Rectangle.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(11, 6, 4, 3, 1)
        r2 = Rectangle(2, 5, 9, 6, 9)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(loaded_rectangles[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(11, 6, 4, 3, 1)
        r2 = Rectangle(2, 5, 9, 6, 9)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(loaded_rectangles[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(11, 6, 4, 3, 1)
        r2 = Rectangle(2, 5, 9, 6, 9)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in loaded_rectangles))
    
    def test_load_from_file_first_square(self):
        s1 = Square(5, 4, 3, 1)
        s2 = Square(1, 5, 7, 9)
        Square.save_to_file([s1, s2])
        loaded_squares = Square.load_from_file()
        self.assertEqual(str(s1), str(loaded_squares[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 4, 3, 1)
        s2 = Square(1, 5, 7, 9)
        Square.save_to_file([s1, s2])
        loaded_squares = Square.load_from_file()
        self.assertEqual(str(s2), str(loaded_squares[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 4, 3, 1)
        s2 = Square(1, 5, 7, 9)
        Square.save_to_file([s1, s2])
        loaded_squares = Square.load_from_file()
        self.assertTrue(all(isinstance(obj, Square) for obj in loaded_squares))



        
if __name__ == '__main__':
    unittest.main()

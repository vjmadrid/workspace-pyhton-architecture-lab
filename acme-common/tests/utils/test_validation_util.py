# -*- coding: utf-8 -*-


import unittest
import pytest

from src.acmecommon.utils.validation_util import ValidationUtil


class TestValidationUtil(unittest.TestCase):

    def setUp(self):
        pass

    # *** str ***

    def test_is_str_valid_with_null(self):
        self.assertFalse(ValidationUtil.is_str_valid(None))

    def test_is_str_valid_with_empty(self):
        self.assertFalse(ValidationUtil.is_str_valid(''))

    def test_is_str_valid(self):
        self.assertTrue(ValidationUtil.is_str_valid('test'))

    def test_is_str_valid_with_exception_with_exception_with_null(self):
        with pytest.raises(Exception) as excep:
            string = None
            ValidationUtil.is_str_valid_with_exception(string)

        assert "string:str is invalid" in str(excep.value)

    def test_is_str_valid_with_exception(self):
        self.assertTrue(ValidationUtil.is_str_valid_with_exception('test'))

    # *** dict ***

    def test_is_dict_valid_with_null(self):
        self.assertFalse(ValidationUtil.is_dict_valid(None))

    def test_is_dict_valid_with_empty(self):
        empty_dict = {}
        self.assertFalse(ValidationUtil.is_dict_valid(empty_dict))

    def test_is_dict_valid(self):
        example_dict = {'key': 'value'}
        self.assertTrue(ValidationUtil.is_dict_valid(example_dict))

    def test_is_dict_valid_with_exception_with_null(self):
        with pytest.raises(Exception) as excep:
            dictionary = None
            ValidationUtil.is_dict_valid_with_exception(dictionary)

        assert "dictionary:dict is invalid" in str(excep.value)

    def test_is_dic_valid_with_exception(self):
        example_dict = {'key': 'value'}
        self.assertTrue(ValidationUtil.is_dict_valid_with_exception(example_dict))

    # *** object ***

    def test_is_obj_valid_with_null(self):
        self.assertFalse(ValidationUtil.is_obj_valid(None))

    def test_is_obj_valid(self):
        self.assertTrue(ValidationUtil.is_obj_valid(''))

    def test_is_obj_valid_with_exception_with_null(self):
        with pytest.raises(Exception) as excep:
            object = None
            ValidationUtil.is_obj_valid_with_exception(object)

        assert "object is invalid" in str(excep.value)

    def test_is_obj_valid_with_exception(self):
        self.assertTrue(ValidationUtil.is_obj_valid_with_exception('test'))

if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-


import unittest
import pytest

from acmeselenium.constants import driver_constant
from acmeselenium.drivers.chrome import chrome_util
from acmeselenium.utils.validation_util import ValidationUtil


class TestValidationUtil(unittest.TestCase):

    def setUp(self):
        pass

    # *** driver ***

    def test_is_driver_valid_with_null(self):
        self.assertFalse(ValidationUtil.is_driver_valid(None))

    def test_is_driver_valid(self):
        browser = chrome_util.setup_driver_chrome_chromedriver()

        self.assertTrue(ValidationUtil.is_driver_valid(browser))

    def test_is_driver_valid_with_exception_with_null(self):
        with pytest.raises(Exception) as excep:
            ValidationUtil.is_driver_valid_with_exception(None)

        assert f"{driver_constant.DRIVER_KEY} is invalid" in str(excep.value)

    def test_is_driver_valid_with_exception(self):
        browser = chrome_util.setup_driver_chrome_chromedriver()

        self.assertTrue(ValidationUtil.is_driver_valid_with_exception(browser))

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

        assert f"string:str is invalid" in str(excep.value)

    def test_is_str_valid_with_exception(self):
        self.assertTrue(ValidationUtil.is_driver_valid_with_exception('test'))

    # *** dict ***

    def test_is_dict_valid_with_null(self):
        self.assertFalse(ValidationUtil.is_dict_valid(None))

    def test_is_dict_valid_with_empty(self):
        empty_dict = {}
        self.assertFalse(ValidationUtil.is_dict_valid(empty_dict))

    def test_is_dict_valid(self):
        example_dict = { 'key': 'value'}
        self.assertTrue(ValidationUtil.is_dict_valid(example_dict))

    def test_is_dict_valid_with_exception_with_null(self):
        with pytest.raises(Exception) as excep:
            dictionary = None
            ValidationUtil.is_dict_valid_with_exception(dictionary)

        assert f"dictionary:dict is invalid" in str(excep.value)

    def test_is_dic_valid_with_exception(self):
        example_dict = { 'key': 'value'}
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

        assert f"object is invalid" in str(excep.value)

    def test_is_obj_valid_with_exception(self):
        self.assertTrue(ValidationUtil.is_obj_valid_with_exception('test'))

if __name__ == "__main__":
    unittest.main()

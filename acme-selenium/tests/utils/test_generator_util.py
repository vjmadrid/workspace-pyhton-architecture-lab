# -*- coding: utf-8 -*-


import unittest


from src.acmeselenium.utils.generator_util import GeneratorUtil

TEST_URL_VALID = "acme/product"

TEST_URL_INVALID = "N/A"

TEST_GLOBAL_URL_LIST = {
    TEST_URL_VALID: ["product_1", "product_2"]
}


class TestGeneratorUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_random_index_with_empty(self):
        my_list = []

        with self.assertRaises(ValueError):
            GeneratorUtil.generate_random_index(my_list, False)

    def test_generate_random_index_valid(self):
        my_list = [1, 2, 3]

        index = GeneratorUtil.generate_random_index(my_list, False)
        self.assertIsNotNone(index)

    def test_generate_random_url_with_none(self):
        with self.assertRaises(ValueError):
            GeneratorUtil.generate_random_url(None)

    def test_generate_random_url_with_empty(self):
        with self.assertRaises(ValueError):
            GeneratorUtil.generate_random_url({})

    def test_generate_random_url_valid(self):
        TEST_URL_LIST = {
            'http://www.google.es/search?q=Postman': 'Postman',
            'http://www.google.es/search?q=Java': 'Java'
        }

        url_selected = GeneratorUtil.generate_random_url(TEST_URL_LIST)
        self.assertIsNotNone(url_selected)

    def test_generate_random_key_by_dict_with_invalid(self):
        with self.assertRaises(ValueError):
            GeneratorUtil.generate_random_key_by_dict(None)

        with self.assertRaises(ValueError):
            GeneratorUtil.generate_random_key_by_dict({})

    def test_generate_random_key_by_dict(self):
        url_selected = GeneratorUtil.generate_random_key_by_dict(TEST_GLOBAL_URL_LIST)
        self.assertIsNotNone(url_selected)

    def test_generate_random_value_by_dict_with_invalid_dict(self):
        with self.assertRaises(ValueError):
            GeneratorUtil.generate_random_value_by_dict(None, TEST_URL_INVALID)

        with self.assertRaises(ValueError):
            GeneratorUtil.generate_random_value_by_dict({}, TEST_URL_INVALID)

    def test_generate_random_value_by_dict_with_invalid_value(self):
        with self.assertRaises(KeyError):
            GeneratorUtil.generate_random_value_by_dict(TEST_GLOBAL_URL_LIST, TEST_URL_INVALID)

    def test_generate_random_value_by_dict(self):

        value = GeneratorUtil.generate_random_value_by_dict(TEST_GLOBAL_URL_LIST, TEST_URL_VALID)
        self.assertIsNotNone(value)


if __name__ == "__main__":
    unittest.main()

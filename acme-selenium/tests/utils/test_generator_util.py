# -*- coding: utf-8 -*-


import unittest


from src.acmeselenium.utils.generator_util import GeneratorUtil


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


if __name__ == "__main__":
    unittest.main()

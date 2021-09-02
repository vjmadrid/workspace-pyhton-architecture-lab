# -*- coding: utf-8 -*-


import unittest


from src.acmecommon.parsers.json_parser import JsonParser


TEST_EXAMPLE_JSON_PATH = './tests/parsers/'
TEST_EXAMPLE_JSON_FILE = 'example.json'


class TestJsonParser(unittest.TestCase):

    def setUp(self):
        self.json_parser = JsonParser(TEST_EXAMPLE_JSON_PATH, TEST_EXAMPLE_JSON_FILE)

    def test_is_json_valid_parser(self):
        json_value = self.json_parser.read_from_json()

        self.assertEqual('hello', json_value['message'])
        self.assertEqual(10, json_value['timeout'])


if __name__ == "__main__":
    unittest.main()

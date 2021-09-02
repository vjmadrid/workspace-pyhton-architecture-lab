# -*- coding: utf-8 -*-


import unittest


from src.acmecommon.parsers.configini_parser import ConfigIniParser


TEST_EXAMPLE_CONFIG_INI_PATH = './tests/parsers/'
TEST_EXAMPLE_CONFIG_INI_FILE = 'example.ini'


class TestConfigIniParser(unittest.TestCase):

    def setUp(self):
        self.config_ini_parser = ConfigIniParser(TEST_EXAMPLE_CONFIG_INI_PATH, TEST_EXAMPLE_CONFIG_INI_FILE)

    def test_is_config_ini_valid_parser(self):
        value_dict = self.config_ini_parser.config_section_dict('app')

        self.assertEqual('hello', value_dict['message'])
        self.assertEqual(10, int(value_dict['timeout']))


if __name__ == "__main__":
    unittest.main()

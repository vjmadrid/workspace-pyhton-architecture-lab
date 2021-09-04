# -*- coding: utf-8 -*-


import unittest

from src.acmecommon.utils.dict_util import DicUtil


class TestDateUtil(unittest.TestCase):

    TEST_DICT = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_key_by_value(self):
        self.assertEqual(
            "key_1", DicUtil().find_key_by_value(self.TEST_DICT, "value_1")
        )
        self.assertEqual(
            "key_2", DicUtil().find_key_by_value(self.TEST_DICT, "value_2")
        )
        self.assertEqual(
            "key_3", DicUtil().find_key_by_value(self.TEST_DICT, "value_3")
        )


if __name__ == "__main__":
    unittest.main()

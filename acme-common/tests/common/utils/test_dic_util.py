# -*- coding: utf-8 -*-


import unittest

from acmecommon.common.utils.dict_util import DicUtil


class TestDateUtil(unittest.TestCase):

    def setUp(self):
        self.dict_test = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}

    def test_find_key_by_value(self):
        self.assertEqual('key_1', DicUtil().find_key_by_value(self.dict_test, 'value_1'))
        self.assertEqual('key_2', DicUtil().find_key_by_value(self.dict_test, 'value_2'))
        self.assertEqual('key_3', DicUtil().find_key_by_value(self.dict_test, 'value_3'))


if __name__ == '__main__':
    unittest.main()

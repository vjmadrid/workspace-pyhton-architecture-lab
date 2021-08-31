# -*- coding: utf-8 -*-


import unittest
from acme.common.utils.number_util import NumberUtil


class TestNumberUtils(unittest.TestCase):
    def test_round_down(self):
        self.assertEqual(10, NumberUtil(12).round_down(1))
        self.assertEqual(120, NumberUtil(123).round_down(1))
        self.assertEqual(100, NumberUtil(123).round_down(2))
        self.assertEqual(123000, NumberUtil(123456).round_down(3))

    def test_set_value(self):
        _number_utils = NumberUtil()
        self.assertEqual("1,000", _number_utils.set_value(1000).insert_comma())

    def test_insert_comma(self):
        self.assertEqual("0", NumberUtil(0).insert_comma())
        self.assertEqual("23,451", NumberUtil(23451).insert_comma())
        self.assertEqual("1,498,478,477", NumberUtil(1498478477).insert_comma())
        self.assertEqual(
            "14,984,781,245,477", NumberUtil(14984781245477).insert_comma()
        )
        self.assertEqual("-23,451", NumberUtil(-23451).insert_comma())
        self.assertEqual("-23,454,241,241", NumberUtil(-23454241241).insert_comma())


if __name__ == "__main__":
    unittest.main()

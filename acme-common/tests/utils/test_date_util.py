# -*- coding: utf-8 -*-


import unittest
import datetime

from src.acmecommon.utils.date_util import DateUtil


class TestDateUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_valid_date(self):
        self.assertTrue(DateUtil().is_valid_date("20151021"))
        self.assertFalse(DateUtil().is_valid_date("20151041"))
        self.assertFalse(DateUtil().is_valid_date("2015102"))
        self.assertFalse(DateUtil().is_valid_date("20151000"))

    def test_get_first_date_of_next_month(self):
        base_date = datetime.datetime(2016, 12, 31)
        next_month = DateUtil().get_first_date_of_next_month(base_date=base_date)
        self.assertEqual(1, next_month.month)

        base_date = datetime.datetime(2016, 1, 1)
        next_month = DateUtil().get_first_date_of_next_month(base_date=base_date)
        self.assertEqual(2, next_month.month)

    def test_get_age_band(self):
        today = datetime.datetime.today()

        year = today.year - 36
        self.assertEqual(30, DateUtil().get_age_band(year=year))
        year = today.year - 41
        self.assertEqual(40, DateUtil().get_age_band(year=year))
        year = today.year - 99
        self.assertEqual(90, DateUtil().get_age_band(year=year))

    # def test_month_delta(self):
    #    date1 = datetime.datetime.strptime(str('2011-08-14 12:00:00'), '%Y-%m-%d %H:%M:%S')
    #    date2 = datetime.datetime.strptime(str('2012-02-15'), '%Y-%m-%d')

    #    self.assertEqual(6, DateUtil().month_delta(date1, date2))
    #    self.assertEqual(-6, DateUtil().month_delta(date2, date1))

    def test_get_timestamp_diff_formatted(self):
        _now = datetime.datetime.now()
        _date_utils = DateUtil()

        self.assertEqual(
            "-",
            _date_utils.get_timestamp_diff_formatted(
                _now.timestamp(), _now.timestamp()
            ),
        )


if __name__ == "__main__":
    unittest.main()

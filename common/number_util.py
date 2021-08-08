##-*- coding: utf-8 -*-

"""
Utilities
"""

import math
import unittest

__author__ = 'Víctor Madrid'
__credits__ = ['Víctor Madrid']
__copyright__ = 'Copyright 2021'

__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = ''
__email__ = ''
__status__ = 'Production'

class TestNumberUtils(unittest.TestCase):

    def test_round_down(self):
        self.assertEqual(30, NumberUtils(36).round_down(1))
        self.assertEqual(300, NumberUtils(361).round_down(2))
        self.assertEqual(700, NumberUtils(768).round_down(2))
        self.assertEqual(760, NumberUtils(768).round_down(1))
        self.assertEqual(768000, NumberUtils(768124).round_down(3))

    def test_set_value(self):
        _number_utils = NumberUtils()
        self.assertEqual('1,000', _number_utils.set_value(1000).insert_comma())

    def test_insert_comma(self):
        self.assertEqual('0', NumberUtils(0).insert_comma())
        self.assertEqual('23,451', NumberUtils(23451).insert_comma())
        self.assertEqual('1,498,478,477', NumberUtils(1498478477).insert_comma())
        self.assertEqual('14,984,781,245,477', NumberUtils(14984781245477).insert_comma())
        self.assertEqual('-23,451', NumberUtils(-23451).insert_comma())
        self.assertEqual('-23,454,241,241', NumberUtils(-23454241241).insert_comma())

class NotSupportedException(Exception):

    def __init__(self, message, errors):
        super(NotSupportedException, self).__init__(message)
        self.errors = errors

class NumberUtils:

    _int_value = 0
    _string_value = ''
    _len_string_value = 0

    def __init__(self, int_value=0):
        self._int_value = int(int_value)
        self._string_value = str(self._int_value)
        self._len_string_value = len(self._string_value)

    def __del__(self):
        self._int_value = 0
        self._string_value = ''
        self._len_string_value = 0
    
    def set_value(self, int_value=0):
        """
        Usage:
            _number_utils = NumberUtils()
            _number_utils.set_value(1000).insert_comma()  # returns '1,000'
        """
        self._int_value = int_value
        self._string_value = str(self._int_value)
        self._len_string_value = len(self._string_value)
        return self

    def insert_comma(self):
        """
        usage:
            NumberUtils(2200030112490).insert_comma() returns '2,200,030,112,490'
        """

        result = ''
        negative = False
        if 0 > self._int_value:
            negative = True
            self.set_value(abs(self._int_value))
        if self._string_value and self._string_value.isdigit():
            index = 0
            while index < self._len_string_value:
                single_result = ''
                if ((self._len_string_value - index - 1) % 3 == 0) and (index < self._len_string_value - 1):
                    single_result = self._string_value[index] + ','
                else:
                    single_result = self._string_value[index]                    
                result += single_result
                index += 1
        if negative:
            return '-' + result
        return result

    def round_down(self, x):
        """
        Usage:
            NumberUtils(768124).round_down(3) returns 768000
        """
        return self._int_value - (self._int_value % int(math.pow(10, int(x))))


if __name__ == '__main__':
    unittest.main()

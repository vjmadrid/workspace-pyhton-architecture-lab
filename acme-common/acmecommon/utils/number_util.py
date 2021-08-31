# -*- coding: utf-8 -*-


import math


class NumberUtil:

    _int_value = 0
    _string_value = ""
    _len_string_value = 0

    def __init__(self, int_value=0):
        self._int_value = int(int_value)
        self._string_value = str(self._int_value)
        self._len_string_value = len(self._string_value)

    def __del__(self):
        self._int_value = 0
        self._string_value = ""
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

    def round_down(self, value):
        """
        Usage:
            NumberUtils(12).round_down(1) returns 10
            NumberUtils(1234).round_down(2) returns 1200
            NumberUtils(123456).round_down(3) returns 123000
        """

        return self._int_value - (self._int_value % int(math.pow(10, int(value))))

    def insert_comma(self):
        """
        Usage:
            NumberUtils(2200030112490).insert_comma() returns '2,200,030,112,490'
        """

        result = ""
        negative = False

        if self._int_value < 0:
            negative = True
            self.set_value(abs(self._int_value))

        if self._string_value and self._string_value.isdigit():
            index = 0
            while index < self._len_string_value:
                single_result = ""

                if ((self._len_string_value - index - 1) % 3 == 0) and (
                    index < self._len_string_value - 1
                ):
                    single_result = self._string_value[index] + ","
                else:
                    single_result = self._string_value[index]

                result += single_result
                index += 1

        if negative:
            return "-" + result

        return result

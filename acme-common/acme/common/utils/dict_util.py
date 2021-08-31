# -*- coding: utf-8 -*-


class DicUtil:
    def find_key_by_value(self, dic, value):
        """
        Usage:
            _dic_util = DicUtil()
            _dic_util.find_key_by_value(dic,'test')

        WARNING: Behavior is undefined if there's more than one key that has the passed-in value
        """

        return [k for k, v in dic.items() if v == value][0]

    def find_key_by_value_case_insensitive(self, dic, value):
        """
        Usage:
            _dic_util = DicUtil()
            _dic_util.find_key_by_value(dic,'TEST')

        WARNING: Behavior is undefined if there's more than one key that has the passed-in value
        """

        return [k for k, v in dic.items() if v == value][0]

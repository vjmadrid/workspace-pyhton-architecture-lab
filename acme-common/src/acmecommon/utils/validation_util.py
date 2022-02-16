# -*- coding: utf-8 -*-


class ValidationUtil:

    @staticmethod
    def is_str_valid(string: str):
        return ((string is not None) and (len(string.strip())))

    @staticmethod
    def is_str_valid_with_exception(string: str):
        if not ValidationUtil.is_str_valid(string):
            name_param = ValidationUtil.is_str_valid_with_exception.__code__.co_varnames[0]
            raise Exception(f"{name_param}:str is invalid")
        return True

    @staticmethod
    def is_dict_valid(dictionary: dict):
        return ((dictionary is not None) and (len(dictionary)))

    @staticmethod
    def is_dict_valid_with_exception(dictionary: dict):
        if not ValidationUtil.is_dict_valid(dictionary):
            name_param = ValidationUtil.is_dict_valid_with_exception.__code__.co_varnames[0]
            raise Exception(f"{name_param}:dict is invalid")
        return True

    @staticmethod
    def is_obj_valid(object):
        return (object is not None)

    @staticmethod
    def is_obj_valid_with_exception(object: dict):
        if not ValidationUtil.is_obj_valid(object):
            name_param = ValidationUtil.is_obj_valid_with_exception.__code__.co_varnames[0]
            raise Exception(f"{name_param} is invalid")
        return True

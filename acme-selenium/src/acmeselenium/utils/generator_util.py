# -*- coding: utf-8 -*-

import datetime

from random import randint

from selenium.webdriver.common.by import By


class GeneratorUtil:

    def __init__(self):
        pass

    def generate_random_index_by_list_xpath_filter(self, driver, list_xpath_filter):

        if driver is None:
            raise ValueError('Driver invalid')

        if list_xpath_filter:
            elements = driver.find_elements(By.XPATH, list_xpath_filter)
            num_elements = len(elements)

            return (-1, randint(1, num_elements))[num_elements > 0]

        return -1

    @staticmethod
    def generate_random_index(element_list, is_array_mode):

        if element_list is None or (bool(element_list) is False):
            raise ValueError('List is invalid')

        result = -1
        num_elements = len(element_list)

        if num_elements > 0:
            result = randint(1, num_elements)
            if is_array_mode:
                return result - 1

        return result

    @staticmethod
    def generate_random_url(url_dict):

        if url_dict is None or (bool(url_dict) is False):
            raise ValueError('URL dictionary is invalid')

        keys_url_list = list(url_dict)
        index_url = GeneratorUtil.generate_random_index(keys_url_list, True)

        url_selected = keys_url_list[index_url]

        return url_selected

    @staticmethod
    def generate_random_value():
        return (int(datetime.datetime.now().strftime("%s")) * 1000)

    @staticmethod
    def generate_random_key_by_dict(value_dict):

        if value_dict is None or (bool(value_dict) is False):
            raise ValueError('Dictionary is invalid')

        keys = value_dict.keys()
        keys_list = list(keys)
        index = GeneratorUtil.generate_random_index(keys, True)

        print(str(keys))
        print(str(index))

        if index < 0:
            return -1

        key_selected = keys_list[index]
        return key_selected

    @staticmethod
    def generate_random_value_by_dict(value_dict, value_key):

        if value_dict is None or (bool(value_dict) is False):
            raise ValueError('Dictionary is invalid')

        value_list = value_dict[value_key]
        index = GeneratorUtil.generate_random_index(value_list, True)

        if index < 0:
            return None

        value_selected = value_list[index]
        return value_selected

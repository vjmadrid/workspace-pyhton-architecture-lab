# -*- coding: utf-8 -*-


class CookieUtil:

    @staticmethod
    def set_cookie(driver, cookie_dict):

        if driver is None:
            raise ValueError('Driver invalid')

        driver.add_cookie(cookie_dict)

    @staticmethod
    def set_cookies(driver, cookie_dict_list):

        if driver is None:
            raise ValueError('Driver invalid')

        if cookie_dict_list:
            for index in len(cookie_dict_list):
                CookieUtil.set_cookie(driver, cookie_dict_list[index])

    @staticmethod
    def show_cookies(driver):

        if driver is None:
            raise ValueError('Driver invalid')

        return driver.get_cookies()

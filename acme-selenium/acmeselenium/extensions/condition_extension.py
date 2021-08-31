# -*- coding: utf-8 -*-


"""
XXXX
"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Condition():

    def __init__(self, expected_condition, scope):
        self.expected_condition = expected_condition
        self.scope = scope

    # @property
    # def default_message(self):
    #     return make_default_condition_message(self.expected_condition)

    def wait_for(self, timeout=5):
        WebDriverWait(self.scope, timeout).until(
            self.expected_condition,
            message=f"{self.default_message} in {timeout} seconds",
        )

    def __bool__(self):
        try:
            return bool(self.expected_condition(self.scope))
        except NoSuchElementException:
            return False

    def __repr__(self):
        return str(self.__bool__())

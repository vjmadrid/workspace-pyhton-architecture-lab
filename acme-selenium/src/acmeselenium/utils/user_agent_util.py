# -*- coding: utf-8 -*-


from selenium.webdriver.remote.webdriver import WebDriver


class AgentUtil:

    @staticmethod
    def get_user_agent(driver: WebDriver):
        return driver.execute_script("return navigator.userAgent")

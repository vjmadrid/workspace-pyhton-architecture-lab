# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from acmeselenium.constants import driver_constant
from acmeselenium.drivers.chrome import chrome_option_util
from acmeselenium.drivers.firefox import firefox_option_util

from .web_driver_listener import WebDriverListener


class DriverFactory:

    @staticmethod
    def get_driver(browser_type, options_dict) -> EventFiringWebDriver:
        if browser_type == driver_constant.BROWSER_TYPE_FIREFOX:
            return DriverFactory.get_driver_firefox(options_dict)

        if browser_type == driver_constant.BROWSER_TYPE_CHROME:
            return DriverFactory.get_driver_chrome(options_dict)

        return None

    @staticmethod
    def get_driver_chrome(options_dict) -> EventFiringWebDriver:
        if options_dict is None:
            raise ValueError('Options invalid')

        cutom_options = chrome_option_util.default_chrome_options(options_dict)

        driver = EventFiringWebDriver(
            webdriver.Chrome(
                executable_path=ChromeDriverManager().install(), options=cutom_options
            ),
            WebDriverListener(),
        )

        return driver

    @staticmethod
    def get_driver_firefox(options_dict) -> EventFiringWebDriver:
        if options_dict is None:
            raise ValueError('Options invalid')

        cutom_options = firefox_option_util.default_firefox_options(options_dict)

        driver = EventFiringWebDriver(
            webdriver.Firefox(
                executable_path=GeckoDriverManager().install(), options=cutom_options
            ),
            WebDriverListener(),
        )

        return driver

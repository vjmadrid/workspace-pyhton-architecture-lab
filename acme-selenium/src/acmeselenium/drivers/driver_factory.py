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
    def get_driver_with_executable(browser_type, executable_path, options_dict) -> EventFiringWebDriver:
        """Returns a web driver according to the configuration from an installation

        :param browser_type: String with the type of browser to use
        :type browser_type: str

        :param executable_path: Web driver executable installation path
        :type executable_path: str

        :param options_dict: Configuration options for web driver
        :type options_dict: Options

        :raises ValueError: Invalid parameter

        :return: Driver configured for Chrome
        :rtype: WebDriver
        """

        if browser_type == driver_constant.BROWSER_TYPE_FIREFOX:
            return DriverFactory.get_driver_firefox(executable_path, options_dict)

        if browser_type == driver_constant.BROWSER_TYPE_CHROME:
            return DriverFactory.get_driver_chrome(executable_path, options_dict)

        return None

    @staticmethod
    def get_driver(browser_type, options_dict) -> EventFiringWebDriver:
        """Returns a web driver according to the configuration from a dependency (provided by default)

        :param browser_type: String with the type of browser to use
        :type browser_type: str

        :param options_dict: Configuration options for web driver
        :type options_dict: Options

        :raises ValueError: Invalid parameter

        :return: Driver configured for Chrome
        :rtype: WebDriver
        """

        if browser_type == driver_constant.BROWSER_TYPE_FIREFOX:
            return DriverFactory.get_driver_with_executable(browser_type, GeckoDriverManager().install(), options_dict)

        if browser_type == driver_constant.BROWSER_TYPE_CHROME:
            return DriverFactory.get_driver_with_executable(browser_type, ChromeDriverManager().install(), options_dict)

        return None

    @staticmethod
    def get_driver_chrome(executable_path, options_dict) -> EventFiringWebDriver:
        """Returns a web driver for Chrome configured

        :param executable_path: Web driver executable installation path, defaults to ChromeDriverManager().install()
        :type executable_path: str

        :param options_dict: Configuration options for Chrome, defaults to None
        :type options_dict: Options

        :return: Driver configured for Chrome
        :rtype: WebDriver
        """

        if executable_path is None:
            executable_path = ChromeDriverManager().install()

        if options_dict is None:
            raise ValueError('options_dict is an invalid parameter')

        options = chrome_option_util.custom_chrome_options(options_dict)

        driver = EventFiringWebDriver(
            webdriver.Chrome(
                executable_path=executable_path, options=options
            ),
            WebDriverListener()
        )

        return driver

    @staticmethod
    def get_driver_firefox(executable_path, options_dict) -> EventFiringWebDriver:
        """Returns a web driver for Firefox configured

        :param executable_path: Web driver executable installation path, defaults to GeckoDriverManager().install()
        :type executable_path: str

        :param options_dict: Configuration options for Chrome
        :type options_dict: Options

        :return: Driver configured for Chrome
        :rtype: WebDriver
        """

        if executable_path is None:
            executable_path = GeckoDriverManager().install()

        if executable_path is None:
            raise ValueError('options_dict is an invalid parameter')

        options = firefox_option_util.custom_firefox_options(options_dict)

        driver = EventFiringWebDriver(
            webdriver.Firefox(
                executable_path=executable_path, options=options
            ),
            WebDriverListener()
        )

        return driver

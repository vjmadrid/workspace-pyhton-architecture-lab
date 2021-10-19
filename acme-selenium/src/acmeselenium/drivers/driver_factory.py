# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from acmeselenium.constants import driver_constant
from acmeselenium.drivers.chrome import chrome_option_util
from acmeselenium.drivers.firefox import firefox_option_util

from .web_driver_listener import WebDriverListener


VALID_BROWSER_SET = set([
    driver_constant.BROWSER_TYPE_FIREFOX,
    driver_constant.BROWSER_TYPE_CHROME
])


class DriverFactory:

    @staticmethod
    def get_webdriver_manager_executable_path(browser_type):
        if browser_type is None:
            raise Exception('browser_type is an invalid parameter')

        result = None
        if browser_type == driver_constant.BROWSER_TYPE_FIREFOX:
            result = GeckoDriverManager().install()
        elif browser_type == driver_constant.BROWSER_TYPE_CHROME:
            result = ChromeDriverManager().install()
        else:
            raise Exception(f'"{browser_type}" is not a supported browser')
        return result

    @staticmethod
    def get_driver(options_dict) -> EventFiringWebDriver:
        """Returns a web driver according to the configuration from a dependency (provided by default)

        Example
            example_options_dict = {
                'browser_type': xxx, # *
                'executable_path': xxx,
                'headless': xxx,
                'download_path': xxx,
                'file_types': 'xxx'
            }

        :param options_dict: Configuration options for web driver
        :type options_dict: dict

        :raises ValueError: Invalid parameter

        :return: Driver configured for Chrome
        :rtype: WebDriver
        """

        if options_dict is None:
            raise Exception('options_dict is an invalid parameter')

        if driver_constant.BROWSER_TYPE_KEY not in options_dict:
            raise Exception(f"{driver_constant.BROWSER_TYPE_KEY} is an invalid parameter")

        browser_type = options_dict[driver_constant.BROWSER_TYPE_KEY]
        if browser_type not in VALID_BROWSER_SET:
            raise Exception(f'"{browser_type}" is not a supported browser')

        executable_path = None
        if driver_constant.EXECUTABLE_PATH_KEY in options_dict:
            executable_path_param = options_dict[driver_constant.EXECUTABLE_PATH_KEY]
            if not executable_path_param:
                executable_path = executable_path_param
        else:
            executable_path = DriverFactory.get_webdriver_manager_executable_path(browser_type)

        options_dict[driver_constant.EXECUTABLE_PATH_KEY] = executable_path

        result = None
        if browser_type == driver_constant.BROWSER_TYPE_FIREFOX:
            result = DriverFactory.get_driver_firefox(options_dict)
        elif browser_type == driver_constant.BROWSER_TYPE_CHROME:
            result = DriverFactory.get_driver_chrome(options_dict)
        return result

    @staticmethod
    def get_driver_chrome(options_dict) -> EventFiringWebDriver:
        """Returns a web driver for Chrome configured

        Example
            example_options_dict = {
                'executable_path': xxx,     # Optional
                'user_data_path': xxx,      # Optional
                'headless': xxx,
                'download_path': xxx,
                'file_types': 'xxx'
            }

        :param executable_path: Web driver executable installation path, defaults to ChromeDriverManager().install()
        :type executable_path: str

        :param options_dict: Configuration options for Chrome, defaults to None
        :type options_dict: dict

        :return: Driver configured for Chrome
        :rtype: WebDriver
        """

        if options_dict is None:
            raise ValueError('options_dict is an invalid parameter')

        if driver_constant.EXECUTABLE_PATH_KEY not in options_dict:
            raise Exception(f"{driver_constant.EXECUTABLE_PATH_KEY} is an invalid parameter")

        executable_path = options_dict[driver_constant.EXECUTABLE_PATH_KEY]

        if executable_path is None:
            executable_path = ChromeDriverManager().install()

        options = chrome_option_util.custom_chrome_options(options_dict)

        driver = EventFiringWebDriver(
            webdriver.Chrome(
                executable_path=executable_path, options=options
            ),
            WebDriverListener()
        )

        return driver

    @staticmethod
    def get_driver_firefox(options_dict) -> EventFiringWebDriver:
        """Returns a web driver for Firefox configured

        Example
            example_options_dict = {
                'executable_path': xxx,     # Optional
                'user_data_path': xxx,      # Optional
                'headless': xxx,
                'download_path': xxx,
                'file_types': 'xxx'
            }

        :param executable_path: Web driver executable installation path, defaults to GeckoDriverManager().install()
        :type executable_path: str

        :param options_dict: Configuration options for Chrome
        :type options_dict: dict

        :return: Driver configured for Chrome
        :rtype: WebDriver
        """

        if options_dict is None:
            raise ValueError('options_dict is an invalid parameter')

        if driver_constant.EXECUTABLE_PATH_KEY not in options_dict:
            raise Exception(f"{driver_constant.EXECUTABLE_PATH_KEY} is an invalid parameter")

        executable_path = options_dict[driver_constant.EXECUTABLE_PATH_KEY]

        if executable_path is None:
            executable_path = GeckoDriverManager().install()

        options = firefox_option_util.custom_firefox_options(options_dict)

        driver = EventFiringWebDriver(
            webdriver.Firefox(
                executable_path=executable_path, options=options
            ),
            WebDriverListener()
        )

        return driver

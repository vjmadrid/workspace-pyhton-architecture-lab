# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from .web_driver_listener import WebDriverListener


class DriverFactory:

    @staticmethod
    def get_driver(browser, headless_mode=False) -> EventFiringWebDriver:
        if browser == 'firefox':
            return DriverFactory.get_driver_firefox(headless_mode)
        elif browser == 'chrome':
            return DriverFactory.get_driver_chrome(headless_mode)
        else:
            return None

    @staticmethod
    def get_driver_chrome(headless_mode=False) -> EventFiringWebDriver:
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        if headless_mode is True:
            options.add_argument("--headless")

        driver = EventFiringWebDriver(
            webdriver.Chrome(ChromeDriverManager().install(), options=options),
            WebDriverListener(),
        )

        return driver

    @staticmethod
    def get_driver_firefox(headless_mode=False) -> EventFiringWebDriver:
        options = webdriver.FirefoxOptions()

        if headless_mode is True:
            options.headless = True

        driver = EventFiringWebDriver(
            webdriver.Firefox(
                executable_path=GeckoDriverManager().install(), options=options
            ),
            WebDriverListener(),
        )

        return driver

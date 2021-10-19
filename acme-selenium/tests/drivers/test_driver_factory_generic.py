# -*- coding: utf-8 -*-


import unittest
import os
import pytest

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from acmeselenium.constants import driver_constant
from acmeselenium.drivers.driver_factory import DriverFactory
from acmeselenium.supports import testing_google_support


DEFAULT_SLEEP = 3
TEST_DEFAULT_DOWNLOAD_FOLDER = os.path.dirname(os.path.dirname(__file__))
TEST_OPTIONS_CHROME_DICT = {
    driver_constant.BROWSER_TYPE_KEY: 'chrome',
    driver_constant.EXECUTABLE_PATH_KEY: None,
    driver_constant.HEADLESS_KEY: True,
    driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
    driver_constant.FILE_TYPES_KEY: 'text/plain'
}
TEST_OPTIONS_CHROME_WITH_EXECUTABLE_DICT = {
    driver_constant.BROWSER_TYPE_KEY: 'chrome',
    driver_constant.EXECUTABLE_PATH_KEY: ChromeDriverManager().install(),
    driver_constant.HEADLESS_KEY: True,
    driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
    driver_constant.FILE_TYPES_KEY: 'text/plain'
}
TEST_OPTIONS_FIREFOX_DICT = {
    driver_constant.BROWSER_TYPE_KEY: 'firefox',
    driver_constant.EXECUTABLE_PATH_KEY: None,
    driver_constant.HEADLESS_KEY: True,
    driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
    driver_constant.FILE_TYPES_KEY: 'text/plain'
}
TEST_OPTIONS_FIREFOX_WITH_EXECUTABLE_DICT = {
    driver_constant.BROWSER_TYPE_KEY: 'firefox',
    driver_constant.EXECUTABLE_PATH_KEY: GeckoDriverManager().install(),
    driver_constant.HEADLESS_KEY: True,
    driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
    driver_constant.FILE_TYPES_KEY: 'text/plain'
}


class TestDriverFactoryChrome(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_driver_options_null(self):
        with pytest.raises(Exception) as excep:
            DriverFactory.get_driver(None)
        assert "options_dict is an invalid parameter" in str(excep.value)

    def test_get_driver_invalid_browser_type_param(self):
        TEST_OPTIONS_DICT = {
            driver_constant.HEADLESS_KEY: True,
            driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
            driver_constant.FILE_TYPES_KEY: 'text/plain'
        }

        with pytest.raises(Exception) as excep:
            DriverFactory.get_driver(TEST_OPTIONS_DICT)
        assert f"{driver_constant.BROWSER_TYPE_KEY} is an invalid parameter" in str(excep.value)

    def test_get_driver_invalid_browser_type_value(self):
        INVALID_BROWSER_VALUE = 'acme'
        TEST_OPTIONS_DICT = {
            driver_constant.BROWSER_TYPE_KEY: INVALID_BROWSER_VALUE,
            driver_constant.HEADLESS_KEY: True,
            driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
            driver_constant.FILE_TYPES_KEY: 'text/plain'
        }

        with pytest.raises(Exception) as excep:
            DriverFactory.get_driver(TEST_OPTIONS_DICT)
        assert '"acme" is not a supported browser' in str(excep.value)

    def test_get_driver_with_chrome(self):
        browser = DriverFactory.get_driver(TEST_OPTIONS_CHROME_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)

    def test_get_driver_with_chrome_executable(self):
        browser = DriverFactory.get_driver(TEST_OPTIONS_CHROME_WITH_EXECUTABLE_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)

    def test_get_driver_with_firefox(self):
        browser = DriverFactory.get_driver(TEST_OPTIONS_FIREFOX_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)

    def test_get_driver_with_firefox_executable(self):
        browser = DriverFactory.get_driver(TEST_OPTIONS_FIREFOX_WITH_EXECUTABLE_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)


if __name__ == "__main__":
    unittest.main()

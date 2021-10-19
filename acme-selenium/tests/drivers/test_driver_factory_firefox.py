# -*- coding: utf-8 -*-


import unittest
import os
import pytest

from webdriver_manager.firefox import GeckoDriverManager

from acmeselenium.constants import driver_constant
from acmeselenium.drivers.driver_factory import DriverFactory
from acmeselenium.supports import testing_google_support


DEFAULT_SLEEP = 3
TEST_DEFAULT_DOWNLOAD_FOLDER = os.path.dirname(os.path.dirname(__file__))


class TestDriverFactoryFirefox(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_driver_firefox_options_null(self):
        with pytest.raises(Exception) as excep:
            DriverFactory.get_driver_firefox(None)
        assert "options_dict is an invalid parameter" in str(excep.value)

    def test_get_driver_firefox_invalid_executable_path(self):
        TEST_INVALID_OPTIONS_DICT = {
            driver_constant.HEADLESS_KEY: True,
            driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
            driver_constant.FILE_TYPES_KEY: 'text/plain'
        }

        with pytest.raises(Exception) as excep:
            DriverFactory.get_driver_firefox(TEST_INVALID_OPTIONS_DICT)
        assert f"{driver_constant.EXECUTABLE_PATH_KEY} is an invalid parameter" in str(excep.value)

    def test_get_driver_firefox(self):
        TEST_OPTIONS_DICT = {
            driver_constant.EXECUTABLE_PATH_KEY: None,
            driver_constant.HEADLESS_KEY: True,
            driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
            driver_constant.FILE_TYPES_KEY: 'text/plain'
        }

        browser = DriverFactory.get_driver_firefox(TEST_OPTIONS_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)

    def test_get_driver_firefox_with_executable(self):
        TEST_OPTIONS_WITH_EXECUTABLE_DICT = {
            driver_constant.EXECUTABLE_PATH_KEY: GeckoDriverManager().install(),
            driver_constant.HEADLESS_KEY: True,
            driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
            driver_constant.FILE_TYPES_KEY: 'text/plain'
        }

        browser = DriverFactory.get_driver_firefox(TEST_OPTIONS_WITH_EXECUTABLE_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elememaknts_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)


if __name__ == "__main__":
    unittest.main()

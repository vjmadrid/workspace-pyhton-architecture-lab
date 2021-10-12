# -*- coding: utf-8 -*-


import unittest
import os


from acmeselenium.constants import driver_constant
from acmeselenium.drivers.driver_factory import DriverFactory
from acmeselenium.supports import testing_google_support


DEFAULT_SLEEP = 3

TEST_DEFAULT_DOWNLOAD_FOLDER = os.path.dirname(os.path.dirname(__file__))
TEST_OPTIONS_DICT = {
    'headless': True,
    'custom_download_path': TEST_DEFAULT_DOWNLOAD_FOLDER,
    'file_types': 'text/plain'
}


class TestDriverFactory(unittest.TestCase):

    def setUp(self):
        pass

    # *** Firefox ***

    def test_get_driver_firefox(self):
        browser = DriverFactory.get_driver_firefox(TEST_OPTIONS_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)

    def test_get_driver_generic_with_firefox(self):
        browser = DriverFactory.get_driver(driver_constant.BROWSER_TYPE_FIREFOX, TEST_OPTIONS_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)

    # *** Chrome ***

    def test_setup_driver_chrome_default(self):
        browser = DriverFactory.get_driver_chrome(TEST_OPTIONS_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)

    def test_get_driver_generic_with_chrome(self):
        browser = DriverFactory.get_driver(driver_constant.BROWSER_TYPE_CHROME, TEST_OPTIONS_DICT)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)


if __name__ == "__main__":
    unittest.main()

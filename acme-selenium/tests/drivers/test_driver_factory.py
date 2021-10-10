# -*- coding: utf-8 -*-


import unittest


from acmeselenium.constants import driver_constant
from acmeselenium.drivers.driver_factory import DriverFactory
from acmeselenium.supports import testing_google_support


class TestDriverFactory(unittest.TestCase):

    def setUp(self):
        pass

    def test_setup_driver_firefox_default(self):
        browser = DriverFactory.get_driver_firefox(True)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.TEST_INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)

    def test_setup_driver_chrome_default(self):
        browser = DriverFactory.get_driver_chrome(True)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.TEST_INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)

    def test_get_driver_firefox(self):
        browser = DriverFactory.get_driver(driver_constant.BROWSER_TYPE_FIREFOX, True)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.TEST_INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)

    def test_get_driver_chrome(self):
        browser = DriverFactory.get_driver(driver_constant.BROWSER_TYPE_CHROME, True)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.TEST_INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)


if __name__ == "__main__":
    unittest.main()

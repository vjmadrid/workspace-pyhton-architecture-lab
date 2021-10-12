# -*- coding: utf-8 -*-


import unittest


from selenium import webdriver
from src.acmeselenium.drivers.firefox import firefox_util
from acmeselenium.supports import testing_google_support


class TestFirefoxUtil(unittest.TestCase):

    def setUp(self):
        self.firefox_options = webdriver.FirefoxOptions()
        self.firefox_options.headless = True

    def test_setup_driver_firefox_gecko_default(self):
        browser = firefox_util.setup_driver_firefox_gecko()
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)

    def test_setup_driver_firefox_gecko_with_options(self):
        browser = firefox_util.setup_driver_firefox_gecko(self.firefox_options)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-


import unittest


from selenium import webdriver
from acmeselenium.drivers.chrome import chrome_util
from acmeselenium.supports import testing_google_support


class TestChromeUtil(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.headless = True

    def test_setup_driver_chrome_chromedriver_default(self):
        browser = chrome_util.setup_driver_chrome_chromedriver()
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)

    def test_setup_driver_chrome_chromedriver_with_options(self):
        browser = chrome_util.setup_driver_chrome_chromedriver(self.chrome_options)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)

    def test_setup_driver_chrome_default(self):
        browser = chrome_util.setup_driver_chrome(chrome_util.DEFAULT_CHROME_DRIVER_PATH_MAC_OS, None)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)

    def test_setup_driver_chrome_with_options(self):
        browser = chrome_util.setup_driver_chrome(chrome_util.DEFAULT_CHROME_DRIVER_PATH_MAC_OS, self.chrome_options)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_text_search = browser.find_elements_by_css_selector(testing_google_support.INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_text_search)


if __name__ == "__main__":
    unittest.main()

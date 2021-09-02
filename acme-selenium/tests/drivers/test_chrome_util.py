# -*- coding: utf-8 -*-


import unittest


from src.acmeselenium.drivers import chrome_util
from selenium.webdriver.chrome.options import Options


TEST_GOOGLE_URL = 'https://www.google.com'
TEST_ELEMENT_SELECTOR = 'input[name=q]'


class TestChromeUtil(unittest.TestCase):

    def setUp(self):
        pass

    def test_setup_driver_chrome_default(self):
        browser = chrome_util.setup_driver_chrome_default()
        browser.get(TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(TEST_ELEMENT_SELECTOR)

        self.assertIsNotNone(input_element)

    def test_setup_driver_chrome_with_options(self):
        custom_options = Options()
        custom_options.headless = True

        browser = chrome_util.setup_driver_chrome_with_options(custom_options)
        browser.get(TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(TEST_ELEMENT_SELECTOR)

        self.assertIsNotNone(input_element)


if __name__ == "__main__":
    unittest.main()

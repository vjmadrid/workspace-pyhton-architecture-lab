# -*- coding: utf-8 -*-


import unittest


from src.acmeselenium.drivers import firefox_util
from selenium.webdriver.firefox.options import Options


TEST_GOOGLE_URL = 'https://www.google.com'
TEST_ELEMENT_SELECTOR = 'input[name=q]'


class TestFirefoxUtil(unittest.TestCase):

    def setUp(self):
        pass

    def test_setup_driver_firefox_default(self):
        browser = firefox_util.setup_driver_firefox_default()
        browser.get(TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(TEST_ELEMENT_SELECTOR)

        self.assertIsNotNone(input_element)

    def test_setup_driver_firefox_with_options(self):
        custom_options = Options()
        custom_options.headless = True

        browser = firefox_util.setup_driver_firefox_with_options(custom_options)
        browser.get(TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(TEST_ELEMENT_SELECTOR)

        self.assertIsNotNone(input_element)


if __name__ == "__main__":
    unittest.main()

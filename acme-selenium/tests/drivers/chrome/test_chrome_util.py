# -*- coding: utf-8 -*-


import unittest


from acmeselenium.drivers.chrome import chrome_util
from acmeselenium.supports import testing_google_support
from selenium.webdriver.chrome.options import Options


class TestChromeUtil(unittest.TestCase):

    def setUp(self):
        pass

    def test_setup_driver_chrome_chromedriver_default(self):
        browser = chrome_util.setup_driver_chrome_chromedriver()
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.TEST_INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)

    def test_setup_driver_chrome_chromedriver_with_options(self):
        custom_options = Options()
        custom_options.headless = True

        browser = chrome_util.setup_driver_chrome_chromedriver(custom_options)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.TEST_INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)

    def test_setup_driver_chrome_default(self):
        browser = chrome_util.setup_driver_chrome(chrome_util.DEFAULT_CHROME_DRIVER_PATH_MAC_OS, None)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.TEST_INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)

    def test_setup_driver_chrome_with_options(self):
        custom_options = Options()
        custom_options.headless = True

        browser = chrome_util.setup_driver_chrome(chrome_util.DEFAULT_CHROME_DRIVER_PATH_MAC_OS, custom_options)
        browser.get(testing_google_support.TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(testing_google_support.TEST_INPUT_TEXT_SEARCH)

        browser.quit()

        self.assertIsNotNone(input_element)


if __name__ == "__main__":
    unittest.main()

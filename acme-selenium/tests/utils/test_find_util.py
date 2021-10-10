# -*- coding: utf-8 -*-


import unittest


from acmeselenium.drivers.chrome import chrome_util, chrome_option_util
from acmeselenium.utils.operation_find_util import OperationFindUtil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TEST_GOOGLE_URL = 'https://www.google.com'
TEST_INPUT_TEXT_SEARCH = 'input[name=q]'
TEST_SEARCH_BUTTON = 'input[name=btnK]'
TEST_LUCK_BUTTON = 'input[name=btnI]'


class TestFindUtil(unittest.TestCase):

    def setUp(self):
        pass

    def test_find_by_xpath(self):
        options = chrome_option_util.default_chrome_options_basic()
        browser = chrome_util.setup_driver_chrome_chromedriver(options)
        browser.get(TEST_GOOGLE_URL)

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]'))).click()

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, TEST_INPUT_TEXT_SEARCH))).click()
        input_element = OperationFindUtil().find(browser, By.XPATH, TEST_INPUT_TEXT_SEARCH, False)

        input("Pulsa...")

        browser.quit()

        self.assertIsNotNone(input_element)


if __name__ == "__main__":
    unittest.main()

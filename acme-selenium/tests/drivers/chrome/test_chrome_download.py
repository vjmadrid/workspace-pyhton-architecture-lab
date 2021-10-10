# -*- coding: utf-8 -*-


import unittest
import os
import time


from acmeselenium.drivers.chrome import chrome_util, chrome_option_util
from acmeselenium.utils import check_download_util
from acmeselenium.supports import testing_download_support


DEFAULT_DOWNLOAD_FOLDER = os.path.dirname(os.path.dirname(__file__))
TEST_EXAMPLE_FILE = "info.txt"
TEST_EXAMPLE_FILE_PATH = DEFAULT_DOWNLOAD_FOLDER + "/" + TEST_EXAMPLE_FILE


OPTIONS_DICT = {
    'headless': True,
    'custom_download_path': DEFAULT_DOWNLOAD_FOLDER,
    'file_type': 'text/plain'
}


class TestChromeDownload(unittest.TestCase):

    def setUp(self):
        pass

    def test_file_download_with_default_chrome_options_min(self):

        options = chrome_option_util.default_chrome_options_min()
        browser = chrome_util.setup_driver_chrome_chromedriver(options)

        chrome_util.enable_download_headless(browser, DEFAULT_DOWNLOAD_FOLDER)
        browser.get(testing_download_support.TEST_FILE_DOWNLOAD_URL)

        # Generate text file
        #   * Enter text
        #   * Create
        #   * Download
        browser.find_element_by_id(testing_download_support.TEST_INPUT_TEXT_AREA_CONTENT_FILE_ID) \
            .send_keys(testing_download_support.TEST_CONTENT_FILE)
        browser.find_element_by_id(testing_download_support.TEST_GENERATE_FILE_BUTTON_ID).click()
        browser.find_element_by_id(testing_download_support.TEST_DOWNLOAD_FILE_LINK_ID).click()

        time.sleep(2)

        browser.quit()

        self.assertTrue(os.path.exists(TEST_EXAMPLE_FILE_PATH))
        self.assertTrue(check_download_util.is_file_downloaded(TEST_EXAMPLE_FILE_PATH))

    def test_file_download_with_default_chrome_options_custom(self):

        options = chrome_option_util.default_chrome_options(OPTIONS_DICT)

        browser = chrome_util.setup_driver_chrome_chromedriver(options)

        chrome_util.enable_download_headless(browser, DEFAULT_DOWNLOAD_FOLDER)
        browser.get(testing_download_support.TEST_FILE_DOWNLOAD_URL)

        # Generate text file
        #   * Enter text
        #   * Create
        #   * Download
        browser.find_element_by_id(testing_download_support.TEST_INPUT_TEXT_AREA_CONTENT_FILE_ID) \
            .send_keys(testing_download_support.TEST_CONTENT_FILE)
        browser.find_element_by_id(testing_download_support.TEST_GENERATE_FILE_BUTTON_ID).click()
        browser.find_element_by_id(testing_download_support.TEST_DOWNLOAD_FILE_LINK_ID).click()

        time.sleep(2)

        browser.quit()

        self.assertTrue(os.path.exists(TEST_EXAMPLE_FILE_PATH))
        self.assertTrue(check_download_util.is_file_downloaded(TEST_EXAMPLE_FILE_PATH))


if __name__ == "__main__":
    unittest.main()

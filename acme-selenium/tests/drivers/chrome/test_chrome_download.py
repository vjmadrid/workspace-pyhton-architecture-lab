# -*- coding: utf-8 -*-


import unittest
import os
import time


from acmeselenium.drivers.chrome import chrome_util, chrome_option_util
from acmeselenium.utils import check_download_util


TEST_FILE_DOWNLOAD_URL = 'http://demo.automationtesting.in/FileDownload.html'

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
DEFAULT_DOWNLOAD_FOLDER = '/Users/vjmadrid/Downloads/'
# DEFAULT_DOWNLOAD_FOLDER = ROOT_DIR
TEST_EXAMPLE_FILE = "info.txt"
TEST_EXAMPLE_FILE_PATH = DEFAULT_DOWNLOAD_FOLDER + "/" + TEST_EXAMPLE_FILE


OPTIONS_DICT = {
    'headless': True,
    'custom_download_path': DEFAULT_DOWNLOAD_FOLDER,
    'file_type': 'text/plain'
}


@unittest.skip('Skipping_unit_tests')
class TestChromeDownload(unittest.TestCase):

    def test_file_download(self):

        # chrome_options = chrome_option_util.default_chrome_options(OPTIONS_DICT)
        # chrome_options = chrome_option_util.default_chrome_options_basic()

        options = chrome_option_util.default_chrome_options_min()
        browser = chrome_util.setup_driver_chrome_chromedriver(options)
        chrome_util.enable_download_headless(browser, DEFAULT_DOWNLOAD_FOLDER)
        browser.get(TEST_FILE_DOWNLOAD_URL)

        # Generate text file
        #   * Enter text
        #   * Create
        #   * Download
        browser.find_element_by_id('textbox').send_keys("Hello World")
        browser.find_element_by_id('createTxt').click()
        browser.find_element_by_id('link-to-download').click()

        time.sleep(2)

        browser.quit()

        self.assertTrue(os.path.exists(TEST_EXAMPLE_FILE_PATH))
        self.assertTrue(check_download_util.is_file_downloaded(TEST_EXAMPLE_FILE_PATH))


if __name__ == "__main__":
    unittest.main()

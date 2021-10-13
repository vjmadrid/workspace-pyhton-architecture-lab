# -*- coding: utf-8 -*-


import unittest
import os
import time


from acmeselenium.drivers.chrome import chrome_util, chrome_option_util
from acmeselenium.utils import check_download_util
from acmeselenium.supports import testing_download_support


DEFAULT_SLEEP = 3

TEST_DEFAULT_DOWNLOAD_FOLDER = os.path.dirname(os.path.dirname(__file__)) + "/chrome"
TEST_EXAMPLE_FILE_PATH = TEST_DEFAULT_DOWNLOAD_FOLDER + "/" + testing_download_support.TEST_EXAMPLE_FILE
TEST_OPTIONS_DICT = {
    'headless': False,
    'download_path': TEST_DEFAULT_DOWNLOAD_FOLDER,
    'file_types': 'text/plain'
}


class TestChromeDownload(unittest.TestCase):

    def setUp(self):
        pass

    def test_file_download_by_chromedriver_with_default_chrome_options(self):
        options = chrome_option_util.default_chrome_options()
        browser = chrome_util.setup_driver_chrome_chromedriver(options)
        chrome_util.enable_download_headless(browser, TEST_DEFAULT_DOWNLOAD_FOLDER)

        testing_download_support.action_generate_and_download_file(browser)
        time.sleep(DEFAULT_SLEEP)
        browser.quit()

        self.assertTrue(os.path.exists(TEST_EXAMPLE_FILE_PATH))
        self.assertTrue(check_download_util.is_file_downloaded_and_delete(TEST_EXAMPLE_FILE_PATH))

    def test_file_download_by_chromedriver_with_custom_chrome_options(self):
        options = chrome_option_util.custom_chrome_options(TEST_OPTIONS_DICT)
        browser = chrome_util.setup_driver_chrome_chromedriver(options)

        testing_download_support.action_generate_and_download_file(browser)
        time.sleep(DEFAULT_SLEEP)
        browser.quit()

        self.assertTrue(os.path.exists(TEST_EXAMPLE_FILE_PATH))
        self.assertTrue(check_download_util.is_file_downloaded_and_delete(TEST_EXAMPLE_FILE_PATH))


if __name__ == "__main__":
    unittest.main()

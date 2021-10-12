# -*- coding: utf-8 -*-


import unittest
import os
import time


from acmeselenium.drivers.firefox import firefox_util, firefox_option_util
from acmeselenium.utils import check_download_util
from acmeselenium.supports import testing_download_support


DEFAULT_SLEEP = 3

TEST_DEFAULT_DOWNLOAD_FOLDER = os.path.dirname(os.path.dirname(__file__)) + "/firefox"
TEST_EXAMPLE_FILE_PATH = TEST_DEFAULT_DOWNLOAD_FOLDER + "/" + testing_download_support.TEST_EXAMPLE_FILE
TEST_OPTIONS_DICT = {
    'headless': True,
    'custom_download_path': TEST_DEFAULT_DOWNLOAD_FOLDER,
    'file_types': 'text/plain'
}


class TestFirefoxDownload(unittest.TestCase):

    def setUp(self):
        pass

    def test_file_download_by_gecko_with_default_firefox_options_min(self):
        options = firefox_option_util.default_firefox_options_min(TEST_DEFAULT_DOWNLOAD_FOLDER)
        browser = firefox_util.setup_driver_firefox_gecko(options)

        testing_download_support.action_generate_and_download_file(browser)
        time.sleep(DEFAULT_SLEEP)
        browser.quit()

        self.assertTrue(os.path.exists(TEST_EXAMPLE_FILE_PATH))
        self.assertTrue(check_download_util.is_file_downloaded_and_delete(TEST_EXAMPLE_FILE_PATH))

    def test_file_download_by_gecko_with_default_firefox_options_custom(self):
        options = firefox_option_util.default_firefox_options(TEST_OPTIONS_DICT)
        browser = firefox_util.setup_driver_firefox_gecko(options)

        testing_download_support.action_generate_and_download_file(browser)
        time.sleep(DEFAULT_SLEEP)
        browser.quit()

        self.assertTrue(os.path.exists(TEST_EXAMPLE_FILE_PATH))
        self.assertTrue(check_download_util.is_file_downloaded_and_delete(TEST_EXAMPLE_FILE_PATH))


if __name__ == "__main__":
    unittest.main()

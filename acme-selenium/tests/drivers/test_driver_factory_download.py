# -*- coding: utf-8 -*-


import unittest
import os
import time

from acmeselenium.constants import driver_constant
from acmeselenium.drivers.driver_factory import DriverFactory
from acmeselenium.utils import check_download_util
from acmeselenium.supports import testing_download_support


DEFAULT_SLEEP = 3

TEST_DEFAULT_DOWNLOAD_FOLDER = os.path.dirname(os.path.dirname(__file__))
TEST_EXAMPLE_FILE_PATH = TEST_DEFAULT_DOWNLOAD_FOLDER + "/" + testing_download_support.TEST_EXAMPLE_FILE
TEST_OPTIONS_FIREFOX_DICT = {
    driver_constant.BROWSER_TYPE_KEY: 'firefox',
    driver_constant.EXECUTABLE_PATH_KEY: None,
    driver_constant.HEADLESS_KEY: True,
    driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
    driver_constant.FILE_TYPES_KEY: 'text/plain'
}
TEST_OPTIONS_CHROME_DICT = {
    driver_constant.BROWSER_TYPE_KEY: 'chrome',
    driver_constant.EXECUTABLE_PATH_KEY: None,
    driver_constant.HEADLESS_KEY: True,
    driver_constant.DOWNLOAD_PATH_KEY: TEST_DEFAULT_DOWNLOAD_FOLDER,
    driver_constant.FILE_TYPES_KEY: 'text/plain'
}


class TestDriverFactoryDownload(unittest.TestCase):

    def setUp(self):
        pass

    # *** Firefox ***

    def test_get_driver_firefox_download(self):
        browser = DriverFactory.get_driver(TEST_OPTIONS_FIREFOX_DICT)

        testing_download_support.action_generate_and_download_file(browser)
        time.sleep(DEFAULT_SLEEP)
        browser.quit()

        self.assertTrue(os.path.exists(TEST_EXAMPLE_FILE_PATH))
        self.assertTrue(check_download_util.is_file_downloaded_and_delete(TEST_EXAMPLE_FILE_PATH))

    # *** Chrome ***

    def test_get_driver_chrome_download(self):
        browser = DriverFactory.get_driver(TEST_OPTIONS_CHROME_DICT)

        testing_download_support.action_generate_and_download_file(browser)
        time.sleep(DEFAULT_SLEEP)
        browser.quit()

        self.assertTrue(os.path.exists(TEST_EXAMPLE_FILE_PATH))
        self.assertTrue(check_download_util.is_file_downloaded_and_delete(TEST_EXAMPLE_FILE_PATH))


if __name__ == "__main__":
    unittest.main()

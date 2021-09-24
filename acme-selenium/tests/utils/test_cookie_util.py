# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

from src.acmeselenium.utils.cookie_util import CookieUtil


@unittest.skip('Skipping_unit_tests')
class TestCookieUtil(unittest.TestCase):

    TEST_URL = 'https://reddit.com'
    TEST_COOKIE_DOMAIN = 'reddit.com'
    TEST_EXAMPLE_COOKIE = {'name': 'cookiesPolicy', 'value': '1', 'domain': TEST_COOKIE_DOMAIN}
    TEST_EXAMPLE_COOKIE_FLAG = {'name': 'acme_monitoriz', 'value': 'true', 'domain': TEST_COOKIE_DOMAIN}

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"
        self.browser = webdriver.Chrome(desired_capabilities=caps, chrome_options=chrome_options)
        self.on_testing = True

    def tearDown(self):
        if (self.on_testing):
            self.browser.quit()

    def test_add_cookie(self):
        self.browser.get(self.TEST_URL)

        CookieUtil.set_cookie(self.browser, self.TEST_EXAMPLE_COOKIE)

        cookies_list = self.browser.get_cookies()

        self.assertIsNotNone(cookies_list)
        self.assertEquals(7, len(cookies_list))


if __name__ == "__main__":
    unittest.main()

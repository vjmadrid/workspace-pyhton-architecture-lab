# -*- coding: utf-8 -*-


import unittest


from src.acmeselenium.drivers.driver_factory import DriverFactory


TEST_GOOGLE_URL = 'https://www.google.com'
TEST_ELEMENT_SELECTOR = 'input[name=q]'


@unittest.skip('Skipping_unit_tests')
class TestDriverFactory(unittest.TestCase):

    def setUp(self):
        pass

    def test_setup_driver_firefox_default(self):
        browser = DriverFactory.get_driver_firefox(True)
        browser.get(TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(TEST_ELEMENT_SELECTOR)

        self.assertIsNotNone(input_element)

    def test_setup_driver_chrome_default(self):
        browser = DriverFactory.get_driver_chrome(True)
        browser.get(TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(TEST_ELEMENT_SELECTOR)

        self.assertIsNotNone(input_element)

    def test_setup_driver_default(self):
        browser = DriverFactory.get_driver('firefox', True)
        browser.get(TEST_GOOGLE_URL)

        input_element = browser.find_elements_by_css_selector(TEST_ELEMENT_SELECTOR)

        self.assertIsNotNone(input_element)


if __name__ == "__main__":
    unittest.main()

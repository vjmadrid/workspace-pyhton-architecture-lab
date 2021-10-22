# -*- coding: utf-8 -*-

import logging
import time

from selenium.webdriver.remote.webdriver import WebDriver

from acmeselenium.utils.validation_util import ValidationUtil


logger = logging.getLogger(__name__)


class ScrollUtil:

    @staticmethod
    def scroll_to(driver: WebDriver, offset_pixels: str):
        config_parameters = '{ "offset_pixels":' + str(offset_pixels) + "}"
        logger.info(
            "[SCROLL] [scroll_to] Scroll to  ... -> Parameters : %s", config_parameters
        )

        driver.execute_script(f"window.scrollTo(0, {offset_pixels});")

    @staticmethod
    def scroll_into_view(driver: WebDriver, element, offset_pixels=0):
        """Scrolls page to element using JS
        Args:
            driver (base.CustomDriver)
            element (WebElement)
            offset_pixels
        """
        config_parameters = '{ "offset_pixels":' + str(offset_pixels) + "}"
        logger.info(
            "[SCROLL] [scroll_into_view] Scroll into view  ... -> Parameters : %s", config_parameters
        )

        driver.execute_script("return arguments[0].scrollIntoView();", element)

        # Compensate for the header
        driver.execute_script(f"window.scrollBy(0, -{offset_pixels});")

        return element

    @staticmethod
    def scroll_by_element(driver: WebDriver, element):
        """Scrolls page to element

        :param driver: Browser used
        :type driver: WebDriver

        :param element: Element to be focused on
        :type element: WebElement

        :return: N/A
        :rtype: N/A
        """
        ValidationUtil.is_driver_valid_with_exception(driver)
        logger.debug("[SCROLL] Scroll by element ...")

        driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    @staticmethod
    def scroll_by_element_xpath(driver: WebDriver, xpath_element: str):
        """Scrolls page to element by xpath

        :param driver: Browser used
        :type driver: WebDriver

        :param xpath_element: Xpath of the element to focus on
        :type xpath_element: str

        :return: N/A
        :rtype: N/A
        """
        ValidationUtil.is_driver_valid_with_exception(driver)
        ValidationUtil.is_str_valid_with_exception(xpath_element)

        logger.debug("[SCROLL] Scroll by element xpath : %s", str(xpath_element))

        element = driver.find_element_by_xpath(xpath_element)
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)

    @staticmethod
    def scroll_to_the_end(driver: WebDriver):
        """Scrolls to the end of the page

        :param driver: Browser used
        :type driver: WebDriver

        :return: N/A
        :rtype: N/A
        """
        ValidationUtil.is_driver_valid_with_exception(driver)

        logger.debug("[SCROLL] Scroll to the end  ...")

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            ScrollUtil.scroll_to(driver, "document.body.scrollHeight)")
            time.sleep(0.5)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            last_height = new_height

    @staticmethod
    def scroll_to_page_bottom(driver: WebDriver):
        """Scrolls to te page bottom using JS

        :param driver: Browser used
        :type driver: WebDriver

        :return: N/A
        :rtype: N/A
        """
        ValidationUtil.is_driver_valid_with_exception(driver)
        logger.debug("[SCROLL] Scroll to Page Botton ...")

        ScrollUtil.scroll_to(driver, "document.body.scrollHeight)")

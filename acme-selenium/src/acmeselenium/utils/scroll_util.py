# -*- coding: utf-8 -*-

import logging
import time

from selenium.webdriver.remote.webdriver import WebDriver


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
    def scroll_to_page_bottom(driver: WebDriver):
        """Scrolls to te page bottom using JS
        Args:
            driver (base.CustomDriver)
        """
        config_parameters = "{}"
        logger.info(
            "[SCROLL] [scroll_to] Scroll to Page Botton ... -> Parameters : %s", config_parameters
        )

        ScrollUtil.scroll_to(driver, "document.body.scrollHeight)")

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
    def scroll_down_til_the_end(driver):
        """Scrolls page to element using JS
        Args:
            driver (base.CustomDriver)
        """
        config_parameters = "{}"
        logger.info(
            "[SCROLL] [scroll_down_til_the_end] Scrollinto view  ... -> Parameters : %s", config_parameters
        )

        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

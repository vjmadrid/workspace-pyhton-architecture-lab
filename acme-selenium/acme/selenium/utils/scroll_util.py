# -*- coding: utf-8 -*-

import logging
import time
from selenium.webdriver.remote.webdriver import WebDriver


logger = logging.getLogger(__name__)


def scroll_to(driver: WebDriver, offset_pixels: str):
    CONFIG_PARAMETERS = '{ "offset_pixels":' + str(offset_pixels) + '}'
    logger.info("[SCROLL] [scroll_to] Scroll to  ... -> Parameters : " + CONFIG_PARAMETERS)

    driver.execute_script("window.scrollTo(0, {});".format(offset_pixels))


def scroll_to_page_bottom(driver: WebDriver):
    """Scrolls to te page bottom using JS
    Args:
        driver (base.CustomDriver)
    """
    CONFIG_PARAMETERS = '{}'
    logger.info("[SCROLL] [scroll_to] Scroll to Page Botton ... -> Parameters : " + CONFIG_PARAMETERS)

    scroll_to(driver, "document.body.scrollHeight)")


def scroll_into_view(driver: WebDriver, element, offset_pixels=0):
    """Scrolls page to element using JS
    Args:
        driver (base.CustomDriver)
        element (WebElement)
        offset_pixels
    """
    CONFIG_PARAMETERS = '{ "offset_pixels":' + str(offset_pixels) + '}'
    logger.info("[SCROLL] [scroll_into_view] Scroll into view  ... -> Parameters : " + CONFIG_PARAMETERS)

    driver.execute_script("return arguments[0].scrollIntoView();", element)

    # Compensate for the header
    driver.execute_script("window.scrollBy(0, -{});".format(offset_pixels))

    return element


def scroll_down_til_the_end(driver):
    """Scrolls page to element using JS
    Args:
        driver (base.CustomDriver)
    """
    CONFIG_PARAMETERS = '{}'
    logger.info("[SCROLL] [scroll_down_til_the_end] Scrollinto view  ... -> Parameters : " + CONFIG_PARAMETERS)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

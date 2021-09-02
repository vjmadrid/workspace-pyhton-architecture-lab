# -*- coding: utf-8 -*-

import logging
from selenium.webdriver.remote.webdriver import WebDriver


logger = logging.getLogger(__name__)


def go_to_url(driver: WebDriver, url_page: str):
    config_parameters = '{ "urlPage":' + str(url_page) + "}"
    logger.debug(
        "[NAVIGATION] [go_to_url] Go to Url ... -> Parameters :%s", config_parameters
    )

    driver.get(url_page)
    # verification_util.verify_valid_url(driver, url_page, False)


def go_to_page(driver: WebDriver, class_page):
    config_parameters = '{ "classPage.NAME":' + str(class_page.NAME) + "}"
    logger.debug(
        "[NAVIGATION] [go_to_page] Go to Page Class ... -> Parameters : %s", config_parameters
    )

    go_to_url(driver, class_page.URL)

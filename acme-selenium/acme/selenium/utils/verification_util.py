# -*- coding: utf-8 -*-

import logging
from selenium.webdriver.common.by import By
from acmeselenium.selenium.utils import test_util

logger = logging.getLogger(__name__)


class UnderConstructionPage:

    NAME = "Under Construction Page"
    URL_PATH = "/maintenance"


def verify_if_exist_by_xpath(driver, xpathElement):
    CONFIG_PARAMETERS = '{ "xpathElement":' + str(xpathElement) + '}'
    logging.getLogger().debug("[VERIFICATION] [verifyIfExistByXpath] Verify Exist By XPath ... -> Parameters : " + CONFIG_PARAMETERS)

    resultSelected = driver.find_elements(By.XPATH, xpathElement)
    return len(resultSelected) > 0


def verify_valid_url(driver, definied_URL, test_mode):
    CONFIG_PARAMETERS = '{ "definiedURL":' + str(definied_URL) + ', "test_mode":' + str(test_mode) + '}'
    logging.getLogger().debug("[VERIFICATION] [verify_valid_url] Verify Valid URL ... -> Parameters : " + CONFIG_PARAMETERS)

    result = True
    if UnderConstructionPage.URL_PATH in driver.current_url:
        test_util.show_error_message(test_mode, "[VERIFICATION] [verify_valid_url] ERROR. Under Construction Page")
        result = False

    if definied_URL not in driver.current_url:
        error_message = "[VERIFICATION] [verify_valid_url] ERROR. URL Target Page " + str(driver.current_url) \
            + " NOT contains " + str(definied_URL)
        test_util.show_error_message(test_mode, error_message)
        result = False

    return result


def verify_valid_url_with_exit(driver, definied_URL, test_mode):
    verifyURL = verify_valid_url(driver, definied_URL, test_mode)

    if not verifyURL:
        driver.quit()
        quit()

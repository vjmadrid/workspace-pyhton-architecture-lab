# -*- coding: utf-8 -*-

import logging
import sys

from selenium.webdriver.common.by import By

from acmeselenium.utils import test_util


logger = logging.getLogger(__name__)


class UnderConstructionPage:

    NAME = "Under Construction Page"
    URL_PATH = "/maintenance"


def verify_if_exist_by_xpath(driver, xpath_element):
    config_parameters = '{ "xpathElement":' + str(xpath_element) + "}"
    logging.getLogger().debug(
        "[VERIFICATION] [verifyIfExistByXpath] Verify Exist By XPath ... -> Parameters : %s", config_parameters
    )

    result_selected = driver.find_elements(By.XPATH, xpath_element)
    return len(result_selected) > 0


def verify_valid_url(driver, definied_url, test_mode):
    config_parameters = (
        '{ "definiedURL":' + str(definied_url) + ', "test_mode":' + str(test_mode) + "}"
    )
    logging.getLogger().debug(
        "[VERIFICATION] [verify_valid_url] Verify Valid URL ... -> Parameters : %s", config_parameters
    )

    result = True
    if UnderConstructionPage.URL_PATH in driver.current_url:
        test_util.show_error_message(
            test_mode,
            "[VERIFICATION] [verify_valid_url] ERROR. Under Construction Page",
        )
        result = False

    if definied_url not in driver.current_url:
        error_message = (
            "[VERIFICATION] [verify_valid_url] ERROR. URL Target Page "
            + str(driver.current_url)
            + " NOT contains "
            + str(definied_url)
        )
        test_util.show_error_message(test_mode, error_message)
        result = False

    return result


def verify_valid_url_with_exit(driver, definied_url, test_mode):
    verify_url = verify_valid_url(driver, definied_url, test_mode)

    if not verify_url:
        driver.quit()
        sys.exit()

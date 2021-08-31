# -*- coding: utf-8 -*-

import logging
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException


def webdriverwait(locator, driver, delay, until_element_EC, active_refresh, active_test_mode):
    """
    Performs a search attempt for an item by setting a delay time, a search condition, refresh and test mode
    """

    CONFIG_PARAMETERS = '{ "delay":' + str(delay) + ', "locator":' + str(locator) \
        + ', "active_refresh":' + str(active_refresh) + ', "active_test_mode":' + str(active_test_mode) + '}'
    logging.getLogger().debug("[ACTION] [Operation] Run WebDriverWait ... -> Parameters : " + CONFIG_PARAMETERS)

    if (active_refresh):
        driver.refresh()

    element = None
    try:
        element = WebDriverWait(driver, delay).until(until_element_EC)
        return element
    except TimeoutException as ex:
        # print ("ERROR. Timeout Reached. Exception: " + str(traceback.format_exc(ex)))

        if (active_test_mode):
            assert False, "ERROR. Timeout Reached. Exception: " + str(traceback.format_exc(ex))

        return element


def webdriverwait_default(locator, driver, delay, until_element_EC):
    """
    Performs a search attempt for an item by setting a delay time and a search condition
    """

    return webdriverwait(locator, driver, delay, until_element_EC, False, False)


def test_webdriverwait_default(locator, driver, delay, until_element_EC):
    """
    Performs a search attempt for an item by setting a delay time and a search condition

    Use Test
    """

    return webdriverwait(locator, driver, delay, until_element_EC, False, True)


def retry_webdriverwait(locator, driver, delay, until_element_EC, max_retries, active_refresh, active_test_mode):
    """
    Performs a search attempt for an item by setting a delay time, a search condition, defining a retry policy, refresh and test mode
    """

    CONFIG_PARAMETERS = '{"delay":' + str(delay) + ', "locator":' + str(locator) + ', "max_retries":' + str(max_retries) \
        + ', "active_refresh":' + str(active_refresh) + ', "active_test_mode":' + str(active_test_mode) + '}'
    logging.getLogger().debug("[ACTION] [Operation] Retry WebDriverWait ... -> Parameters : " + CONFIG_PARAMETERS)

    num_retries = 1
    while(num_retries < max_retries):
        logging.getLogger().debug("Retry " + str(num_retries))

        try:
            element = WebDriverWait(driver, delay).until(until_element_EC)
            return element
        except StaleElementReferenceException:
            print("Stale reference on WebDriverWait... retrying ")
        except TimeoutException as ex:
            print("WARNING. Timeout Reached retry " + str(num_retries) + "ex :" + str(ex))

        if (active_refresh):
            driver.refresh()

        num_retries = num_retries + 1

    # Last attempt
    return webdriverwait(locator, driver, delay, until_element_EC, active_refresh, False)


def retry_webdriverwait_default(locator, driver, delay, until_element_EC, max_retries):
    """
    Performs a search attempt for an item by setting a delay time, a search condition (expected_conditions) and defining a retry policy
    """

    return retry_webdriverwait(locator, driver, delay, until_element_EC, max_retries, False, False)


def test_retry_webdriverwait_default(locator, driver, delay, until_element_EC, max_retries):
    """
    Test Performs a search attempt for an item by setting a delay time, a search condition (expected_conditions) and defining a retry policy
    """

    return retry_webdriverwait(locator, driver, delay, until_element_EC, max_retries, False, True)

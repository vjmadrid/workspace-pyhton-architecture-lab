import traceback
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException



def webDriverWait(logger, locator, driver, delay, until_element_EC, active_refresh, active_test_mode):
    """
    Performs a search attempt for an item by setting a delay time, a search condition, refresh and test mode
    """

    CONFIG_PARAMETERS =  '{ "delay":'+str(delay) + ', "locator":' + str(locator) + ', "active_refresh":' + str(active_refresh) + ', "active_test_mode":' + str(active_test_mode)  +'}'
    logger.debug("[ACTION] [Operation] Run WebDriverWait : "+ CONFIG_PARAMETERS)

    if (active_refresh):
        driver.refresh()

    element = None
    try:
        element = WebDriverWait(driver, delay).until(until_element_EC)
        return element
    except TimeoutException as ex:
        #print ("ERROR. Timeout Reached. Exception: " + str(traceback.format_exc(ex)))

        if (active_test_mode):
            assert False, "ERROR. Timeout Reached. Exception: " + str(traceback.format_exc(ex))
        
        return element



def webDriverWait_default(logger, locator, driver, delay, until_element_EC):
    """
    Performs a search attempt for an item by setting a delay time and a search condition
    """

    return webDriverWait(logger, locator, driver, delay, until_element_EC, False, False)



def test_webDriverWait_default(logger, locator, driver, delay, until_element_EC):
    """
    Performs a search attempt for an item by setting a delay time and a search condition

    Use Test
    """

    return webDriverWait(logger, locator, driver, delay, until_element_EC, False, True)



def retry_webDriverWait(logger, locator, driver, delay, until_element_EC, max_retries, active_refresh, active_test_mode):
    """
    Performs a search attempt for an item by setting a delay time, a search condition, defining a retry policy, refresh and test mode
    """

    CONFIG_PARAMETERS =  '{ "delay":' + str(delay) + ', "locator":' + str(locator) + ', "max_retries":' + str(max_retries) + ', "active_refresh":' + str(active_refresh) + ', "active_test_mode":' + str(active_test_mode)  +'}'
    logger.debug("[ACTION] [Operation] Retry WebDriverWait : "+ CONFIG_PARAMETERS)

    num_retries = 1
    while(num_retries < max_retries):
        logger.debug("Retry "+ str(num_retries))

        try:
            element = WebDriverWait(driver, delay).until(until_element_EC)
            return element
        except StaleElementReferenceException:
            print ("Stale reference on WebDriverWait... retrying ") 
        except TimeoutException as ex:
            print ("WARNING. Timeout Reached retry "+str(num_retries))
        
        if (active_refresh):
            driver.refresh()

        num_retries = num_retries + 1

    # Last attempt
    return webDriverWait(logger, locator, driver, delay, until_element_EC, active_refresh, False)



def retry_webDriverWait_default(logger,locator, driver, delay, until_element_EC, max_retries):
    """
    Performs a search attempt for an item by setting a delay time, a search condition (expected_conditions) and defining a retry policy
    """

    return retry_webDriverWait(logger, locator, driver, delay, until_element_EC, max_retries, False, False)



def test_retry_webDriverWait_default(logger, locator, driver, delay, until_element_EC, max_retries):
    """
    Test Performs a search attempt for an item by setting a delay time, a search condition (expected_conditions) and defining a retry policy
    """

    return retry_webDriverWait(logger, locator, driver, delay, until_element_EC, max_retries, False, True)
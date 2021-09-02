import logging
import time

from selenium.common import exceptions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from acmeselenium.exceptions import selenium_exceptions

logger = logging.getLogger(__name__)


def is_value_in_attr(element, attr="class", value="active"):
    """Checks if the attribute value is present for given attribute
    Args:
      element (selenium.webdriver.remote.webelement.WebElement)
      attr (basestring): attribute name e.g. "class"
      value (basestring): value in the class attribute that
        indicates the element is now active/opened
    Returns:
        bool
    """
    attributes = element.get_attribute(attr)
    return value in attributes.split()


def click_on_staleable_element(driver: WebDriver, el_locator, wait_seconds=1):
    """Clicks an element that can be modified between the time we find it and when we click on it"""
    time_start = time.time()

    while time.time() - time_start < wait_seconds:
        try:
            driver.find_element(*el_locator).click()
            break
        except exceptions.StaleElementReferenceException as excep:
            logger.error(str(excep))
            time.sleep(0.1)
    else:
        raise selenium_exceptions.ElementNotFound(el_locator)


def element_is_visible(driver, by_selenium, locator, timeout):
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by_selenium, locator))
        )
        return True
    except TimeoutException:
        return False


def element_is_not_visible(driver, by_selenium, locator, timeout=8):
    try:
        WebDriverWait(driver, timeout).until_not(
            EC.visibility_of_element_located((by_selenium, locator))
        )
        return False
    except TimeoutException:
        return False

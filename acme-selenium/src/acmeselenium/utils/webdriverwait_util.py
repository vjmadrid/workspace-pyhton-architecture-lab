import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


logger = logging.getLogger(__name__)


class WebDriverWaitUtil:

    @staticmethod
    def webdriverwait_until_condition(driver: WebDriver, condition, wait_seconds=1):
        """Wait until given expected condition is met
        Args:
            driver (base.CustomDriver)
            condition
            wait_seconds
        """
        WebDriverWait(driver, wait_seconds).until(condition)

    @staticmethod
    def webdriverwait_when_visible(driver: WebDriver, locator, wait_seconds=1):
        """Return WebElement by locator when is visible
        Args:
            driver (base.CustomDriver)
            locator (tuple)
        Returns:
            selenium.webdriver.remote.webelement.WebElement
        """

        return WebDriverWaitUtil.webdriverwait_until_condition(
            driver, EC.presence_of_element_located(locator), wait_seconds
        )

    @staticmethod
    def webdriverwait_when_all_visible(driver: WebDriver, locator, wait_seconds=1):
        """Return WebElements by locator when all of them are visible
        Args:
            locator (tuple)
        Returns:
            selenium.webdriver.remote.webelement.WebElements
        """

        return WebDriverWaitUtil.webdriverwait_until_condition(
            driver, EC.visibility_of_any_elements_located(locator), wait_seconds
        )

    def get_when_invisible(driver: WebDriver, locator, wait_seconds=1):
        """Return WebElement by locator when is invisible
        Args:
            driver (base.CustomDriver)
            locator (tuple)
        Returns:
            selenium.webdriver.remote.webelement.WebElement
        """

        return WebDriverWaitUtil.webdriverwait_until_condition(
            driver, EC.invisibility_of_element_located(locator), wait_seconds
        )

    @staticmethod
    def webdriverwait_until_not_present(driver: WebDriver, locator):
        """Wait until no element(-s) for locator given are present in the DOM"""

        WebDriverWaitUtil.webdriverwait_until_condition(driver, lambda d: len(d.find_elements(*locator)) == 0)

    def webdriverwait_when_clickable(driver: WebDriver, locator, wait_seconds=1):
        """
        Args:
            driver (base.CustomDriver)
            locator (tuple)
        Returns:
            selenium.webdriver.remote.webelement.WebElement
        """

        return WebDriverWaitUtil.webdriverwait_until_condition(
            driver, EC.element_to_be_clickable(locator), wait_seconds
        )

    @staticmethod
    def webdriverwait_for_element_text(
        driver: WebDriver, by_selenium, locator, text: str, wait_seconds=1
    ):
        """Return WebElement by locator when a text is present in element
        Args:
            driver (base.CustomDriver)
            by
            locator (tuple)
            text (str)
        """

        return WebDriverWaitUtil.webdriverwait_until_condition(
            driver, EC.text_to_be_present_in_element(by_selenium, locator), wait_seconds
        )

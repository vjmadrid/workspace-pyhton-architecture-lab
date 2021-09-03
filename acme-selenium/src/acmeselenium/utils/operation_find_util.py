# -*- coding: utf-8 -*-


from selenium.common.exceptions import StaleElementReferenceException


class OperationFindUtil:

    @staticmethod
    def find(driver, how, what, active_refresh):
        """
        Performs a search attempt for an item by setting how and what
        """

        if active_refresh:
            driver.refresh()

        element = driver.find_element(how, what)
        return element

    @staticmethod
    def find_click(driver, how, what, active_refresh):
        """
        Performs a search attempt for an item by setting how and what + click
        """

        element = OperationFindUtil.find(driver, how, what, active_refresh).click()
        return element

    @staticmethod
    def retry_find(driver, how, what, max_retries, active_refresh):
        """
        Reintenta hasta encontrar el elemento y realiza click sobre el
        """

        num_retries = 1
        while num_retries < max_retries:

            try:
                element = driver.find_element(how, what)
                return element
            except StaleElementReferenceException:
                print("Stale reference on click or find!!!... retrying ")

            if active_refresh:
                driver.refresh()

            num_retries = num_retries + 1

        return OperationFindUtil.find_click(driver, how, what, active_refresh)

    @staticmethod
    def run_active_click(driver, element, is_active_click=False):
        if is_active_click:
            element.click()
        else:
            driver.execute_script("arguments[0].click();", element)

    @staticmethod
    def retry_find_click(
        driver, how, what, max_retries, active_refresh, is_active_click=False
    ):
        """
        Reintenta hasta encontrar el elemento y realiza click sobre el
        """

        num_retries = 1
        while num_retries < max_retries:

            try:
                element = driver.find_element(how, what)
                OperationFindUtil.run_active_click(driver, element, is_active_click)
                return element
            except StaleElementReferenceException:
                print("Stale reference on click or find!!!... retrying ")

            if active_refresh:
                driver.refresh()

            num_retries = num_retries + 1

        element = OperationFindUtil.find(driver, how, what, active_refresh)
        OperationFindUtil.run_active_click(driver, element, is_active_click)

        return element

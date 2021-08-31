# -*- coding: utf-8 -*-

import logging

from selenium.webdriver.support.events import AbstractEventListener

# log_filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# logging.basicConfig(
#    filename=f"{log_filename}.log",
#    format="%(asctime)s: %(levelname)s: %(message)s",
#    level=logging.INFO
# )

logger = logging.getLogger(__name__)


class WebDriverListener(AbstractEventListener):

    def __init__(self):
        self.logger = logger

    def before_navigate_to(self, url, driver):
        self.logger.info(f"Navigating to {url}")

    def after_navigate_to(self, url, driver):
        self.logger.info(f"Navigated to {url}")

    def before_find(self, by, value, driver):
        self.logger.info(f"Searching for element by {by} {value}")

    def after_find(self, by, value, driver):
        self.logger.info(f"Element by {by} {value} found")

    def before_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info(f"Clicking on {element.get_attribute('class')}")
        else:
            self.logger.info(f"Clicking on {element.get_attribute('text')}")

    def after_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info(f"{element.get_attribute('class')} clicked")
        else:
            self.logger.info(f"{element.get_attribute('text')} clicked")

    def before_quit(self, driver):
        self.logger.info("Driver quitting")

    def after_quit(self, driver):
        self.logger.info("Driver quitted")

    def on_exception(self, exception, driver):
        self.logger.info(exception)

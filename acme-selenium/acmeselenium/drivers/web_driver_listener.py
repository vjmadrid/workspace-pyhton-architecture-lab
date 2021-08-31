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
        self.logger.info("Navigating to %s", url)

    def after_navigate_to(self, url, driver):
        self.logger.info("Navigated to %s", url)

    def before_find(self, by, value, driver):
        self.logger.info("Searching for element by %s %s", by, value)

    def after_find(self, by, value, driver):
        self.logger.info("Element by %s %s found", by, value)

    def before_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info("Clicking on %s", element.get_attribute('class'))
        else:
            self.logger.info("Clicking on %s", element.get_attribute('text'))

    def after_click(self, element, driver):
        if element.get_attribute("text") is None:
            self.logger.info("%s clicked", element.get_attribute('class'))
        else:
            self.logger.info("%s clicked", element.get_attribute('text'))

    def before_quit(self, driver):
        self.logger.info("Driver quitting")

    def after_quit(self, driver):
        self.logger.info("Driver quitted")

    def on_exception(self, exception, driver):
        self.logger.info(exception)

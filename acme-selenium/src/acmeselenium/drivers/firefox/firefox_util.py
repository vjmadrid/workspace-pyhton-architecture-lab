# -*- coding: utf-8 -*-


import logging

from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager


logger = logging.getLogger(__name__)


DEFAULT_FIREFOX_DRIVER_PATH = "/usr/local/bin/geckodriver"


def setup_driver_firefox_gecko(options=None):
    logger.debug("[SETUP] [setup_driver_firefox_gecko] Setup Driver Firefox Gecko ...")

    if options is None:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

    return driver


def setup_driver_firefox(executable_path, options=None):
    logger.debug("[SETUP] [setup_driver_firefox] Setup Driver Firefox ...")

    if options is None:
        driver = webdriver.Firefox(executable_path=executable_path)
    else:
        driver = webdriver.Firefox(executable_path=executable_path, options=options)

    return driver

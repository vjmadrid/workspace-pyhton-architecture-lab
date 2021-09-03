# -*- coding: utf-8 -*-

import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


logger = logging.getLogger(__name__)


DEFAULT_CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"


def enable_download_headless(browser, download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_dir
        }
    }

    browser.execute("send_command", params)


def setup_driver_chrome_chromedriver(options=None):
    logger.debug("[SETUP] [setup_driver_firefox_gecko] Setup Driver Firefox Gecko ...")

    if options is None:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    return driver


def setup_driver_chrome(executable_path, options=None):
    logger.debug("[SETUP] [setup_driver_chrome] Setup Driver Chrome ...")

    if options is None:
        driver = webdriver.Chrome(executable_path=executable_path)
    else:
        driver = webdriver.Chrome(executable_path=executable_path, options=options)

    return driver

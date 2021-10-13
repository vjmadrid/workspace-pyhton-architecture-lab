# -*- coding: utf-8 -*-

import logging

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


logger = logging.getLogger(__name__)


def enable_download_headless(chrome_driver, download_dir):
    """Configure a Chrome browser to enable downloading in headless mode

    :param chrome_driver: Chrome-based Web Driver
    :type chrome_driver: WebDriver

    :param options: Driver download path
    :type options: str

    :raises ValueError: Invalid parameter

    :return: N/A
    :rtype: N/A
    """

    if chrome_driver is None:
        raise ValueError('executable_path is an invalid parameter')

    if download_dir is None:
        raise ValueError('download_dir is an invalid parameter')

    chrome_driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_dir
        }
    }

    chrome_driver.execute("send_command", params)


def setup_driver_chrome(executable_path, options_dict=None):
    """Returns a web driver for Chrome configured from an installation

    :param executable_path: Web driver executable installation path
    :type executable_path: str (Optional)

    :param options: Configuration options for Chrome, defaults to None
    :type options: Options

    :raises ValueError: Invalid parameter

    :return: Driver configured for Chrome
    :rtype: WebDriver
    """

    if executable_path is None:
        raise ValueError('executable_path is an invalid parameter')

    logger.debug("[SETUP] [setup_driver_chrome] Setup Driver Chrome ...")

    if options_dict is None:
        driver = webdriver.Chrome(executable_path=executable_path)
    else:
        driver = webdriver.Chrome(executable_path=executable_path, options=options_dict)

    return driver


def setup_driver_chrome_chromedriver(options_dict=None):
    """Returns a web driver for Chrome configured from a dependency (provided by default)

    :param options_dict: Configuration options for Chrome, defaults to None
    :type options_dict: Options

    :return: Driver configured for Chrome
    :rtype: WebDriver
    """

    logger.debug("[SETUP] [setup_driver_firefox_gecko] Setup Driver Firefox Gecko ...")

    return setup_driver_chrome(ChromeDriverManager().install(), options_dict)

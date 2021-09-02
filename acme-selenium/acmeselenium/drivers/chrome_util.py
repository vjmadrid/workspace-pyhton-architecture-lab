# -*- coding: utf-8 -*-

import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from webdriver_manager.chrome import ChromeDriverManager


logger = logging.getLogger(__name__)


# ********************
#    Setup Chrome
# ********************

DEFAULT_CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"
DEFAULT_FIREFOX_DOWNLOAD_FOLDER = "/Users/vjmadrid/Downloads/"


def setup_driver_chrome():
    logger.debug("[SETUP] [setp_driver_chrome] Setup Driver Chrome ...")

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "normal"

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # return webdriver.Chrome(chrome_options=chrome_options)

    return webdriver.Chrome(desired_capabilities=caps)


def setup_driver_chrome_install():
    logger.debug("[SETUP] [setup_driver_chrome_install] Setup Driver Chrome with Install ...")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


def setup_driver_chrome_headless():
    logging.getLogger().debug(
        "[SETUP] [setup_driver_chrome_headless] Setup Driver Chrome Headless ..."
    )

    options = Options()
    # options.add_argument('headless')
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    # prefs["profile.default_content_settings.popups"]=0
    # prefs["download.default_directory"]=downloadPath
    # options.add_experimental_option("prefs", prefs)
    #browser = webdriver.Chrome(options=options, executable_path=CHROMEDRIVER_PATH)

    # options.add_argument('--ignore-ssl-errors=yes')
    # options.add_argument('--ignore-certificate-errors')

    return webdriver.Chrome(options=options, executable_path=DEFAULT_CHROME_DRIVER_PATH)

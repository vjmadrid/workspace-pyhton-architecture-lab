# -*- coding: utf-8 -*-


import os

from selenium import webdriver

from acmeselenium.constants import driver_constant


def default_chrome_options():
    """Performs the default configuration of a Chrome WebDriver

    :return: Default configuration options for a Chrome WebDriver
    :rtype: Options
    """

    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("disable-infobars")

    return options


def custom_chrome_options(options_dict):
    """Performs the custom configuration of a Chrome WebDriver

    Example
        example_options_dict = {
            'headless': False,
            'download_path': 'xxx',
            'file_type': 'audio/mp3'
        }

    :param options_dict: Dictionary with all parameters of this method
    :type options_dict: dict

    :raises ValueError: Invalid parameter

    :return: Custom configuration options for a Chrome WebDriver
    :rtype: Options
    """

    if options_dict is None:
        raise ValueError('options_dict is an invalid parameter')

    options = webdriver.ChromeOptions()

    # Configuration Default
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("disable-infobars")

    # Configuration Headless
    if driver_constant.HEADLESS_KEY in options_dict:
        if options_dict['headless']:
            options.add_argument("--headless")
        else:
            options.add_argument('--start-maximized')
            options.add_argument('--window-size=1920,1080')
    else:
        options.add_argument('--start-maximized')
        options.add_argument('--window-size=1920,1080')

    # Configuracion Download
    if driver_constant.DOWNLOAD_PATH_KEY in options_dict:
        download_path = options_dict[driver_constant.DOWNLOAD_PATH_KEY]

        # Create if not exist
        if not os.path.isdir(download_path):
            os.makedirs(download_path)

        prefs = {}
        prefs["profile.default_content_settings.popups"] = 0
        prefs["download.prompt_for_download"] = False
        prefs["download.directory_upgrade"] = True
        prefs["safebrowsing_for_trusted_sources_enabled"] = False
        prefs["safebrowsing.enabled"] = False
        prefs["download.default_directory"] = download_path

        options.add_experimental_option("prefs", prefs)

    return options

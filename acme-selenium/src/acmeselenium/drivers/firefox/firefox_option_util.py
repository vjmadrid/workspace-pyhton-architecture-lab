# -*- coding: utf-8 -*-


import os

from selenium import webdriver

from acmeselenium.constants import driver_constant


def action_direct_download(firefox_options, download_path, file_types):
    """Performs the default configuration of a Chrome WebDriver

    :param firefox_options: Browser options to complete
    :type firefox_options: Options

    :param download_path: String with browser download path
    :type download_path: Options

    :param file_types: String with the types of files allowed for downloading
    :type file_types: Options

    :raises ValueError: Invalid parameter

    :return: Custom configuration options for a Chrome WebDriver
    :rtype: Options
    """

    if firefox_options is None:
        raise ValueError('firefox_options is an invalid parameter')

    if download_path is None:
        raise ValueError('download_path is an invalid parameter')

    if file_types is None:
        raise ValueError('file_types is an invalid parameter')

    # Create if not exist
    if not os.path.isdir(download_path):
        os.makedirs(download_path)

    firefox_options.set_preference("browser.download.folderList", 2)
    firefox_options.set_preference("browser.download.dir", download_path)
    firefox_options.set_preference("browser.download.manager.showWhenStarting", False)

    if file_types is None:
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", driver_constant.DEFAULT_SAVE_TO_DISK_FILE_TYPES)
    else:
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", file_types)


def default_firefox_options(download_path):
    """Performs the default configuration of a Firefox WebDriver

    :return: Default configuration options for a Firefox WebDriver
    :rtype: Options
    """

    if download_path is None:
        raise ValueError('download_path is an invalid parameter')

    options = webdriver.FirefoxOptions()
    options.headless = True
    options.set_preference("dom.webnotifications.enabled", False)
    action_direct_download(options, download_path, driver_constant.DEFAULT_SAVE_TO_DISK_FILE_TYPES)

    return options


def custom_firefox_options(options_dict):
    """Performs the custom configuration of a Firefox WebDriver

    Example
        example_options_dict = {
            'user_data_path': xxx,      # Optional
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

    options = webdriver.FirefoxOptions()

    # Configuration Headless
    if driver_constant.HEADLESS_KEY in options_dict:
        if options_dict[driver_constant.HEADLESS_KEY]:
            options.headless = options_dict[driver_constant.HEADLESS_KEY]

    # Configuration Notifications
    options.set_preference("dom.webnotifications.enabled", False)

    # Configuracion Download
    if driver_constant.DOWNLOAD_PATH_KEY in options_dict:
        download_path = options_dict[driver_constant.DOWNLOAD_PATH_KEY]

        if driver_constant.FILE_TYPES_KEY in options_dict:
            action_direct_download(options, download_path, options_dict[driver_constant.FILE_TYPES_KEY])
        else:
            action_direct_download(options, download_path, driver_constant.DEFAULT_SAVE_TO_DISK_FILE_TYPES)

    # Configuration User Data
    if driver_constant.USER_DATA_PATH_KEY in options_dict:
        user_data_path = options_dict[driver_constant.USER_DATA_PATH_KEY]
        if user_data_path:
            options.profile = user_data_path

    return options

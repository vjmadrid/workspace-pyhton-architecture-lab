# -*- coding: utf-8 -*-


import os


from selenium import webdriver
from acmeselenium.constants import driver_constant


def action_direct_download(options, custom_download_path, file_types):
    if options is None:
        raise ValueError('custom_download_path invalid')

    if custom_download_path is None:
        raise ValueError('custom_download_path invalid')

    if file_types is None:
        raise ValueError('file_types invalid')

    # Create if not exist
    if not os.path.isdir(custom_download_path):
        os.makedirs(custom_download_path)

    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", custom_download_path)
    options.set_preference("browser.download.manager.showWhenStarting", False)

    if file_types is None:
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", driver_constant.DEFAULT_SAVE_TO_DISK_FILE_TYPES)
    else:
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", file_types)


def default_firefox_options(options_dict):

    if options_dict is None:
        raise ValueError('Options invalid')

    options = webdriver.FirefoxOptions()
    options.headless = options_dict[driver_constant.HEADLESS_KEY]

    # Notifications
    options.set_preference("dom.webnotifications.enabled", False)

    # Direct Download
    if driver_constant.CUSTOM_DOWNLOAD_PATH_KEY in options_dict:
        custom_download_path = options_dict[driver_constant.CUSTOM_DOWNLOAD_PATH_KEY]

        if driver_constant.FILE_TYPES_KEY in options_dict:
            action_direct_download(options, custom_download_path, options_dict[driver_constant.FILE_TYPES_KEY])
        else:
            action_direct_download(options, custom_download_path, driver_constant.DEFAULT_SAVE_TO_DISK_FILE_TYPES)

    return options


def default_firefox_options_min(custom_download_path):
    options = webdriver.FirefoxOptions()
    options.headless = True

    # Notifications
    options.set_preference("dom.webnotifications.enabled", False)

    # Download
    action_direct_download(options, custom_download_path, driver_constant.DEFAULT_SAVE_TO_DISK_FILE_TYPES)

    return options

# -*- coding: utf-8 -*-


import os


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

DEFAULT_DOWNLOAD_FOLDER = "/Users/vjmadrid/Downloads/"

SAVE_TO_DISK_FILE_TYPE = 'audio/mp3'

'''
example_options_dict = {
    'headless': False,
    'custom_download_path': 'xxx',
    'file_type': 'audio/mp3'
}
'''


def default_firefox_options(options_dict):

    if options_dict is None:
        raise ValueError('Options invalid')

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.headless = options_dict['headless']

    # Notifications
    firefox_options.set_preference("dom.webnotifications.enabled", False)

    # Direct Download
    custom_download_path = options_dict['custom_download_path']
    if custom_download_path is not None:

        # Create if not exist
        if not os.path.isdir(custom_download_path):
            os.makedirs(custom_download_path)

        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference("browser.download.dir", custom_download_path)
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", options_dict['file_type'])

    return firefox_options


def default_firefox_options_basic():
    options = Options()
    options.headless = True

    # Notifications
    options.set_preference("dom.webnotifications.enabled", False)

    # Download
    options.set_preference("browser.download.dir", DEFAULT_DOWNLOAD_FOLDER)
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/mp3")

    # options.add_argument("--window-size=1920,1200")

    # options.add_argument('--ignore-ssl-errors=yes')
    # options.add_argument('--ignore-certificate-errors')
    return options

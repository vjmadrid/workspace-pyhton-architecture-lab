# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


DEFAULT_DOWNLOAD_FOLDER = "/Users/vjmadrid/Downloads/"
SAVE_TO_DISK_FILE_TYPE = 'audio/mp3'


'''
example_options_dict = {
    'headless': False,
    'custom_download_path': 'xxx',
    'file_type': 'audio/mp3'
}
'''


def default_chrome_options_basic():
    chrome_options = Options()

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DEFAULT_DOWNLOAD_FOLDER,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True})

    return chrome_options


def default_chrome_options_min():
    chrome_options = Options()

    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')

    return chrome_options


def default_chrome_options(options_dict):

    if options_dict is None:
        raise ValueError('Options invalid')

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.headless = options_dict['headless']

    #if options_dict['headless'] == True:
    chrome_options.add_argument("--headless")

    # chrome_options.add_argument('--disable-download-notification')
    # chrome_options.add_argument('--start-maximized')
    #  chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--window-size=1920x1080")
    # chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--verbose')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--disable-software-rasterizer')

    # custom_download_path = options_dict['custom_download_path']
    # if custom_download_path is not None:

    #     # Create if not exist
    #     if not os.path.isdir(custom_download_path):
    #         os.makedirs(custom_download_path)

    #     prefs = {}
    #     prefs["profile.default_content_settings.popups"] = 0
    #     prefs["download.prompt_for_download"] = False
    #     prefs["download.directory_upgrade"] = True
    #     prefs["safebrowsing_for_trusted_sources_enabled"] = False
    #     prefs["safebrowsing.enabled"] = False
    #     prefs["download.default_directory"] = custom_download_path

    #     chrome_options.add_experimental_option("prefs", prefs)

    return chrome_options

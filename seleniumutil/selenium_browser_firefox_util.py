
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



# ********************
#    Setup Firefox
# ********************

DEFAULT_FIREFOX_DRIVER_PATH = '/usr/local/bin/geckodriver'
DEFAULT_FIREFOX_DOWNLOAD_FOLDER = '/Users/vjmadrid/Downloads/'


def setUpDriverFirefox(logger):
    logger.debug("[SETUP] [setUpDriverFirefox] Setup Driver Firefox ...")

    caps = DesiredCapabilities().FIREFOX

    profile = webdriver.FirefoxProfile()
    profile.set_preference("webdriver_assume_untrusted_issuer", False)
    profile.update_preferences()
    
    return webdriver.Firefox(capabilities=caps, firefox_profile=profile)



def setUpDriverFirefoxHeadless(logger):
    logger.debug("[SETUP] [setUpDriverFirefoxHeadless] Setup Driver Firefox Headless ...")

    options = Options()
    #options.headless = True

    # Notifications
    options.set_preference("dom.webnotifications.enabled", False)

    # Download
    #options.set_preference("browser.download.dir", DEFAULT_FIREFOX_DOWNLOAD_FOLDER)
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/mp3")

    #options.add_argument("--window-size=1920,1200")

    #options.add_argument('--ignore-ssl-errors=yes')
    #options.add_argument('--ignore-certificate-errors')

    return webdriver.Firefox(executable_path=DEFAULT_FIREFOX_DRIVER_PATH, options=options)


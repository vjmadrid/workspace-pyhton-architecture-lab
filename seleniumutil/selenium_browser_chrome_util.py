
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from seleniumutil import selenium_navigation_util

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



DEFAULT_CHROME_DRIVER_PATH = '/usr/local/bin/chromedriver'
DEFAULT_FIREFOX_DRIVER_PATH = '/usr/local/bin/geckodriver'



def setUpDriverChrome():
    print ("INFO. ["+time.strftime("%H:%M:%S")+"] [setUpDriverChrome] setUp Driver...")

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "normal"
    
    return webdriver.Chrome(desired_capabilities=caps)


def setUpDriverChromeHeadless():
    print ("INFO. ["+time.strftime("%H:%M:%S")+"] [setUpDriverChromeHeadless] setUp Driver...")

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    #options.add_argument('--ignore-ssl-errors=yes')
    #options.add_argument('--ignore-certificate-errors')

    return webdriver.Chrome(options=options, executable_path=DEFAULT_CHROME_DRIVER_PATH)


def setUpDriverFirefox():
    print ("INFO. ["+time.strftime("%H:%M:%S")+"] [setUpDriverFirefox] setUp Driver...")

    caps = DesiredCapabilities().FIREFOX
    profile = webdriver.FirefoxProfile()
    profile.set_preference("webdriver_assume_untrusted_issuer", False)
    profile.update_preferences()
    
    return webdriver.Firefox(capabilities=caps,firefox_profile=profile)



def setUpDriverFirefoxHeadless(logger):
    logger.info("[setUpDriverFirefoxHeadless] setUp Driver Firefox Headless...")

    options = Options()
    options.headless = True
    #options.add_argument("--window-size=1920,1200")

    #options.add_argument('--ignore-ssl-errors=yes')
    #options.add_argument('--ignore-certificate-errors')

    return webdriver.Firefox(executable_path=DEFAULT_FIREFOX_DRIVER_PATH)



import logging
from acmecommon.common.logging import logger
from acmeselenium.selenium.drivers import firefox_util
from acmeselenium.selenium.utils import navigation_util


# ********************
#    Setup Logging
# ********************


LOG_PATH = './log/'
LOG_FILE_NAME = 'example.log'
LOG_MODE = 'TEST'
LOG_MAIN_LEVEL = logging.INFO

logger.setup_logging(LOG_PATH, LOG_FILE_NAME, LOG_MODE, LOG_MAIN_LEVEL)

logger = logging.getLogger(__name__)


# ********************
#   Setup Selenium
# ********************

SELENIUM_CONFIG_DELAY_DEFAULT = 5
SELENIUM_CONFIG_MAX_RETRY_DEFAULT = 3


# ***********************
#   Execution
# **********************


logging.getLogger().info('*** LAB ***')

browser = firefox_util.setup_driver_firefox_headless()

# browser = DriverFactory.get_driver_firefox(headless_mode=False)

navigation_util.go_to_url(browser, "https://es.wikipedia.org/wiki/Wikipedia:Portada")

input("Please press the Enter key to proceed")

# logging.getLogger().info("*** END ***")
browser.quit()

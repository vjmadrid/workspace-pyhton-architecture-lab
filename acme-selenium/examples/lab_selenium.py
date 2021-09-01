import logging

from acmeselenium.drivers import firefox_util
from acmeselenium.drivers.driver_factory import DriverFactory
from acmeselenium.utils import navigation_util, verification_util


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ********************
#   Setup Selenium
# ********************

SELENIUM_CONFIG_DELAY_DEFAULT = 5
SELENIUM_CONFIG_MAX_RETRY_DEFAULT = 3


# ***********************
#   Execution
# **********************


logger.info("*** LAB Selenium ***")

# Option 1
# browser = firefox_util.setup_driver_firefox_headless()

# Option 2
# browser = DriverFactory.get_driver_firefox(headless_mode=False)

# Option 3 : Default static values
config = {}
config['browser'] = 'firefox'
config['headless_mode'] = True

browser = DriverFactory.get_driver(config['browser'], config['headless_mode'])

navigation_util.go_to_url(browser, "https://es.wikipedia.org/wiki/Wikipedia:Portada")

verification_util.verify_valid_url_with_exit(browser, "https://es.wikipedia.org/wiki/Wikipedia:Portada", False)

logger.info("*** END ***")
browser.quit()

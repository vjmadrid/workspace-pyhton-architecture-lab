import logging
from acme.common.logging import logger


# ********************
#    Setup Logging
# ********************

LOG_PATH = "./logs/"
LOG_FILE_NAME = "example"
LOG_MODE = "TEST"
LOG_MAIN_LEVEL = logging.INFO

logger.setup_logging(LOG_PATH, LOG_FILE_NAME, LOG_MODE, LOG_MAIN_LEVEL)

logger = logging.getLogger(__name__)

for index in range(20):
    logger.info("Test Message -> " + str(index))

logger.error("Ejemplo de error")

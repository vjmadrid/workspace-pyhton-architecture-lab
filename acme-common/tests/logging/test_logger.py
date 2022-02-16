# -*- coding: utf-8 -*-


import unittest
import logging

from src.acmecommon.logging.logger import Logger
import src.acmecommon.logging.logger_constant as logger_constant


LOG_PATH = "./logs/"
LOG_FILE_NAME = "example"
LOG_MAIN_LEVEL = logging.INFO
ENABLE_CONSOLE = True
ENABLE_NOTIFICATIONS_KEY = False

EXAMPLE_OPTIONS_DICT = {
    logger_constant.LOGGING_SERVICE_NAME_KEY: "test",
    logger_constant.LOGGING_PATH_KEY: LOG_PATH,
    logger_constant.LOGGING_FILE_NAME_KEY: LOG_FILE_NAME,
    logger_constant.LOGGING_MAIN_LEVEL_KEY: LOG_MAIN_LEVEL,
    logger_constant.ENABLE_CONSOLE_KEY: ENABLE_CONSOLE,
    logger_constant.ENABLE_NOTIFICATIONS_KEY: ENABLE_NOTIFICATIONS_KEY
}

class TestNumberUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_logging(self):
        logger = Logger(EXAMPLE_OPTIONS_DICT)

        for index in range(20):
            logger.info("Test Message -> " + str(index))

        logger.error("Ejemplo de error")


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-


import logging
import datetime
import os
from logging.handlers import RotatingFileHandler


loggers = {}


LOG_FILE_FORMATTER = logging.Formatter(
    "[%(levelname)s]:%(asctime)s:%(module)s:%(lineno)d:%(name)s:%(message)s"
)
LOG_CONSOLE_FORMATTER = logging.Formatter("[%(levelname)s]: %(message)s")


def setup_logging(log_path, log_file_name, log_mode, log_main_level):

    logger = logging.getLogger()
    logger.setLevel(log_main_level)

    # log_filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    now = datetime.datetime.now().strftime("%Y%m%d")

    file_name = "{0}/{1}-{2}.log".format(log_path, log_file_name, now)
    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(LOG_FILE_FORMATTER)

    debug_file_name = "{0}/debug_{1}-{2}.log".format(log_path, log_file_name, now)
    debug_file_handler = RotatingFileHandler(
        debug_file_name, maxBytes=10 ** 6, backupCount=5
    )
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(LOG_FILE_FORMATTER)

    error_file_name = "{0}/error_{1}-{2}.log".format(log_path, log_file_name, now)
    errors_file_handler = RotatingFileHandler(
        error_file_name, maxBytes=10 ** 6, backupCount=5
    )
    errors_file_handler.setLevel(logging.WARNING)
    errors_file_handler.setFormatter(LOG_FILE_FORMATTER)

    if log_mode == "TEST":
        # Console_handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(LOG_CONSOLE_FORMATTER)
        logger.addHandler(console_handler)

    logger.addHandler(file_handler)
    logger.addHandler(debug_file_handler)
    logger.addHandler(errors_file_handler)

    return logger


def log(text, level=logging.INFO, name="WDM", formatter="[%(name)s] - %(message)s"):
    log_level = os.getenv("SONG-SCRAPER_LOG_LEVEL")

    if log_level:
        level = int(log_level)

    if loggers.get(name):
        loggers.get(name).info(text)
    else:
        _logger = logging.getLogger(name)

        handler = logging.StreamHandler()
        formatter = logging.Formatter(formatter)
        handler.setFormatter(formatter)
        _logger.addHandler(handler)
        _logger.setLevel(level)
        loggers[name] = _logger
        _logger.info(text)

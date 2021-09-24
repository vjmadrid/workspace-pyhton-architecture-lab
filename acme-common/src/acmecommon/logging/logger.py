# -*- coding: utf-8 -*-


import logging
import datetime
import os
from logging.handlers import RotatingFileHandler

import yaml


loggers = {}


LOG_FILE_FORMATTER = logging.Formatter(
    "[%(levelname)s]:%(asctime)s:%(module)s:%(lineno)d:%(name)s:%(message)s"
)
LOG_CONSOLE_FORMATTER = logging.Formatter("[%(levelname)s]: %(message)s")

LOG_YAML_CONFIG_FILE_DEFAULT = 'logging.yaml'


def setup_logging(log_path, log_file_name, log_mode, log_main_level):

    # Option : Load Environment Var
    # log_level = os.getenv("SONG-SCRAPER_LOG_LEVEL")
    # if log_level:
    #   level = int(log_level)
    #   logger.setLevel(log_main_level)

    logger = logging.getLogger()
    logger.setLevel(log_main_level)

    # log_filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    now = datetime.datetime.now().strftime("%Y%m%d")

    file_name = f"{log_path}/{log_file_name}-{now}.log"
    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(LOG_FILE_FORMATTER)

    debug_file_name = f"{log_path}/debug_{log_file_name}-{now}.log"
    debug_file_handler = RotatingFileHandler(
        debug_file_name, maxBytes=10 ** 6, backupCount=5
    )
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(LOG_FILE_FORMATTER)

    error_file_name = f"{log_path}/error_{log_file_name}-{now}.log"
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

    # Add logger with name
    loggers['song-scraper'] = logger

    return logger


def setup_logging_with_config_yaml(
    default_path=LOG_YAML_CONFIG_FILE_DEFAULT,
    default_level=logging.INFO,
    env_key='LOG_CFG'
):

    path = default_path
    value = os.getenv(env_key, None)

    if value:
        path = value

    if os.path.exists(path):
        with open(path, 'rt', encoding="utf-8") as file_handler:
            config = yaml.safe_load(file_handler.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

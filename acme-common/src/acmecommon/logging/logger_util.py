# -*- coding: utf-8 -*-


import logging
import os
import yaml


from . import logger_constant


loggers = {}


def setup_logging_with_config_yaml(
    default_path=logger_constant.LOG_YAML_CONFIG_FILE_DEFAULT,
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

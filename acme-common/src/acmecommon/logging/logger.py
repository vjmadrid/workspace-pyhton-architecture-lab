# -*- coding: utf-8 -*-


import logging
import datetime
from logging.handlers import RotatingFileHandler


from . import logger_constant
from src.acmecommon.utils.validation_util import ValidationUtil
from src.acmecommon.notifications.notification import NotificationHandler


class Logger:

    logger = None
    NotificationHandler = None

    def __init__(self, params_dict):
        """

        Example
            example_params_dict = {
                'logging_service_name': xxx,
                'logging_path': xxx,
                'logging_file_name': xxx,
                'logging_main_level': 'xxx',
                'enable_console': 'xxx',
                'enable_notifications': 'xxx'
            }

        :param params_dict: Dictionary with all parameters of this method
        :type params_dict: dict

        :raises ValueError: Invalid parameter

        :return: N/A
        :rtype: N/A
        """

        ValidationUtil.is_dict_valid_with_exception(params_dict)

        logging_path = params_dict[logger_constant.LOGGING_PATH_KEY]
        logging_file_name = params_dict[logger_constant.LOGGING_FILE_NAME_KEY]

        enable_console = params_dict[logger_constant.ENABLE_CONSOLE_KEY]

        # General setup
        LOGGING_FILE_FORMATTER = logging.Formatter(logger_constant.LOGGING_FILE_FORMATTER_PATTERN_DEFAULT)
        LOGGING_CONSOLE_FORMATTER = logging.Formatter(logger_constant.LOGGING_CONSOLE_FORMATTER_PATTERN_DEFAULT)
        now = datetime.datetime.now().strftime("%Y%m%d")

        # Logger setup
        if logger_constant.LOGGING_SERVICE_NAME_KEY not in params_dict:
            logging_service_name = ""
            logger_name = ""
            self.logger = logging.getLogger()
        else:
            logging_service_name = params_dict[logger_constant.LOGGING_SERVICE_NAME_KEY]
            logger_name = f"{logging_service_name}_logger"
            self.logger = logging.getLogger(logger_name)

        # Logging Level setup
        if logger_constant.LOGGING_MAIN_LEVEL_KEY not in params_dict:
            self.logger.setLevel(logging.INFO)
        else:
            logging_main_level = params_dict[logger_constant.LOGGING_MAIN_LEVEL_KEY]
            self.logger.setLevel(logging_main_level)

        self.logger.propagate = False

        # Loggging to file setup

        # * Info Logging to file
        file_name = f"{logging_path}/{logging_file_name}-{now}.log"
        file_handler = logging.FileHandler(file_name)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(LOGGING_FILE_FORMATTER)
        self.logger.addHandler(file_handler)

        # * Debug Logging to file
        debug_file_name = f"{logging_path}/debug_{logging_file_name}-{now}.log"
        debug_file_handler = RotatingFileHandler(
            debug_file_name, maxBytes=10 ** 6, backupCount=5
        )
        debug_file_handler.setLevel(logging.DEBUG)
        debug_file_handler.setFormatter(LOGGING_FILE_FORMATTER)
        self.logger.addHandler(debug_file_handler)

        # Error Logging to file
        error_file_name = f"{logging_path}/error_{logging_file_name}-{now}.log"
        errors_file_handler = RotatingFileHandler(
            error_file_name, maxBytes=10 ** 6, backupCount=5
        )
        errors_file_handler.setLevel(logging.WARNING)
        errors_file_handler.setFormatter(LOGGING_FILE_FORMATTER)
        self.logger.addHandler(errors_file_handler)

        # Logging to console
        if enable_console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(LOGGING_CONSOLE_FORMATTER)
            self.logger.addHandler(console_handler)

        # Notification handler config
        if logger_constant.ENABLE_NOTIFICATIONS_KEY not in params_dict:
            NotificationHandler = None
        else:
            enable_notifications = params_dict[logger_constant.ENABLE_NOTIFICATIONS_KEY]
            self.NotificationHandler = None # NotificationHandler(enable_notifications)


    def log(self, message, level="info", notification=False):

        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "debug":
            self.logger.debug(message)

        # if notification and self.NotificationHandler.enabled:
        #     self.NotificationHandler.send_notification(str(message))

    def info(self, message, notification=True):
        self.log(message, "info", notification)

    def warning(self, message, notification=True):
        self.log(message, "warning", notification)

    def error(self, message, notification=True):
        self.log(message, "error", notification)

    def debug(self, message, notification=False):
        self.log(message, "debug", notification)

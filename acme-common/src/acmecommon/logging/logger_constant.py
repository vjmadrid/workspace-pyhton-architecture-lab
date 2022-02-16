# -*- coding: utf-8 -*-


LOGGING_SERVICE_NAME_KEY = "logging_service_name"
LOGGING_PATH_KEY = "logging_path"
LOGGING_FILE_NAME_KEY = "logging_file_name"
LOGGING_MAIN_LEVEL_KEY = "logging_main_level"


ENABLE_CONSOLE_KEY = "enable_console"
ENABLE_NOTIFICATIONS_KEY = "enable_notifications"


LOGGING_FILE_FORMATTER_PATTERN_DEFAULT = "[%(levelname)s]:%(asctime)s:%(module)s:%(lineno)d:%(name)s:%(message)s"
LOGGING_CONSOLE_FORMATTER_PATTERN_DEFAULT = "[%(levelname)s]: %(message)s"


LOGGING_YAML_CONFIG_FILE_DEFAULT = 'logging.yaml'

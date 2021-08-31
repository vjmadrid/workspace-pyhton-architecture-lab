# -*- coding: utf-8 -*-


import logging


logger = logging.getLogger(__name__)


def show_error_message(test_mode, message):
    config_parameters = (
        '{ "test_mode":' + str(test_mode) + ', "message":' + str(message) + "}"
    )
    logger.debug(
        "[TEST] [show_error_message] Show Error Message ... -> Parameters :%s", config_parameters
    )

    if test_mode:
        assert False, str(message)
    else:
        logger.error(str(message))

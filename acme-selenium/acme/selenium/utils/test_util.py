# -*- coding: utf-8 -*-


import logging


def show_error_message(test_mode, message):
    CONFIG_PARAMETERS = '{ "test_mode":' + str(test_mode) + ', "message":' + str(message) + '}'
    logging.getLogger().debug("[TEST] [show_error_message] Show Error Message ... -> Parameters : " + CONFIG_PARAMETERS)

    if (test_mode):
        assert False, str(message)
    else:
        logging.getLogger().error(str(message))

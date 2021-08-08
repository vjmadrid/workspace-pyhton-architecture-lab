
def showErrorMessage(logger, active_test_mode, message):
    CONFIG_PARAMETERS =  '{ "active_test_mode":' + str(active_test_mode) + ', "message":' + str(message) +'}'
    logger.debug("[TEST] [showErrorMessage] Show Error Message : "+ CONFIG_PARAMETERS)

    if (active_test_mode):
        assert False, str(message)
    else:
        logger.error(str(message))




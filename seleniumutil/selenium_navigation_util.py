######################################
#  FUNCIONES NAVEGACION              #
######################################

from seleniumutil import selenium_verification_util



def goToUrl(logger, driver, urlPage):
    CONFIG_PARAMETERS =  '{ "urlPage":' + str(urlPage) + '}'
    logger.info("[NAVIGATION] [goToUrl] Url : "+ CONFIG_PARAMETERS)

    driver.get(urlPage)
    selenium_verification_util.verifyValidURL(logger, driver, urlPage, False)




def goToPage(logger, driver, classPage):
    CONFIG_PARAMETERS =  '{ "classPage.NAME":' + str(classPage.NAME) + '}'
    logger.debug("[NAVIGATION] [goToPage] Class " + classPage.NAME)

    goToUrl(logger, driver, classPage.URL)



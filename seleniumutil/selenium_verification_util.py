##########################################
#        FUNCIONES VERIFICACION          #
##########################################

from selenium.webdriver.common.by import By
from seleniumutil import selenium_test_util


class UnderConstructionPage:

    NAME = "Under Construction Page"
    URL_PATH = "/maintenance"



def verifyIfExistByXpath(logger, driver, xpathElement):
    CONFIG_PARAMETERS =  '{ "xpathElement":' + str(xpathElement) + '}'
    logger.info("[VERIFICATION] [verifyIfExistByXpath] Verify Exist By XPath : "+ CONFIG_PARAMETERS)

    resultSelected = driver.find_elements(By.XPATH, xpathElement)
    return len(resultSelected) > 0



def verifyValidURL(logger, driver, definiedURL, active_test_mode):
    CONFIG_PARAMETERS =  '{ "definiedURL":'+str(definiedURL) + ', "active_test_mode":' + str(active_test_mode) +'}'
    logger.info("[VERIFICATION] [verifyValidURL] Verify Valid URL : "+ CONFIG_PARAMETERS)

    urlCheck = driver.current_url

    if UnderConstructionPage.URL_PATH in urlCheck:
        selenium_test_util.showErrorMessage(logger, active_test_mode, "ERROR. Under Construction Page")

    if not definiedURL in urlCheck:
        selenium_test_util.showErrorMessage(logger, active_test_mode, "ERROR. URL Target Page NOT contains " + definiedURL)




def verifyValidSpecificURL(driver, definiedURL):
    urlCheck = driver.current_url

    if not definiedURL in urlCheck:
        assert False, "ERROR. URL Target Page NOT contains " + definiedURL
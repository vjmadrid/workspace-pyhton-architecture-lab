# -*- coding: utf-8 -*-


TEST_FILE_DOWNLOAD_URL = 'http://demo.automationtesting.in/FileDownload.html'
INPUT_TEXT_AREA_CONTENT_FILE_ID = 'textbox'
GENERATE_FILE_BUTTON_ID = 'createTxt'
DOWNLOAD_FILE_LINK_ID = 'link-to-download'

TEST_CONTENT_FILE = "Hello World"
TEST_EXAMPLE_FILE = "info.txt"


def action_generate_and_download_file(driver):

    if driver is None:
        raise ValueError('driver invalid')

    driver.get(TEST_FILE_DOWNLOAD_URL)

    # Generate text file
    driver.find_element_by_id(INPUT_TEXT_AREA_CONTENT_FILE_ID) \
        .send_keys(TEST_CONTENT_FILE)
    driver.find_element_by_id(GENERATE_FILE_BUTTON_ID).click()
    driver.find_element_by_id(DOWNLOAD_FILE_LINK_ID).click()

# -*- coding: utf-8 -*-


def set_window_size_big(driver):
    SIZE_BIG = (1200, 900)
    driver.set_window_size(SIZE_BIG[0], SIZE_BIG[1])


def set_window_size_small(driver):
    SIZE_SMALL = (900, 600)
    driver.set_window_size(SIZE_SMALL[0], SIZE_SMALL[1])


def set_mobile_view(mobile, driver):
    if mobile:
        set_window_size_small(driver)
    else:
        set_window_size_big(driver)

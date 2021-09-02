# -*- coding: utf-8 -*-


def set_window_size_big(driver):
    size_big = (1200, 900)
    driver.set_window_size(size_big[0], size_big[1])


def set_window_size_small(driver):
    size_small = (900, 600)
    driver.set_window_size(size_small[0], size_small[1])


def set_mobile_view(mobile, driver):
    if mobile:
        set_window_size_small(driver)
    else:
        set_window_size_big(driver)

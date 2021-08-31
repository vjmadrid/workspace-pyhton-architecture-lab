# -*- coding: utf-8 -*-

import os
import time


SMALL_WAIT_SECONDS = float(os.getenv("SMALL_WAIT_SECONDS", str(2)))
MEDIUM_WAIT_SECONDS = float(os.getenv("MEDIUM_WAIT_SECONDS", str(4)))
LONG_WAIT_SECONDS = float(os.getenv("LONG_WAIT_SECONDS", str(8)))
EXTRA_LONG_WAIT_SECONDS = float(os.getenv("EXTRA_LONG_WAIT_SECONDS", str(16)))


def sleep(seconds):
    time.sleep(seconds)


def sleep_small():
    time.sleep(SMALL_WAIT_SECONDS)


def sleep_medium():
    time.sleep(MEDIUM_WAIT_SECONDS)


def sleep_long():
    time.sleep(LONG_WAIT_SECONDS)


def sleep_extra_long():
    time.sleep(EXTRA_LONG_WAIT_SECONDS)

# -*- coding: utf-8 -*-


import os
import time


def is_file_downloaded_and_delete(file_path):

    while not os.path.exists(file_path):
        time.sleep(1)

    if os.path.exists(file_path):
        os.remove(file_path)
        return True

    return False

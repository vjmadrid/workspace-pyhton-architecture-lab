# -*- coding: utf-8 -*-

import unittest
import os
from pathlib import Path
from acmecommon.common.utils.directory_util import DirectoryUtil


class TestDirectoryUtil(unittest.TestCase):

    def setUp(self):
        self.test_current_path = Path(os.path.dirname(os.path.realpath(__file__)))

        # current_directory = os.getcwd()
        # os.chdir('/home/varun')

    def test_get_files_directory(self):
        result_list = DirectoryUtil().get_files_directory(self.test_current_path)

        self.assertEqual(15, len(result_list))

    def test_get_files_directory_list(self):
        result_list = DirectoryUtil().get_files_directory_list(self.test_current_path)

        # for elem in result_list:
        #    print(elem)

        self.assertEqual(15, len(result_list))


if __name__ == '__main__':
    unittest.main()

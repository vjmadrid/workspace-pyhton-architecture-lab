# -*- coding: utf-8 -*-

import unittest
import os
from pathlib import Path

from src.acmecommon.utils.directory_util import DirectoryUtil


class TestDirectoryUtil(unittest.TestCase):

    def setUp(self):
        self.current_path = Path(os.path.dirname(os.path.realpath(__file__)))
        self.test_current_path = str(self.current_path) + "/test"

        print("current_path ::" + str(self.current_path))
        print("test_current_path ::" + str(self.test_current_path))

        # current_directory = os.getcwd()
        # os.chdir('/home/varun')

    def tearDown(self):
        pass

    def test_create_directory(self):
        DirectoryUtil.create_directory(self.test_current_path)

        self.assertTrue((os.path.exists(self.test_current_path)) and (os.path.isdir(self.test_current_path)))

        os.remove(self.test_current_path)

    def test_get_files_directory(self):
        result_list = DirectoryUtil.get_files_directory(self.current_path)

        self.assertEqual(17, len(result_list))

    def test_get_files_directory_list(self):
        result_list = DirectoryUtil.get_files_directory_list(self.current_path)

        # for elem in result_list:
        #    print(elem)

        self.assertEqual(17, len(result_list))


if __name__ == "__main__":
    unittest.main()

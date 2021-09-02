# -*- coding: utf-8 -*-


import unittest
import os
from pathlib import Path

from src.acmecommon.utils.file_util import FileUtil


class TestFileUtil(unittest.TestCase):

    TEST_FILE_NAME = "example.txt"

    def setUp(self):
        self.test_current_path = Path(os.path.dirname(os.path.realpath(__file__)))
        self.test_example_file_path = (
            self.test_current_path / TestFileUtil.TEST_FILE_NAME
        )

    def test_get_file_size(self):
        self.assertEqual(19, FileUtil().get_file_size(self.test_example_file_path))


if __name__ == "__main__":
    unittest.main()

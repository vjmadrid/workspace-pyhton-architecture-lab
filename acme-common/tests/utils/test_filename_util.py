# -*- coding: utf-8 -*-


import unittest

from src.acmecommon.utils.filename_util import FileNameUtil


class TestFileNameUtil(unittest.TestCase):

    TEST_FILENAME = "filename"
    TEST_EXT = "py"
    TEST_FILENAME_EXT = TEST_FILENAME + "." + TEST_EXT
    TEST_PATH = "/path/to/"
    TEST_PATH_FILENAME_EXT = TEST_PATH + TEST_FILENAME_EXT
    TEST_CONTENT_TYPE = "image/png"
    TEST_OTHER_FILENAME_EXT = "filename.png"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_extract_file_name(self):
        self.assertEqual(
            self.TEST_FILENAME_EXT,
            FileNameUtil(self.TEST_PATH_FILENAME_EXT).extract_file_name(),
        )

    def test_extract_extension(self):
        self.assertEqual(
            self.TEST_EXT, FileNameUtil(self.TEST_PATH_FILENAME_EXT).extract_extension()
        )

    def test_exclude_extension(self):
        self.assertEqual(
            self.TEST_FILENAME, FileNameUtil(self.TEST_FILENAME_EXT).exclude_extension()
        )

    def test_extract_directory(self):
        self.assertTrue(
            self.TEST_PATH,
            FileNameUtil(self.TEST_PATH_FILENAME_EXT).extract_directory(),
        )

    def test_get_content_type(self):
        self.assertTrue(
            self.TEST_CONTENT_TYPE,
            FileNameUtil(self.TEST_OTHER_FILENAME_EXT).get_content_type(),
        )


if __name__ == "__main__":
    unittest.main()

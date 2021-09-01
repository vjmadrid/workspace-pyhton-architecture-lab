# -*- coding: utf-8 -*-

from acmecommon.exceptions.common_exceptions import NotSupportedException


EXTENSION_DICT = {
    "png": "image/png",
    "jpg": "image/jpg",
    "jpeg": "image/jpeg",
    "gif": "image/gif",
    "bmp": "image/bmp",
    "tif": "image/tiff",
    "tiff": "image/tiff",
    "pdf": "application/pdf",
    "zip": "application/zip",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
}


class FileNameUtil:

    _string_value = ""
    _len_string_value = 0

    def __init__(self, string_value=""):
        self._string_value = str(string_value)
        self._len_string_value = len(self._string_value)

    def __del__(self):
        self._string_value = ""
        self._len_string_value = 0

    def extract_file_name(self):
        """
        usage:
            StringUtils('/path/to/filename.py').extract_file_name() returns 'filename.py'
        """
        result = ""
        if self._string_value:
            arr = self._string_value.split("/")
            result += arr[len(arr) - 1]

        return result

    def extract_extension(self):
        """
        usage:
            StringUtils('/path/to/filename.py').extract_extension() returns 'py'
        """
        arr = self._string_value.split(".")
        extension = arr[len(arr) - 1]
        return extension

    def exclude_extension(self):
        """
        usage:
            StringUtils('filename.py').exclude_extension() returns 'filename'
        """
        extension = self.extract_extension()
        if not extension:
            return None
        arr = self._string_value.split(extension)
        filename = arr[0][:-1]
        return filename

    def extract_directory(self):
        """
        usage:
            StringUtils('/path/to/filename.py').extract_extension() returns '/path/to/'
        """
        return self._string_value[: self._string_value.rfind("/") + 1]

    def get_content_type(self):
        """
        usage:
            StringUtils('filename.png').get_content_type() returns 'image/png'
        """

        extension = self.extract_extension()

        if EXTENSION_DICT[extension] is None:
            raise NotSupportedException(
                message="This extension[" + str(extension) + "] is not supported",
                errors={"code": "NOT_SUPPORTED_EXTENSION"},
            )

        return EXTENSION_DICT[extension]

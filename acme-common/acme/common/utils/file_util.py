# -*- coding: utf-8 -*-


import os
import re
import logging
from io import FileIO, BufferedReader, BufferedWriter


DEFAULT_ENCODING = "utf-8"


logger = logging.getLogger(__name__)


class FileUtil():

    def __init__(self, stream=None):
        if stream is not None:
            self.content = stream.content
            self.__stream = stream
            self.__temp_name = "driver"

    @property
    def filename(self) -> str:
        try:
            filename = re.findall("filename=(.+)", self.__stream.headers["content-disposition"])[0]
        except KeyError:
            filename = f"{self.__temp_name}.zip"
        except IndexError:
            filename = f"{self.__temp_name}.exe"

        if '"' in filename:
            filename = filename.replace('"', "")

        return filename

    # def save_file(file: File, directory: str):
    #    os.makedirs(directory, exist_ok=True)

    #    archive_path = f"{directory}{os.sep}{file.filename}"
    #    with open(archive_path, "wb") as code:
    #        code.write(file.content)
    #    return Archive(archive_path)

    def create_dirs(dirs):
        """
        dirs - a list of directories to create if these directories are not found
        :param dirs:
        :return:
        """
        try:
            for dir_ in dirs:
                if not os.path.exists(dir_):
                    os.makedirs(dir_)
        except Exception as err:
            logging.getLogger("Dirs Creator").info("Creating directories error: {0}".format(err))
            exit(-1)

    def copy_file_stream_to_file(self, file, to_path):
        self.copy_buffered_io_to_file(BufferedReader(file), to_path)

    def copy_buffered_io_to_file(self, buffered_io, file_path):
        os.makedirs(file_path[:file_path.rfind('/') + 1], exist_ok=True)
        with FileIO(file_path, mode='wb') as raw_output_io:
            with BufferedWriter(raw_output_io) as writer:
                while 1:
                    line = buffered_io.readline()
                    if not line:
                        break
                    writer.write(line)
        buffered_io.close()

    def is_file_empty(self, file_path):
        """
            Check if file is empty by confirming if its size is 0 bytes
        """

        return os.path.exists(file_path) and os.stat(file_path).st_size == 0

    def generate_list_by_file(self, file_path):
        result_list = []

        if os.path.isfile(file_path):
            count = 0
            my_file = open(file_path, "r", encoding=DEFAULT_ENCODING)

            with my_file as fps:
                for line in fps:
                    count += 1
                    result_list.append(line.strip())

            my_file.close()

        return result_list

    def create_file(self, file_path):
        if (not os.path.exists(file_path)) and os.path.isfile(file_path):
            with open(file_path, 'r', encoding=DEFAULT_ENCODING) as file_handler:
                file_handler.close()

    def create_file_with_handler(self, file_path, mode):
        if (not os.path.exists(file_path)) and os.path.isfile(file_path):
            with open(file_path, mode, encoding=DEFAULT_ENCODING) as file_handler:
                return file_handler

        return None

    def get_file_size(self, file_path):
        if os.path.isabs(file_path):
            return os.path.getsize(file_path)

        fn = os.path.join(os.path.dirname(__file__), file_path)
        return os.path.getsize(fn)

    def get_rel_path(self, file_path):
        return os.path.relpath(file_path)

    def add_in_file(self, file_path, value):
        try:
            with open(file_path, 'a', encoding=DEFAULT_ENCODING) as file_handler:
                file_handler.seek(0)
                file_handler.writelines(value + "\n")
        except Exception as excep:
            logger.error("Error in index adding: ", excep)

    def search_in_file(self, file_path, value):
        try:
            if value in open(file_path, 'r', encoding=DEFAULT_ENCODING).read():
                return True

        except Exception as excep:
            logger.error("Error in index searching : ", excep)

        return False

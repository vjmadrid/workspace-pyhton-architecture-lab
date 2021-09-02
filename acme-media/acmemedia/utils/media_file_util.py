# -*- coding: utf-8 -*-


import os
import re
import logging
import eyed3

from acmecommon.utils.file_util import FileUtil
from acmecommon.utils.filename_util import FileNameUtil


logger = logging.getLogger(__name__)


class MediaFileUtil:

    def __init__(self):
        pass

    def show(self, source_path):
        if os.path.exists(source_path):
            audio_file = eyed3.load(source_path)
            logger.info("* tag.artist :: [%s]", audio_file.tag.artist)
            logger.info("* tag.title :: [%s]", audio_file.tag.title)
            logger.info("* tag.album :: [%s]", audio_file.tag.album)
            logger.info("* tag.track_num :: [%s]", audio_file.tag.track_num)

    def rename(self, source_path, dest_path):

        if (os.path.exists(source_path)) and not os.path.exists(dest_path):
            audiofile = eyed3.load(source_path)

            file_name = FileNameUtil(source_path).extract_file_name()
            extension = FileNameUtil(source_path).extract_extension()
            directory = FileNameUtil(source_path).extract_directory()

            new_filename = directory +"/{0}-{1}" + "." + extension.format(audiofile.tag.artist, audiofile.tag.title)
            os.rename(source_path, new_filename)

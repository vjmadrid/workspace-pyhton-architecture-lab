# -*- coding: utf-8 -*-


import os
import configparser


class ConfigIniParser:

    def __init__(self, root_dir, ini_file_path):
        self.config = configparser.ConfigParser()
        self.file_path = os.path.join(root_dir, ini_file_path)
        self.config.read(self.file_path)

    def config_section_dict(self, section):
        section_dict = {}
        section_keys = self.config.options(section)

        for key in section_keys:
            section_dict[key] = self.config.get(section, key)

            # section_dict[key] = None

        return section_dict

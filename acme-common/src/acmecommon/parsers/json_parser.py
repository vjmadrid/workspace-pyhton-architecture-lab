# -*- coding: utf-8 -*-


import os
import json


class JsonParser:

    def __init__(self, root_dir, json_path):
        self.json_path = os.path.join(root_dir, json_path)

    def read_from_json(self):
        with open(self.json_path, 'r', encoding="utf-8") as json_file:
            json_reader = json.load(json_file)
        return json_reader

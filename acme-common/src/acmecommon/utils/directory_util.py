# -*- coding: utf-8 -*-


import os
import shutil
import glob


class DirectoryUtil:
    def create_directory(self, directory_path):
        if (not os.path.exists(directory_path)) and (os.path.isdir(directory_path)):
            os.makedirs(directory_path)

    def change_directory(self, directory_path):
        result = False

        if os.path.exists(directory_path):
            os.chdir(directory_path)
            result = True

        return result

    def is_empty_directory(self, directory_path):
        result = False

        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            if not os.listdir(directory_path):
                result = True
        return result

    def get_files_directory(self, directory_path):
        file_directory = os.listdir(directory_path)
        result_list = []

        for entry in file_directory:
            full_path = os.path.join(directory_path, entry)

            if os.path.isdir(full_path):
                result_list = result_list + self.get_files_directory(full_path)
            else:
                result_list.append(full_path)

        return result_list

    def get_files_directory_list(self, directory_path):
        result_list = []

        for (dir_path, dir_names, file_names) in os.walk(directory_path):
            result_list += [os.path.join(dir_path, file) for file in file_names]

        return result_list

    def get_empty_directories_list(self, directory_path):
        result_list = []

        for (dir_path, dir_names, file_names) in os.walk(directory_path):
            if len(dir_names) == 0 and len(file_names) == 0:
                result_list.append(dir_path)

        return result_list

    def move_all_files_in_dir(self, src_dir_path, dst_dir_path):
        result = False
        if os.path.isdir(src_dir_path) and os.path.isdir(dst_dir_path):
            for file_path in glob.glob(src_dir_path + "\\*"):
                shutil.move(file_path, dst_dir_path)

            result = True

        return result

    def move_file_to_dir(self, src_file_path, dst_dir_path):
        if not os.path.isdir(dst_dir_path):
            os.makedirs(dst_dir_path)

        shutil.move(src_file_path, dst_dir_path)

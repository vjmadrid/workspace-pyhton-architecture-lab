# -*- coding: utf-8 -*-


import os
import shutil
import glob


class DirectoryUtil:

    @staticmethod
    def create_directory(directory_path):
        result = False

        if (not os.path.exists(directory_path)) and (os.path.isdir(directory_path)):
            os.makedirs(directory_path)
            result = True

        return result

    @staticmethod
    def change_directory(directory_path):
        result = False

        if os.path.exists(directory_path):
            os.chdir(directory_path)
            result = True

        return result

    @staticmethod
    def is_empty_directory(directory_path):
        result = False

        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            if not os.listdir(directory_path):
                result = True
        return result

    @staticmethod
    def get_files_directory(directory_path):
        file_directory = os.listdir(directory_path)
        result_list = []

        for entry in file_directory:
            full_path = os.path.join(directory_path, entry)

            if os.path.isdir(full_path):
                result_list = result_list + DirectoryUtil.get_files_directory(full_path)
            else:
                result_list.append(full_path)

        return result_list

    @staticmethod
    def get_files_directory_list( directory_path):
        result_list = []

        for (dir_path, dir_names, file_names) in os.walk(directory_path):
            result_list += [os.path.join(dir_path, file) for file in file_names]

        return result_list

    @staticmethod
    def get_empty_directories_list(directory_path):
        result_list = []

        for (dir_path, dir_names, file_names) in os.walk(directory_path):
            if len(dir_names) == 0 and len(file_names) == 0:
                result_list.append(dir_path)

        return result_list

    @staticmethod
    def move_all_files_in_dir(src_dir_path, dst_dir_path):
        result = False
        if os.path.isdir(src_dir_path) and os.path.isdir(dst_dir_path):
            for file_path in glob.glob(src_dir_path + "\\*"):
                shutil.move(file_path, dst_dir_path)

            result = True

        return result

    @staticmethod
    def move_file_to_dir(src_file_path, dst_dir_path):
        if not os.path.isdir(dst_dir_path):
            os.makedirs(dst_dir_path)

        shutil.move(src_file_path, dst_dir_path)

    @staticmethod
    def remove_content_in_dir(directory_path):
        result = False

        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    result = True
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
                
        return result

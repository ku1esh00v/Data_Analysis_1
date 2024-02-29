#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os

def group_files_by_extension(folder):
    files = {}
    for filename in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, filename)):
            file_extension = filename.split('.')[-1]
            if file_extension in files:
                files[file_extension].append(filename)
            else:
                files[file_extension] = [filename]

    for extension, file_list in files.items():
        print(f"Расширение {extension}:")
        for file in file_list:
            print(f"- {file}")
        print()

if __name__ == '__main__':
    folder_path = "C:/Users/User/PycharmProjects/Data_Analysis_1"
    group_files_by_extension(folder_path)
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys

def cat_files(file_names):
    for file_name in file_names:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Не удалось открыть файл: {file_name}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ошибка: не указаны файлы для объединения.")
    else:
        files_to_cat = sys.argv[1:]
        cat_files(files_to_cat)

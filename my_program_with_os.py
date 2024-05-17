#Написал программу, которая создает директорию "Oleg Kuleshov" и в этой директории создает 10 текстовых файлов с названием "текст1.txt", "текст2.txt", ..., "текст10.txt",
#причём текст в файлах генерируется случайно

import os
import random
import string

# Создал директорию "Oleg Kuleshov"
directory_name = "Oleg Kuleshov"
os.makedirs(directory_name, exist_ok=True)
print(f"Создана директория: {directory_name}")

# Переход в созданную директорию
os.chdir(directory_name)

# Создание 10 текстовых файлов с различным содержимым
for i in range(1, 11):
    file_name = f"текст{i}.txt"
    with open(file_name, 'w') as file:
        random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=50))  # Сгенерируем случайный текст
        file.write(random_text)
    print(f"Создан файл: {file_name}")

print("Все файлы созданы в директории 'Oleg Kuleshov'")

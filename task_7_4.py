# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

from os import walk, stat
from os.path import abspath, join

info_dir = abspath(join(".", "task_7_4"))
file_size_dict = {100: [0, []], 1000: [0, []], 10000: [0, []], 100000: [0, []]}
for root, dirs, files in walk(abspath(info_dir)):
    for file in files:
        file_size = stat(join(root, file)).st_size
        for size in file_size_dict.keys():
            if file_size <= size:
                file_ext = file.split(".")[1]
                if file_ext not in file_size_dict[size][1]:
                    file_size_dict[size][1].append(file_ext)
                file_size_dict[size][0] += 1
                break
print(file_size_dict)

# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать
# в любом текстовом редакторе «руками» (не программно);
# Подумайте о возможных исключительных ситуациях при работе скрипта.
# Усложнение Библиотеки для парсинга yaml использовать нельзя.

from os import makedirs
from os.path import abspath, join, exists

def config_yaml_str(yaml_str, space=4):
    idx = yaml_str.rfind(" ")
    isfile = True if "." in yaml_str \
        else False
    if (idx + 1) % space != 0:
        raise ValueError
    elif idx == -1:
        return 1, yaml_str.strip(), isfile
    else:
        return ((idx + 1) // space) + 1, yaml_str[idx:].strip(), isfile

with open("config.yaml", encoding="UTF-8", mode="rt") as config_file:
    current_root = []
    current_level = 0
    for line in config_file:
        level, name, isfile = config_yaml_str(line)
        current_level = len(current_root)
        if level > current_level:
            current_root.append(name)
        elif level == current_level:
            current_root[-1] = name
        elif level < current_level:
            for i in range(current_level - level + 1):
                current_root.pop()
            current_root.append(name)
        dir_path = abspath(join(".", "task_7_2", *current_root))
        if not exists(dir_path):
            if isfile:
                with open(dir_path, encoding="UTF-8", mode="w"):
                    pass
            else:
                makedirs(dir_path)

# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

from os import mkdir
from os.path import join, abspath, exists

prefix = 'task_7_1'
main_dir = 'my_project'
dir_names = ['settings', 'mainapp', 'adminapp', 'authapp']
dir_path = abspath(join('.', prefix, main_dir))

if not exists(dir_path):
    mkdir(dir_path)

for dir_name in dir_names:
    dir_names_path = abspath(join('.', prefix, main_dir, dir_name))
    if not exists(dir_names_path):
        mkdir(dir_names_path)

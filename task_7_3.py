# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.

from os import walk
from os.path import abspath, join
from shutil import copytree

new_dir = abspath(join(".", "task_7_3", "templates"))
root_dir = abspath(join(".", "task_7_2"))
for root, dirs, files in walk(root_dir):
    if "templates" in dirs:
        copytree(join(root, "templates"), new_dir, dirs_exist_ok=True)


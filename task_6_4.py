# 4. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных
# и для вывода на экран записанных данных.
# Данные хранить в файле bakery.csv в кодировке utf-8.
# При записи передавать из командной строки значение суммы продаж.
# Новая запись дозаписывается в конец файла.
# Для чтения данных реализовать в командной строке следующую логику.
# Предполагаем, что первая запись имеет номер 1.
# 1) просто запуск скрипта — выводить все записи;
# 2) запуск скрипта с одним параметром-числом — выводить все записи с номера,
# равного этому числу, до конца;
# 3) запуск скрипта с двумя числами — выводить записи, начиная с номера,
# равного первому числу, по номер, равный второму числу, включительно;
#
# Примеры запуска скриптов:
#
# python add_sale.py 5978
# python add_sale.py 891
# python add_sale.py 7879
# python add_sale.py 1573
# python show_sales.py
# 5978
# 891
# 7879
# 1573
# python show_sales.py 3
# 7879
# 1573
# python show_sales.py 1 3
# 5978
# 891
# 7879
# Усложнение Подумать, как избежать чтения всего файла при реализации
# второго и третьего случаев.

from sys import argv

with open('bakery_sales.txt.txt', encoding='UTF-8', mode='rt') as bakery_sales:
    if len(argv) == 1:
        print('Показать все записи: ')
        for line in bakery_sales:
            print(line.strip())
    elif len(argv) == 2:
        record_begin = int(argv[1])
        print(f'Показать записи с {record_begin}:')
        for i, line in enumerate(bakery_sales):
            if i >= record_begin-1:
                print(line.strip())
    else:
        record_begin = int(argv[1])
        record_end = int(argv[2])

        print(f'Показать записи с {record_begin}:')
        for i, line in enumerate(bakery_sales):
            if record_begin-1 <= i <= record_end-1:
                print(line.strip())


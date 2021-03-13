# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
#
# Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание:
# - код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# - Вы не знате заранее насколько идентичен шаблон строк файла. Попробуйте оценить это.

with open("nginx_logs.txt", encoding="UTF-8", mode="rt") as logfile:
    line_count = 1
    while line_count:
        logline = logfile.readline()
        if logline == "":
            break

        logline_split = logline.split()
        remote_addr = logline_split[0]
        request_type = logline_split[5].strip('"')
        requested_resource = logline_split[6]

        tulip = (remote_addr, request_type, requested_resource)
        print(tulip)

        line_count = line_count + 1



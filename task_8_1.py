# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Уточнение
# Текст до собаки (Local-part): латинские буквы, цифры и символы: ' . _ + -
#
# Текст после собаки (Domain part): латинские буквы, цифры и символы . -
#
# В Domain part обязательно должна быть хотя бы одна точка.
#
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

# импортируем модуль регулярных выражений
import re

# Список email адресов
# email_addresses = "delluiza@yandex.ru; Konfetka13@mail.ru; vladkazh@hotmail.com; uglova93@mailru; icebery@qip.ru; " \
#                   "alpotehinj@gmail.com; cezarikc@mail.ru; maus19890503@hotmailcom; kimef11@yandex.ru".split("@")

email_addresses = "delluiza@yandex.ru; Konfetka13@mail.ru; vladkazh@hotmail.com; uglova93@mailru; icebery@qip.ru; " \
                  "alpotehinj@gmail.com; cezarikc@mail.ru; maus19890503@hotmailcom; kimef11@yandex.ru"

# Пишем регулярное выражение для определения валидности email
email_match = re.match(r'(\w+"a-zA-Z_]+?\.[a-zA-Z]{2,6})', email_addresses)
# re.compile(email_compile, email_addresses, flags=re.IGNORECASE)
# print(email_addresses)


def email_parse(username, domain):
    i = 1
    for el in email_addresses:
        # output = email_match.findall(".")
        if "." in el:
            return output.groupdict()
        else:
            return f'ValueError: wrong email: ', (el)
    i += 1


email_parse(email_addresses, email_match)

# >>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# >>> m.groupdict()
# {'first_name': 'Malcolm', 'last_name': 'Reynolds'}




# emails = """zuck26@facebook.com
# page33@google.com
# jeff42@amazon.com"""
#
#
# >>> pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
# >>> re.findall(pattern, emails, flags=re.IGNORECASE)
# [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]



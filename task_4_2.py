# Написать функцию currency_rates(), принимающую в качестве аргумента код
# валюты (USD, EUR, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере,
# посмотреть содержимое ответа. Можно ли, используя только методы класса str,
# решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами
# использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре
# был передан аргумент? В качестве примера выведите курсы доллара и евро.

from requests import get, utils

url_get = "http://www.cbr.ru/scripts/XML_daily.asp"


def currency_rates(url, cur_name):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    cur_name_value = content.find(cur_name.upper())

    result = []
    if cur_name_value != -1:
        value_beginning = content.find("<Value>", cur_name_value)
        value_beginning_length = 7
        value_ending = content.find("</Value>", value_beginning + value_beginning_length)
        currency = float(content[value_beginning + value_beginning_length: value_ending].replace(",", "."))
        result.append(currency)
    else:
        result.append(None)
    return result


print(f'RUR/USD: ', currency_rates(url_get, 'usd'))
print(f'RUR/EUR: ', currency_rates(url_get, "Eur"))
print(f'RUR/GBP: ', currency_rates(url_get, 'GbP'))
print(f'Нет такой валюты в файле: ', currency_rates(url_get, 'MNT'))


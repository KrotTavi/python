# 4. Создать список, содержащий цены на товары (10 – 20 товаров), например:
# [57.8, 46.51, 97, ...]

prices = [15.22, 48, 99.01, 5.1, 25, 88.7, 35.12, 150, 320.57, 42.09, 222.11, 698, 501.13]

# - Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

# used your solution as an example

for price_printed in prices:
    price_printed_roubles = int(price_printed)
    price_printed_cents = round((price_printed - price_printed_roubles)*100)
    if 0 < price_printed_cents < 10:
        price_printed_cents = f"0{price_printed_cents}"
    elif price_printed_cents == 0:
        price_printed_cents = f"00"
    else:
        price_printed_cents = f"{price_printed_cents}"
    print(f"{price_printed_roubles} руб {price_printed_cents} коп", end=", ")

# - Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).

print(id(prices))
prices.sort()
print(id(prices))
print(prices)

# - Создать новый список, содержащий те же цены, но отсортированные по убыванию.

prices_reversed = prices[::-1]
print(id(prices))
print(id(prices_reversed))
print(prices_reversed)

# - Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


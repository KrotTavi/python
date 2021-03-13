from sys import argv

if len(argv) < 2:
    print('Нет данных о сумме продаж')
    exit(1)

with open('bakery.csv', encoding='UTF-8', mode='at') as bakery:
    bakery.write(f'{argv[1]:>5s}\n')

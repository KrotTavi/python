# 2. Для кубов нечётных чисел от 1 до 1000.
# Вычислить сумму и вывести на экран те числа,
# сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# Вывод на экран формить в виде: число: xxxxxxx sum: xxx

# Алгоритм:

# 1) Сначала разберитесь просто с выделением разрядов числа(цифр).
# Это делается за счет целочисленного деления на 10
# и взятие остатка от этого деления.
# Не используйте операции со строками. Поэкспериментируйте.
# 2) Сделайте этот алгоритм для произвольного числа -
# вам понадобится цикл.
# Отладьте этот алгоритм и подсчитайте сумму цифр.
# 3) Сделайте алгоритм предыдущего пунка частью цикла
# по числам от 1 до 1000.

sum_total = 0

for number in range(1, 1001): # for 1 to 1000
    if number % 2 == 1: # select only odd numbers
        number_cube = number ** 3 # cube the number

        digit_in_number_1 = number_cube // 100000000
        remainder_1 = number_cube % 100000000
        digit_in_number_2 = remainder_1 // 10000000
        remainder_2 = remainder_1 % 10000000
        digit_in_number_3 = remainder_2 // 1000000
        remainder_3 = remainder_2 % 1000000
        digit_in_number_4 = remainder_3 // 100000
        remainder_4 = remainder_3 % 100000
        digit_in_number_5 = remainder_4 // 10000
        remainder_5 = remainder_4 % 10000
        digit_in_number_6 = remainder_5 // 1000
        remainder_6 = remainder_5 % 1000
        digit_in_number_7 = remainder_6 // 100
        remainder_7 = remainder_6 % 100
        digit_in_number_8 = remainder_7 // 10
        remainder_8 = remainder_7 % 10
        digit_in_number_9 = remainder_8 // 1
        remainder_9 = remainder_8 % 1

        sum_of_digits = digit_in_number_1 + digit_in_number_2 + digit_in_number_3 + digit_in_number_4 + digit_in_number_5 + digit_in_number_6 + digit_in_number_7 + digit_in_number_8 + digit_in_number_9

        if sum_of_digits % 7 == 0:
            sum_total = number + sum_total
            print("число:", number, "sum:", sum_total)

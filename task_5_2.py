# 2. Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield. Полностью истощить генератор.
# Например:
# gen1 = iterator_with_yield(11)
# next(gen1)
# 1
# next(gen1)
# 3
# next(gen1)
# 5
# next(gen1)
# 7
# next(gen1)
# 9
# next(gen1)
# 11
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration


def my_iteration_1(stop):
    result = 0
    for result in range(1, stop+1, 2):
        yield result
        result += 1


gen1 = my_iteration_1(21)
while True:
    print(next(gen1))

# Усложнение(*):
# С ключевым словом yield - как в задании 1: генератор нечётных чисел
# от 1 до n (включительно), для чисел, квадрат которых меньше 200.


def my_iteration_2(stop):
    result = 0
    for result in range(1, stop+1, 2):
        if (result ** 2) < 200:
            yield result
        result += 1


gen2 = my_iteration_2(21)
while True:
    print(next(gen2))

# Усложнение(**):
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму
# этого и предыдущих чисел. Например:
#
# gen1 = iterator_with_yield(14)
# next(gen1)
# (1, 1)
# next(gen1)
# (3, 4)
# next(gen1)
# (5, 9)
# next(gen1)
# (7, 16)
# next(gen1)
# (9, 25)
# next(gen1)
# (11, 36)
# next(gen1)
# (13, 49)
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration


def my_iteration_3(stop):
    result = 0
    sum_total = 0
    for result in range(1, stop+1, 2):
        if (result ** 2) < 200:
            sum_total = sum_total + result
            pair = (result, sum_total)
            yield pair
        result += 1


gen3 = my_iteration_3(21)
while True:
    print(next(gen3))

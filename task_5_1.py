# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# без использования ключевого слова yield, полностью истощить генератор.
# Например:
# gen1 = iterator_without_yield(11)
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

gen1 = (el for el in range(1, 21+1, 2))
while True:
    print(next(gen1))

# Усложнение(*):
# Без использования ключевого слова yield: генератор нечётных чисел
# от 1 до n (включительно), для чисел, квадрат которых меньше 200.

gen2 = (el for el in range(1, 21+1, 2) if el ** 2 < 200)
while True:
    print(next(gen2))

# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Усложнение: * Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

from random import choice

def get_jokes(joke_number, lst1, lst2, lst3, unique=False):

    """
    :param joke_number:
    :param lst1:
    :param lst2:
    :param lst3:
    :param unique:
    :return:
    """

    """
    random create list of joke string from three list of string
    :param joke_number: number of jokes
    :param lst1: first words for joke
    :param lst2: second words for joke
    :param unique: use only unique words in jokes
    :return: list of joke(str)
    """

    if unique:
        min_length = min(joke_number, len(lst1), len(lst2), len(lst3))
    else:
        min_length = joke_number

    joke_list = []
    for i in range(min_length):
        joke_list.append(f"{choice(lst1)} {choice(lst2)} {choice(lst3)}")
    return joke_list

nouns = ["магазин", "велосипед", "кресло", "ванна", "школа"]
adverbs = ["сейчас", "вчера", "завтра", "послезавтра", "днём"]
adjectives = ["умный", "красивый", "ласковый", "угрюмый", "добрый"]

print(get_jokes(6, nouns, adverbs, adjectives))
print(get_jokes(joke_number=5, lst1=nouns, lst2=adverbs, lst3=adjectives))

print(get_jokes(6, nouns, adverbs, adjectives, True))

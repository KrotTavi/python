# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имен, а значения —
# списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Замечание: Заранее неизвестно сколько фамилий передадут в функцию thesaurus
# Подумайте: полезен ли будет вам оператор распаковки?
# Сможете ли вы вернуть отсортированный по ключам словарь?

def thesaurus(*args):
    res_dict = dict()
    for name in args:
        first_letter = name[0]
        if first_letter in res_dict.keys():
            res_dict[first_letter].append(name)
        else:
            res_dict[first_letter] = [name]

    sort_dict = dict()
    for key in sorted(res_dict.keys()):
        sort_dict[key] = res_dict[key]
    return sort_dict

print("Имена:")
print(thesaurus("Иван", "Мария", "Петр", "Илья", "Кирилл", "Андрей"))
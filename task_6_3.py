# 3. Есть два файла: в одном хранятся ФИО пользователей сайта,  а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО
# значение в словаре - None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# Примечание: При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи

with open('users.csv', encoding='UTF-8', mode='rt') as users_list, \
        open('hobbies.csv', encoding='UTF-8', mode='rt') as hobbies_list:
    users = users_list.readlines()  # unpack users_list
    hobbies = hobbies_list.readlines()  # unpack hobbies_list

    user_count = 0
    user_list =[]
    for user in users:
        user = users[user_count].strip('\n')
        user_list.append(user)
        user_count += 1

    hobby_count = 0
    hobby_list = []
    for hobby in hobbies:
        hobby = hobbies[hobby_count].strip('\n')
        hobby_list.append(hobby)
        hobby_count += 1

    # looks like this part isn't working
    if len(hobby_list) > len(user_list):
        user_list, None
    else:
        user_list, hobby_list

    users_and_hobbies = dict(zip(user_list, hobby_list))  # create a dictionary
    print(users_and_hobbies)  # print out user and hobby

with open('task_6_3_result.txt', encoding='UTF-8', mode='wt') as users_and_hobbies_result:
    users_and_hobbies_result.write(str(users_and_hobbies))


# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
# Формат вывода результата:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите продолжительность времени в секундах: '))

duration_seconds = duration % 60
duration_minutes = duration // 60 % 60
duration_hours = duration // 3600 % 24
duration_days = duration // 86400 % 30

if duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    print(duration_minutes, 'мин', duration_seconds, 'сек')
elif 3600 <= duration < 86400:
    print(duration_hours, 'час', duration_minutes, 'мин', duration_seconds, 'сек')
else:
    print(duration_days, 'дн', duration_hours, 'час', duration_minutes, 'мин', duration_seconds, 'сек')

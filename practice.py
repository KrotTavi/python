num = 457
is_three_digits = 0 < num // 100 <= 9
print(is_three_digits)

tens = num % 100 // 10
print(tens)

print(tens == 5)
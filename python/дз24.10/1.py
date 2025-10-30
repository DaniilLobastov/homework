import random

lst = [random.randint(-100, 100) for i in range(10)]

product = 1
first_positive = -1
last_positive = -1


for i, num in enumerate(lst):
    if num > 0:
        first_positive = i
        break

for i in range(len(lst) - 1, -1, -1):
    if lst[i] > 0:
        last_positive = i
        break


total_sum = 0
if first_positive != -1 and last_positive != -1 and first_positive < last_positive:
    total_sum = sum(lst[first_positive + 1:last_positive])


negative_sum = sum(i for i in lst if i < 0)
even_sum = sum(i for i in lst if i % 2 == 0)
odd_sum = sum(i for i in lst if i % 2 != 0)
min_max = min(lst) * max(lst)

for i in range(len(lst)):
    if i % 3 == 0:
        product *= lst[i]

print(f'''Список: {lst}
Сумма отрицательных чисел: {negative_sum}
Сумма четных чисел: {even_sum}
Сумма нечетных чисел: {odd_sum}
Произведение минимального и максимального числа: {min_max}
Произведение чисел с индексами кратным 3: {product}
Сумма между первым и последним положительными: {total_sum}''')
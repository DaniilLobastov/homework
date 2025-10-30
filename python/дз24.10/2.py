import random

lst = [random.randint(-100, 100) for i in range(10)]
odd = []
even = []
negative = []
positive = []



for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)


print(f'Список: {lst}\nЧетные: {even}\nНечетные: {odd}\nПоложительные: {positive}\nОтрицательные: {negative}')
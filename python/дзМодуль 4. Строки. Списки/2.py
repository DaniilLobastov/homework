import random

a = [random.randint(-100, 100) for i in range(10)]


print(f'Список:{a} \nМаксимальный элемент: {max(a)}\nМинимальный элемент: {min(a)}\nКоличество положительных чисел: {sum(i > 0 for i in a)}\nКоличество отрицательных чисел: {sum(i < 0 for i in a)}\nКоличетсво нулей: {sum(i==0 for i in a)}')





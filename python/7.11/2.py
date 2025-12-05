def odd_numbers(a, b):
    for i in range(a + 1, b):
        if i % 2 != 0:
            print(i)


a = int(input('Введите число: '))
b = int(input('Введите число: '))

odd_numbers(a, b)
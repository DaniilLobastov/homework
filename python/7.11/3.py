def line(length, direction, symbol):
    if direction == 'горизонтальная':
        print(symbol * length)
    elif direction == 'вертикальная':
        for _ in range(length):
            print(symbol)


line(5, 'горизонтальная', '*')
line(3, 'вертикальная', '!')
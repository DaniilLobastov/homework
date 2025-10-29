while True:

    expression = input("Введите выражение(например 23+25)\nВвод: ")

    expression = expression.replace(" ", "")


    if '+' in expression:
        a, b = expression.split('+')
        print(int(a) + int(b))
    elif '-' in expression:
        a, b = expression.split('-')
        print(int(a) - int(b))
    elif '*' in expression:
        a, b = expression.split('*')
        print(int(a) * int(b))
    elif '/' in expression:
        a, b = expression.split('/')
        print(int(a) / int(b))
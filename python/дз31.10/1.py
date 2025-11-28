import random

def index(lst):
    return min(enumerate(lst), key=lambda x: x[1])[0]

lst = [random.randint(0, 100) for i in range(10)]
print(index(lst))
print(lst)


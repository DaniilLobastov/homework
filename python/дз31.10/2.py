def numbers(s):
    return sorted(s.split(), key=int)
print(numbers("4 2 8 1"))
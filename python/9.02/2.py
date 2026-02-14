def number(n, max_num=None):
    if max_num is None:
        max_num = n
    if n == 0:
        return [[]]
    result = []
    for i in range(1, min(max_num, n) + 1):
        for partition in number(n - i, i):
            result.append([i] + partition)
    return result

n = 4
print(f"Все разбиения числа {n}:")
partitions = number(n)
for p in partitions:
    print(p)
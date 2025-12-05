def lucky(number):
    num_str = str(number)
    if len(num_str) != 6:
        return False
    first = sum(map(int, num_str[:3]))
    second = sum(map(int, num_str[3:]))
    return first == second

print(lucky(123420))
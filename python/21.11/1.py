def recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] if lst[0] > recursive(lst[1:]) else recursive(lst[1:])

numbers = [3, 7, 2, 9, 5]
print(recursive(numbers)) 

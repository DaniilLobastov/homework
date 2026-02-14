def max(arr):
    if len(arr) == 1:
        return arr[0]
    max_of_rest = max(arr[1:])
    return arr[0] if arr[0] > max_of_rest else max_of_rest

numbers = [3, 7, 2, 9, 1, 5]
print(f"наибольший элемент в списке {numbers}: {max(numbers)}")
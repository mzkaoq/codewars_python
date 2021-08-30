def binary_array_to_number(arr):
    number = ''
    for i in arr:
        number += str(i)
    return int(number, 2)

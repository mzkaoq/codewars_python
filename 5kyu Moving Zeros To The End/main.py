def move_zeros(array):
    count = 0
    for i in array:
        if i == 0:
            count += 1
    array[:] = (x for x in array if x != 0)
    array += count * [0]
    return array

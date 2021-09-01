def sum_pairs(ints, s):
    array = set()
    for i in range(len(ints)):
        temp = s - ints[i]
        if temp in array:
            return [temp,ints[i]]
        array.add(ints[i])
    return None


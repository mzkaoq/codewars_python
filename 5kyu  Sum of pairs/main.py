def sum_pairs(ints, s):
    array = dict()
    min = 10000
    for i in range(len(ints)):
        for j in range(i,len(ints)):
            if ints[i] + ints[j] == s:
                if i != j:
                    array[j] = {"ints[i]": ints[i], "ints[j]": ints[j]}
                    if j < min:
                        min = j
    if min != 10000:
        return [array[min]["ints[i]"], array[min]["ints[j]"]]
    else:
        return None



def dbl_linear(n):
    our_list = [1]
    i = 0
    len_list = 1
    while len_list < n * 35:
        our_list.append(our_list[i] * 2 + 1)
        our_list.append(our_list[i] * 3 + 1)
        i += 1
        len_list += 4
    our_list.sort()
    our_list = list(dict.fromkeys(our_list))
    return our_list[n]

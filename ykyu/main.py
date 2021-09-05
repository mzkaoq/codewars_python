def int_diff(lst, n):
    returned_value = 0
    print(lst,n)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + n == lst[j] or lst[i] - n == lst[j]:
                returned_value += 1
    return returned_value

def generate_pairs(m, n):
    list = []
    for i in range(m, n + 1):
        for j in range(i, n + 1):
            z = (i, j)
            list.append(z)
    return list

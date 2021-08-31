def generate_pairs(m, n):
    list = []
    for i in range(m):
        for j in range(n):
            list.append(i,j)
    return list
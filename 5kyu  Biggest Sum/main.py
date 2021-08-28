def find_sum(m):
    M = len(m)
    for i in range(M):
        for j in range(M):
            if i == 0 and j == 0:
                pass
            elif i == 0:
                m[i][j] += m[i][j - 1]
            elif j == 0:
                m[i][j] += m[i - 1][j]
            else:
                if m[i][j] + m[i][j - 1] > m[i][j] + m[i - 1][j]:
                    m[i][j] += m[i][j - 1]
                else:
                    m[i][j] += m[i - 1][j]
    return m[M-1][M-1]


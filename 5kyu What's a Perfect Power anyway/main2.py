def isPP(n):
    for i in range(2, round(n ** 0.5) + 1):
        k = round(n ** (1 / i), 8)
        if k % 1 == 0:
            return [int(k), i]
    return None

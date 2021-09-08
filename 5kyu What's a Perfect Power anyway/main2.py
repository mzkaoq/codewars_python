def isPP(n):
    for i in range(2,round(n**0.5)+1):
        k = n**(1/i)
        if k % 1 == 0:
            return [int(k),i]
    return None


for i in [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]:
    print(isPP(i))
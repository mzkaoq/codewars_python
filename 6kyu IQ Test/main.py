def iq_test(numbers):
    odd = 0
    even = 0
    numbers = numbers.split(" ")
    for i in range(3):
        if int(numbers[i]) % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        for i in numbers:
            if int(i) % 2 != 0:
                return (numbers.index(i) + 1)
    else:
        for i in numbers:
            if int(i) % 2 == 0:
                return (numbers.index(i) + 1)

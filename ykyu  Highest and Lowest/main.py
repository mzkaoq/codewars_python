def high_and_low(numbers):
    numbers = numbers.split(" ")
    min = int(numbers[0])
    max = int(numbers[0])
    for i in numbers:
        if int(i) > max:
            max = int(i)
        if int(i) < min:
            min = int(i)
    numbers = str(max) + " " + str(min)
    return numbers

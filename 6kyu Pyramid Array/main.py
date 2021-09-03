def pyramid(n):
    x = [1]
    array = []
    if n != 0:
        for i in range(n):
            array.append(x*(i+1))
    return array

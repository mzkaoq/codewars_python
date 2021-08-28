def narcissistic( value ):
    value2 = value
    a = list()
    while value >= 1:
        a.append(value % 10)
        value = int(value / 10)
    a.reverse()
    lenght = len(a)
    sum = 0
    for i in a:
        sum += i**lenght

    if sum == value2:
        return(True)
    else:
        return(False)
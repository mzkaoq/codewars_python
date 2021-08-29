def disemvowel(string_):
    new_string= ''
    for i in string_:
        if i in ['A','a','E','e','I','i','O','o','U','u']:
            pass
        else:
            new_string += i
    print(new_string)
    return new_string
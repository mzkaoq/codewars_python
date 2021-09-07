import string


def rot13(message):
    new_string = ''
    for i in message:
        if i in string.ascii_lowercase or string.ascii_uppercase:
            if ord(i) >= 97:
                k = ((ord(i) + 13 - 97) % 26 + 97)
            else:
                k = ((ord(i) + 13 - 65) % 26 + 65)
            new_string += chr(k)
        else:
            new_string += i
    return new_string


print(rot13("Test"))

import string

def rot13(message):
    new_string = ''
    for i in message:
        if i in string.ascii_lowercase or string.ascii_uppercase:
            #print(chr((ord(i)+13)%123))
            print(ord(i))
            k = (ord(i)+13)%123
            print(k)
            if k < 65:
                k+= 65
            print(k)
            new_string += chr(k)
        print('---')
    return new_string

print(rot13("Test"))
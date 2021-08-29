import string


def is_pangram(s):
    new_alphabet = ""
    for i in string.ascii_lowercase:
        new_alphabet += (i + ',')
    new_alphabet = new_alphabet.split(",")
    s = s.lower()
    for i in s:
        if i in new_alphabet:
            new_alphabet.remove(i)
    if new_alphabet == ['']:
        return True
    else:
        return False

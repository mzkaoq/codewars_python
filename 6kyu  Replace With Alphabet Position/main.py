import string


def alphabet_position(text):
    text = text.lower()
    alphabet = []
    returned_string = ''
    for i in string.ascii_lowercase:
        alphabet.append(i)
    for i in text:
        if i in alphabet:
            returned_string += str(alphabet.index(i) + 1) + ' '
    return returned_string[:len(returned_string) - 1]

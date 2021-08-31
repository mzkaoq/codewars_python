def pig_it(text):
    text = text.split(" ")
    print(text)
    end_word = ''
    for i in text:
        if i in ('!', '?', '/'):
            end_word += i + ' '
        else:
            end_word += i[1:len(i)] + i[0] + 'ay '
    return end_word[0:-1]



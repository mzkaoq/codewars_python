def last_survivor(letters, coords):
    new_letters = ''
    for i in letters:
        new_letters += i + ","
    letters = new_letters.split(",")
    letters = letters[:-1]
    for i in coords:
        letters.pop(i)
    return letters[0]


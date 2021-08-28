def solution(s):
    if s == "":
        return []
    else:
        if len(s) % 2 == 1:
            s += "_"
        splits = int(len(s) / 2)
        s = list(s)
        counter = 1
        word = ""
        for i in s:
            word += i
            if counter % 3 == 2:
                word += ","
                counter = 0
            counter += 1
        word = word[:-1]
        s = word.split(",",splits)
        return s
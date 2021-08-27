def open_or_senior(data):
    returned_list = list()
    for i in data:
        print(i[0])
        if i[0] >= 55 and i[1] > 7:
            returned_list.append("Senior")
        else:
            returned_list.append("Open")
    return returned_list

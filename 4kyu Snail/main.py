def snail(snail_map):
    new_list = []
    lenght = len(snail_map)
    incr = lenght ** 2
    y_left = 0
    x_up = 0
    y_right = 0
    x_down = 0
    while incr != 0:
        for i in range(y_left, lenght - y_right - 1):
            new_list.append(snail_map[x_up][i])
            incr -= 1
        y_left += 1
        for i in range(x_up, lenght - x_down - 1):
            new_list.append(snail_map[i][lenght - y_right - 1])
            incr -= 1
        x_up += 1
        for i in range(lenght - y_right , y_left - 1, -1):
            new_list.append(snail_map[lenght - x_down - 1][i])
            incr -= 1
        y_right += 1
        for i in range(lenght - x_down - 1, x_up - 1 , -1):
            new_list.append(snail_map[i][y_left - 1])
            incr -= 1
        x_down += 1
        print(new_list)
    return new_list


array = [[1, 2, 3, 4,88],
         [5, 6, 7, 8,87],
         [9, 10, 11, 12,86],
         [13, 14, 15, 16,85],
         [55,56,67,68,69,70]]
print(snail(array))

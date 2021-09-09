def tower_builder(n_floors):
    y = " "
    x = "*"
    tower = []
    for i in range(1, n_floors + 1):
        spaces = (n_floors - i)
        print(spaces)
        floor = y * spaces + (i - 1) * x + x + (i - 1) * x + y * spaces
        tower.append(floor)
    return tower


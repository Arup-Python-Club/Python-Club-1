def print_pyramid(rows):
    for i in range(rows):
        indent = ' ' * (rows - 1 - i)
        print(indent + '*' * (2 * i + 1))

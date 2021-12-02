def is_valid_index(row, col):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False

text = input()
size = int(input())

matrix = []

commands = {"up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
}

current_x, current_y = None, None
for r in range(size):
    matrix.append(list(input()))
    for c in range(size):
        if matrix[r][c] == "P":
            current_x, current_y = r, c

number_of_commands = int(input())


for i in range(number_of_commands):
    command = input()
    next_x = current_x + commands[command][0]
    next_y = current_y + commands[command][1]
    if is_valid_index(next_x, next_y):
        if not matrix[next_x][next_y] == "-":
            text += matrix[next_x][next_y]
        matrix[next_x][next_y] = "P"
        matrix[current_x][current_y] = "-"
        current_x, current_y = next_x, next_y
    else:
        if text:
            text = text[:-1]

print(text)
for r in range(size):
    print(''.join(matrix[r]))

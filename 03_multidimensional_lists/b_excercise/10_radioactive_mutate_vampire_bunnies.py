def is_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

rows, cols = [int(x) for x in input().split()]
lair = []
for row in range(rows):
    lair.append([x for x in input()])
actions = list(input())

current_row, current_col = 0, 0
for row in range(rows):
    for col in range(cols):
        if lair[row][col] == "P":
            current_row = row
            current_col = col

is_dead = False
is_finished = False
for act in actions:
    if act == "L":
        next_row, next_col = current_row, current_col - 1
    elif act == "R":
        next_row, next_col = current_row, current_col + 1
    elif act == "U":
        next_row, next_col = current_row - 1, current_col
    elif act == "D":
        next_row, next_col = current_row + 1, current_col
    if not 0 <= next_row < rows or not 0 <= next_col < cols:
        lair[current_row][current_col] = "."
        is_dead = False
        is_finished = True
    elif is_valid_index(next_row, next_col):
        lair[current_row][current_col] = "."
        if not lair[next_row][next_col] == "B":
            lair[next_row][next_col] = "P"
        else:
            is_dead = True
        current_row, current_col = next_row, next_col
    bunnies_coordinates = []
    for i in range(rows):
        for j in range(cols):
            if lair[i][j] == "B":
                bunnies_coordinates.append([i,j])
    for idx in range(len(bunnies_coordinates)):
        i, j = bunnies_coordinates[idx]
        if is_valid_index(i + 1, j):
            if lair[i + 1][j] == "P":
                is_dead = True
            lair[i + 1][j] = "B"
        if is_valid_index(i, j + 1):
            if lair[i][j + 1] == "P":
                is_dead = True
            lair[i][j + 1] = "B"
        if is_valid_index(i, j - 1):
            if lair[i][j - 1] == "P":
                is_dead = True
            lair[i][j - 1] = "B"
        if is_valid_index(i - 1, j):
            if lair[i - 1][j] == "P":
                is_dead = True
            lair[i - 1][j] = "B"
    if is_dead:
        break
    if is_finished:
        break
for i in range(rows):
    print(''.join(lair[i]))
if not is_dead:
    print(f"won: {current_row} {current_col}")
else:
    print(f"dead: {current_row} {current_col}")

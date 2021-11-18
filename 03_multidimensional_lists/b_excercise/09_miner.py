def is_valid_index(row, col, command):
    if command == "up":
        if 0 <= row - 1 < rows:
            current_position[0] = row - 1
            current_position[1] = col
            return True
    elif command == "right":
        if 0 <= col + 1 < rows:
            current_position[0] = row
            current_position[1] = col + 1
            return True
    elif command == "left":
        if 0 <= col - 1 < rows:
            current_position[0] = row
            current_position[1] = col - 1
            return True
    elif command == "down":
        if 0 <= row + 1 < rows:
            current_position[0] = row + 1
            current_position[1] = col
            return True
    return False


rows = int(input())
commands = input().split()
field = []
for row in range(rows):
    field.append([el for el in input().split()])

current_position = []
coals_counter = 0
for i in range(rows):
    for j in range(rows):
        if field[i][j] == "s":
            current_position.append(i)
            current_position.append(j)
        elif field[i][j] == "c":
            coals_counter += 1


is_finished = False

for idx in range(len(commands)):
    command = commands[idx]
    i = current_position[0]
    j = current_position[1]
    if is_valid_index(i,j, command):
        i = current_position[0]
        j = current_position[1]
        if field[i][j] == "e":
            print(f"Game over! ({i}, {j})")
            is_finished = True
            break
        elif field[i][j] == "c":
            coals_counter -= 1
            field[i][j] = "*"
            if coals_counter == 0:
                print(f"You collected all coal! ({i}, {j})")
                is_finished = True
                break
if not is_finished:
    print(f"{coals_counter} pieces of coal left. ({current_position[0]}, {current_position[1]})")

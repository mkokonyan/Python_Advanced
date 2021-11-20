def is_valid_index(row, col):
    if 0 <= row < 5 and 0 <= col < 5:
        return True
    return False


field = []
for i in range(5):
    field.append(input().split())
total_targets = 0
current_i, current_j = 0, 0
for i in range(5):
    for j in range(5):
        if field[i][j] == "x":
            total_targets += 1
        if field[i][j] == "A":
            current_i, current_j = i, j
hit_targets_counter = 0
hit_targets_indexes = []
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        steps = int(command[2])
        for step in range(steps):
            if direction == "right":
                next_i, next_j = current_i, current_j + 1
            elif direction == "left":
                next_i, next_j = current_i, current_j - 1
            elif direction == "up":
                next_i, next_j = current_i - 1, current_j
            elif direction == "down":
                next_i, next_j = current_i + 1, current_j
            if is_valid_index(next_i, next_j):
                if field[next_i][next_j] == ".":
                    field[current_i][current_j] = "."
                    field[next_i][next_j] = "A"
                    current_i, current_j = next_i, next_j
            else:
                break
    elif action == "shoot":
        if direction == "right":
            for col in range(current_j + 1, 5):
                if field[current_i][col] == "x":
                    hit_targets_counter += 1
                    hit_targets_indexes.append([current_i, col])
                    field[current_i][col] = "."
                    break
        elif direction == "left":
            for col in range(current_j - 1, -1, -1):
                if field[current_i][col] == "x":
                    hit_targets_counter += 1
                    hit_targets_indexes.append([current_i, col])
                    field[current_i][col] = "."
                    break
        elif direction == "up":
            for row in range(current_i - 1, -1, -1):
                if field[row][current_j] == "x":
                    hit_targets_counter += 1
                    hit_targets_indexes.append([row, current_j])
                    field[row][current_j] = "."
                    break
        elif direction == "down":
            for row in range(current_i + 1, 5):
                if field[row][current_j] == "x":
                    hit_targets_counter += 1
                    hit_targets_indexes.append([row, current_j])
                    field[row][current_j] = "."
                    break
    if total_targets == hit_targets_counter:
        print(f"Training completed! All {total_targets} targets hit.")
        break
diff = total_targets - hit_targets_counter
if diff > 0:
    print(f"Training not completed! {diff} targets left.")
if len(hit_targets_indexes) > 0:
    for idx in range(len(hit_targets_indexes)):
        print(hit_targets_indexes[idx])

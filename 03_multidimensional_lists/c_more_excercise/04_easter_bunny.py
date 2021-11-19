def is_valid_index(index):
    if 0 <= index < n:
        return True
    return False

n = int(input())
field = []
for _ in range(n):
    field.append(input().split())

for i in range(n):
    for j in range(n):
        if field[i][j] == "B":
            starting_point = (i, j)
            break


directions = ["up", "down", "left", "right"]
max_sum = 0
direction_points = []
direction = ""

for idx in range(len(directions)):
    is_finished = False
    current_sum = 0
    current_direction_points = []
    row, col = starting_point

    if directions[idx] == "up":
        for i in range(row, -1, -1):
            if is_valid_index(i-1):
                if field[i-1][col] == "X":
                    is_finished = True
                    break
                else:
                    current_sum += int(field[i - 1][col])
                    current_direction_points.append([i - 1, col])
            else:
                is_finished = True
                break

    elif directions[idx] == "down":
        for i in range(row, n):
            if is_valid_index(i+1):
                if field[i + 1][col] == "X":
                    is_finished = True
                    break
                else:
                    current_sum += int(field[i + 1][col])
                    current_direction_points.append([i + 1, col])
            else:
                is_finished = True
                break
    elif directions[idx] == "left":
        for i in range(col, -1, -1):
            if is_valid_index(i - 1):
                if field[row][i-1] == "X":
                    is_finished = True
                    break
                else:
                    current_sum += int(field[row][i-1])
                    current_direction_points.append([row, i-1])
            else:
                is_finished = True
                break
    elif directions[idx] == "right":
        for i in range(col, n):
            if is_valid_index(i + 1):
                if field[row][i + 1] == "X":
                    is_finished = True
                    break
                else:
                    current_sum += int(field[row][i + 1])
                    current_direction_points.append([row, i + 1])
            else:
                is_finished = True
                break

    if current_sum >= max_sum:
        max_sum = current_sum
        direction_points = current_direction_points
        direction = directions[idx]


print(direction)
for dir in direction_points:
    print(dir)
print(max_sum)

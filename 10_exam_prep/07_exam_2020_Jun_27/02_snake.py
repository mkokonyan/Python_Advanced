def is_valid_index(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


n = int(input())
territory = []
burrows_coords = []
for i in range(n):
    territory.append(list(input()))
    for j in range(n):
        if territory[i][j] == "S":
            current_x, current_y = i, j
        elif territory[i][j] == "B":
            burrows_coords.append((i, j))

commands = {"left": (0, -1),
            "right": (0, 1),
            "up": (-1, 0),
            "down": (1, 0)
            }
food_quantity = 0

while True:
    current_command = input()
    next_x = current_x + commands[current_command][0]
    next_y = current_y + commands[current_command][1]
    territory[current_x][current_y] = "."
    if is_valid_index(next_x, next_y):
        if territory[next_x][next_y] == "*":
            territory[next_x][next_y] = "S"
            food_quantity += 1
        elif territory[next_x][next_y] == "B":
            if (next_x, next_y) == burrows_coords[0]:
                burrows_coords.pop(0)
            else:
                burrows_coords.pop(1)
            territory[next_x][next_y] = "."
            territory[burrows_coords[0][0]][burrows_coords[0][1]] = "S"
            next_x, next_y = burrows_coords[0][0], burrows_coords[0][1]
    else:
        print("Game over!")
        break
    if food_quantity == 10:
        break
    current_x, current_y = next_x, next_y

if food_quantity == 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")
for i in range(n):
    print(f"{''.join(territory[i])}")

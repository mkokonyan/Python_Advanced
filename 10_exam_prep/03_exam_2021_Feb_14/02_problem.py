from math import floor


def is_valid_index(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False


n = int(input())

board = []
for row in range(n):
    board.append([int(x) if x.isdigit() else x for x in input().split()])

for row in range(n):
    for col in range(n):
        if board[row][col] == "P":
            start_x, start_y = row, col

mapper = {"up": (-1, 0),
          "down": (1, 0),
          "left": (0, -1),
          "right": (0, 1)
          }

collected_coins = 0
current_x, current_y = start_x, start_y
path = []
while True:
    command = input()
    current_x += mapper[command][0]
    current_y += mapper[command][1]
    if is_valid_index(current_x, current_y):
        if not board[current_x][current_y] == "X":
            path.append([current_x, current_y])
            collected_coins += board[current_x][current_y]
            if collected_coins >= 100:
                print(f"You won! You've collected {collected_coins} coins.")
                break
        else:
            collected_coins = floor(collected_coins / 2)
            print(f"Game over! You've collected {collected_coins} coins.")
            break
    else:
        collected_coins = floor(collected_coins / 2)
        print(f"Game over! You've collected {collected_coins} coins.")
        break
print("Your path:")
if path:
    for el in path:
        print(el)
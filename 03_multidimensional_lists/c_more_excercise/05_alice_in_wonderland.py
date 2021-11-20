def is_valid_index(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


n = int(input())
matrix = []
for _ in range(n):
    matrix.append([x for x in input().split()])

current_i, current_j = [[i, j] for i in range(n) for j in range(n) if matrix[i][j] == "A"][0]

collected_bags = 0
while collected_bags < 10:
    command = input()
    if command == "up":
        next_i, next_j = current_i - 1, current_j
    elif command == "down":
        next_i, next_j = current_i + 1, current_j
    elif command == "left":
        next_i, next_j = current_i, current_j - 1
    elif command == "right":
        next_i, next_j = current_i, current_j + 1
    matrix[current_i][current_j] = "*"
    if is_valid_index(next_i, next_j):
        if matrix[next_i][next_j].isdigit():
            collected_bags += int(matrix[next_i][next_j])
            matrix[next_i][next_j] = "*"
        elif matrix[next_i][next_j] == "R":
            matrix[next_i][next_j] = "*"
            break
        current_i, current_j = next_i, next_j
    else:
        break

if collected_bags >= 10:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")
for r in range(n):
    print(' '.join(list(map(str,matrix[r]))))
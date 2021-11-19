def is_valid_index(row, col):
    if 0 <= row < rows and 0 <= col < len(matrix[0]):
        return True
    return False

rows = int(input())
matrix = []
for row in range(rows):
    matrix.append([int(el) for el in input().split()])

command = input()
while not command == "END":
    action, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if is_valid_index(row, col):
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    command = input()

for i in range(rows):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
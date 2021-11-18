def is_valid(index1, index2):
    if 0 <= index1 < rows and 0 <= index2 < rows and matrix[index1][index2] > 0:
        return True
    return False


rows = int(input())
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])

data = [el for el in input().split()]
for i in range(len(data)):
    current_row, current_column = [int(x) for x in data[i].split(",")]
    exploded_cell = matrix[current_row][current_column]
    if exploded_cell > 0:
        if is_valid(current_row - 1, current_column):
            matrix[current_row - 1][current_column] -= exploded_cell
        if is_valid(current_row - 1, current_column - 1):
            matrix[current_row - 1][current_column - 1] -= exploded_cell
        if is_valid(current_row - 1, current_column + 1):
            matrix[current_row - 1][current_column + 1] -= exploded_cell

        if is_valid(current_row, current_column - 1):
            matrix[current_row][current_column - 1] -= exploded_cell
        if is_valid(current_row, current_column + 1):
            matrix[current_row][current_column + 1] -= exploded_cell

        if is_valid(current_row + 1, current_column):
            matrix[current_row + 1][current_column] -= exploded_cell
        if is_valid(current_row + 1, current_column - 1):
            matrix[current_row + 1][current_column - 1] -= exploded_cell
        if is_valid(current_row + 1, current_column + 1):
            matrix[current_row + 1][current_column + 1] -= exploded_cell

        matrix[current_row][current_column] = 0

alive_cells = 0
sum_active_cells = 0

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] > 0:
            alive_cells += 1
            sum_active_cells += matrix[i][j]
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_active_cells}")
for row in range(rows):
    print(" ".join(list(map(str, matrix[row]))))
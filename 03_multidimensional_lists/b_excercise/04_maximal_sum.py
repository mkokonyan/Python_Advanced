rows, cols = [int(el) for el in input().split()]
matrix = []
for row in range(rows):
    matrix.append([int(el) for el in input().split()])

max_sum = 0
max_sum_matrix = []
for i in range(0, rows-2):
    for j in range(0, cols-2):
        current_sum = sum(matrix[i][j:j+3]) + sum(matrix[i+1][j:j+3]) + sum(matrix[i+2][j:j+3])
        if current_sum >= max_sum:
            max_sum = current_sum
            max_sum_matrix.clear()
            for row in range(0, 3):
                max_sum_matrix.append(matrix[i+row][j:j+3])
print(f"Sum = {max_sum}")
for i in range(len(max_sum_matrix)):
    for j in range(len(max_sum_matrix)):
        print(max_sum_matrix[i][j], end=" ")
    print()

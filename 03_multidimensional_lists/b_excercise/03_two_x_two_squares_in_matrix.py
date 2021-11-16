rows, cols = [int(el) for el in input().split()]

matrix = []
two_x_two_counter = 0
for row in range(rows):
    matrix.append([el for el in input().split()])

for row in range(0, rows-1):
    for col in range(0, cols-1):
        char = matrix[row][col]
        if char == matrix[row][col+1] and char == matrix[row+1][col] and char == matrix[row+1][col+1]:
            two_x_two_counter += 1
print(two_x_two_counter)
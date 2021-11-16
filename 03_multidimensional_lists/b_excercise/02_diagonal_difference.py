rows = int(input())
matrix = []
for i in range(rows):
    matrix.append([int(el) for el in input().split()])

primary_diagonal = 0
for row in range(rows):
    primary_diagonal += matrix[row][row]

secondary_diagonal = 0
for row in range(rows):
    secondary_diagonal += matrix[row][rows-1-row]

print(abs(secondary_diagonal-primary_diagonal))
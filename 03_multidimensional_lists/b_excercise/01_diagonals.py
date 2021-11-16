rows = int(input())
matrix = []
for i in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

primary_diagonal = []
for row in range(rows):
    primary_diagonal.append(matrix[row][row])

secondary_diagonal = []
for row in range(rows):
    secondary_diagonal.append(matrix[row][rows-1-row])

print(f"Primary diagonal: {', '.join(list(map(str, primary_diagonal)))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(list(map(str, secondary_diagonal)))}. Sum: {sum(secondary_diagonal)}")
data = input().split("|")
matrix = []
for row in range(len(data)-1, -1, -1):
    matrix.append([int(el) for el in data[row].split()])

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
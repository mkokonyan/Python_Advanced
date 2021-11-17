rows, cols = [int(el) for el in input().split()]
matrix = []
text = input()
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(0)

for row in range(rows):
    if len(text) >= cols:
        if row % 2 == 0:
            for col in range(cols):
                matrix[row][col] = text[col]
            text = text[cols:] + text[:cols]
        else:
            for col in range(cols-1, -1, -1):
                matrix[row][col] = text[col+(len(text)-cols)]
            text = text[(len(text)-cols):] + text[:len(text)-cols]
        text = text[::-1]
    else:
        if row % 2 == 0:
            for col in range(len(text)):
                matrix[row][col] = text[col]
            for col in range(len(text), cols):
                matrix[row][col] = text[col - len(text)]
            text = text[cols-len(text):] + text[:cols-len(text)]
        else:
            for col in range(cols-1, cols - len(text), -1):
                matrix[row][col] = text[col+(len(text)-cols)]
            for col in range(cols - len(text), -1, -1):
                matrix[row][col] = text[col+(len(text)-cols)]
            text = text[(len(text)-cols):] + text[:len(text)-cols]
        text = text[::-1]

for i in range(rows):
    print("".join(matrix[i]))

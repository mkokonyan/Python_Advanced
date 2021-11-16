r, c = [int(el) for el in input().split()]
palindrome_matrix = []

for row in range(r):
    palindrome_matrix.append([])
    for col in range(c):
        first_last_char = chr(97+row)
        middle_char = chr(97+row+col)
        palindrome = first_last_char + middle_char + first_last_char
        palindrome_matrix[row].append(palindrome)

for i in range(len(palindrome_matrix)):
    for j in range(len(palindrome_matrix[i])):
        print(palindrome_matrix[i][j], end=" ")
    print()
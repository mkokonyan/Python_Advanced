rows, cols = [int(el) for el in input().split()]

matrix = []
for row in range(rows):
    matrix.append([int(el) if el.isdigit() else el for el in input().split()])

command = input()
while not command == "END":
    if not command.startswith("swap") or not len(command.split()) == 5:
        print("Invalid input!")
    else:
        command = command.split()
        first_chr_row = int(command[1])
        first_chr_col = int(command[2])
        second_chr_row = int(command[3])
        second_chr_col = int(command[4])
        if 0 <= first_chr_row < rows and 0 <= first_chr_col < cols \
                and 0 <= second_chr_row < rows and 0 <= second_chr_col < cols:
            matrix[first_chr_row][first_chr_col], matrix[second_chr_row][second_chr_col] = \
                matrix[second_chr_row][second_chr_col], matrix[first_chr_row][first_chr_col]
            for i in range(rows):
                for j in range(cols):
                    print(matrix[i][j], end=" ")
                print()
        else:
            print("Invalid input!")
    command = input()

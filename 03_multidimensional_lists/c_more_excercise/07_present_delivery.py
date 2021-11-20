number_of_presents = int(input())
n = int(input())

neighborhood = []
for i in range(n):
    neighborhood.append(input().split())

current_row, current_col = 0, 0
total_nice_kids = 0
for i in range(n):
    for j in range(n):
        if neighborhood[i][j] == "S":
            current_row, current_col = i, j
        elif neighborhood[i][j] == "V":
            total_nice_kids += 1

command = input()
while not command == "Christmas morning":
    if command == "up":
        next_row, next_col = current_row - 1, current_col
    elif command == "down":
        next_row, next_col = current_row + 1, current_col
    elif command == "left":
        next_row, next_col = current_row, current_col - 1
    elif command == "right":
        next_row, next_col = current_row, current_col + 1

    if neighborhood[next_row][next_col] == "V":
        neighborhood[current_row][current_col] = "-"
        current_row, current_col = next_row, next_col
        neighborhood[current_row][current_col] = "S"
        number_of_presents -= 1
        if number_of_presents == 0:
            break
    elif neighborhood[next_row][next_col] == "C":
        neighborhood[current_row][current_col] = "-"
        current_row, current_col = next_row, next_col
        neighborhood[current_row][current_col] = "S"
        if neighborhood[current_row - 1][current_col] == "V" or neighborhood[current_row - 1][current_col] == "X":
            neighborhood[current_row - 1][current_col] = "-"
            number_of_presents -= 1
            if number_of_presents <= 0:
                break
        if neighborhood[current_row + 1][current_col] == "V" or neighborhood[current_row + 1][current_col] == "X":
            neighborhood[current_row + 1][current_col] = "-"
            number_of_presents -= 1
            if number_of_presents <= 0:
                break
        if neighborhood[current_row][current_col - 1] == "V" or neighborhood[current_row][current_col - 1] == "X":
            neighborhood[current_row][current_col - 1] = "-"
            number_of_presents -= 1
            if number_of_presents <= 0:
                break
        if neighborhood[current_row][current_col + 1] == "V" or neighborhood[current_row][current_col + 1] == "X":
            neighborhood[current_row][current_col + 1] = "-"
            number_of_presents -= 1
            if number_of_presents <= 0:
                break
    else:
        neighborhood[current_row][current_col] = "-"
        neighborhood[next_row][next_col] = "S"
        current_row, current_col = next_row, next_col

    command = input()
not_happy_kids = 0
for i in range(n):
    for j in range(n):
        if neighborhood[i][j] == "V":
            not_happy_kids += 1

if number_of_presents <= 0 and not_happy_kids > 0:
    print("Santa ran out of presents!")
for i in range(n):
    print(' '.join(neighborhood[i]))
if not_happy_kids == 0:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {not_happy_kids} nice kid/s.")

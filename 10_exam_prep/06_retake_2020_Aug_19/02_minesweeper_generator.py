def is_valid_index(row, col):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def cell_result(row, col):
    result = 0
    if is_valid_index(row-1, col):
        if board[row-1][col] == "*":
            result += 1
    if is_valid_index(row+1, col):
        if board[row+1][col] == "*":
            result += 1
    if is_valid_index(row, col-1):
        if board[row][col-1] == "*":
            result += 1
    if is_valid_index(row, col+1):
        if board[row][col+1] == "*":
            result += 1
    if is_valid_index(row-1, col+1):
        if board[row-1][col+1] == "*":
            result += 1
    if is_valid_index(row-1, col-1):
        if board[row-1][col-1] == "*":
            result += 1
    if is_valid_index(row+1, col+1):
        if board[row+1][col+1] == "*":
            result += 1
    if is_valid_index(row+1, col-1):
        if board[row+1][col-1] == "*":
            result += 1
    return result


n = int(input())
number_of_bombs = int(input())

board = []
for r in range(n):
    board.append([0] * n)

for _ in range(number_of_bombs):
    bomb_x, bomb_y = [int(x) for x in input()[1:-1].split(", ")]
    board[bomb_x][bomb_y] = "*"

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] = cell_result(i, j)

for row in range(n):
    print(' '.join(list(map(str,board[row]))))
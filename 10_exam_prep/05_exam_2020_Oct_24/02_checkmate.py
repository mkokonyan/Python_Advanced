def is_valid_index(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True
    return False


def up_vertical_validation(row, col):
    for r in range(row-1, 0, -1):
        if is_valid_index(r, col):
            if board[r][col] == "Q":
                return False
            elif board[r][col] == "K":
                return True
    return False


def down_vertical_validation(row, col):
    for r in range(row+1, 8):
        if is_valid_index(r, col):
            if board[r][col] == "Q":
                return False
            elif board[r][col] == "K":
                return True
    return False


def left_horizontal_validation(row, col):
    for c in range(col-1, 0, -1):
        if is_valid_index(row, c):
            if board[row][c] == "Q":
                return False
            elif board[row][c] == "K":
                return True
    return False


def right_horizontal_validation(row, col):
    for c in range(col+1, 8):
        if is_valid_index(row, c):
            if board[row][c] == "Q":
                return False
            elif board[row][c] == "K":
                return True
    return False

def down_right_diagonal_validation(row, col):
    for r in range(row+1, 8):
        for c in range(col+row, 8):
            if is_valid_index(r, c):
                if board[r][c] == "Q":
                    return False
                elif board[r][c] == "K":
                    return True
    return False

def up_right_diagonal_validation(row, col):
    for r in range(row-1, 0, -1):
        for c in range(col-row, 8):
            if is_valid_index(r, c):
                if board[r][c] == "Q":
                    return False
                elif board[r][c] == "K":
                    return True
    return False


board = []
queens_coords = []
valid_coords = []
for r in range(8):
    board.append(list(input().split()))
    for c in range(8):
        if board[r][c] == "Q":
            queens_coords.append([r, c])

for i in range(len(queens_coords)):
    current_row, current_col = queens_coords[i][0], queens_coords[i][1]
    if up_vertical_validation(current_row, current_col) or down_vertical_validation(current_row, current_col) \
            or left_horizontal_validation(current_row, current_col) or right_horizontal_validation(current_row, current_col):
        valid_coords.append(queens_coords[i])

[print(valid_coords[x]) for x in range(len(valid_coords))]



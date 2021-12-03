def is_valid_index(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True
    return False


def down_vertical(row, col):
    for idx in range(1, 8):
        if is_valid_index(row + idx, col):  # Down Vertical
            if board[row + idx][col] == "Q":
                return False
            elif board[row + idx][col] == "K":
                return True


def up_vertical(row, col):
    for idx in range(1, 8):
        if is_valid_index(row - idx, col):  # Up Vertical
            if board[row - idx][col] == "Q":
                return False
            elif board[row - idx][col] == "K":
                return True


def right_horizontal(row, col):
    for idx in range(1, 8):
        if is_valid_index(row, col + idx):  # Right horizontal
            if board[row][col + idx] == "Q":
                return False
            elif board[row][col + idx] == "K":
                return True


def left_horizontal(row, col):
    for idx in range(1, 8):
        if is_valid_index(row, col - idx):  # Left horizontal
            if board[row][col - idx] == "Q":
                return False
            elif board[row][col - idx] == "K":
                return True


def up_right_diagonal(row, col):
    for idx in range(1, 8):
        if is_valid_index(row - idx, col + idx):  # Up Right Diagonal
            if board[row - idx][col + idx] == "Q":
                return False
            elif board[row - idx][col + idx] == "K":
                return True


def down_right_diagonal(row, col):
    for idx in range(1, 8):
        if is_valid_index(row + idx, col + idx):  # Down Right Diagonal
            if board[row + idx][col + idx] == "Q":
                return False
            elif board[row + idx][col + idx] == "K":
                return True


def up_left_diagonal(row, col):
    for idx in range(1, 8):
        if is_valid_index(row - idx, col - idx):  # Up Left Diagonal
            if board[row - idx][col - idx] == "Q":
                return False
            elif board[row - idx][col - idx] == "K":
                return True


def down_left_diagonal(row, col):
    for idx in range(1, 8):
        if is_valid_index(row + idx, col - idx):  # Down Left Diagonal
            if board[row + idx][col - idx] == "Q":
                return False
            elif board[row + idx][col - idx] == "K":
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
    if down_vertical(current_row, current_col) or up_vertical(current_row, current_col)\
            or right_horizontal(current_row, current_col) or left_horizontal(current_row, current_col) \
            or up_right_diagonal(current_row, current_col) or down_right_diagonal(current_row, current_col) \
            or up_left_diagonal(current_row, current_col) or down_left_diagonal(current_row, current_col):
        valid_coords.append(queens_coords[i])

if valid_coords:
    [print(valid_coords[x]) for x in range(len(valid_coords))]
else:
    print("The king is safe!")

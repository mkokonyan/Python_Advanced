def is_valid_index(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True
    return False


board = []
queens_coords = []
for r in range(8):
    board.append(list(input().split()))
    for c in range(8):
        if board[r][c] == "Q":
            queens_coords.append([r, c])
print(queens_coords)
print(board)

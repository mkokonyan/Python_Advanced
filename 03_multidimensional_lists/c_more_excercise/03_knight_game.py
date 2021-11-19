def is_valid_index(index):
    if 0 <= index < rows:
        return True
    return False

def total_knights_actualization():
    total_knights = {}
    knights = 0
    for i in range(rows):
        for j in range(rows):
            if board[i][j] == "K":
                knights += 1
                current_knight = f"knight{knights}"
                removed_knights = 0
                if is_valid_index(i - 2) and is_valid_index(j - 1):
                    if board[i - 2][j - 1] == "K":
                        removed_knights += 1
                if is_valid_index(i - 2) and is_valid_index(j + 1):
                    if board[i - 2][j + 1] == "K":
                        removed_knights += 1
                if is_valid_index(i - 1) and is_valid_index(j - 2):
                    if board[i - 1][j - 2] == "K":
                        removed_knights += 1
                if is_valid_index(i - 1) and is_valid_index(j + 2):
                    if board[i - 1][j + 2] == "K":
                        removed_knights += 1
                if is_valid_index(i + 1) and is_valid_index(j - 2):
                    if board[i + 1][j - 2] == "K":
                        removed_knights += 1
                if is_valid_index(i + 1) and is_valid_index(j + 2):
                    if board[i + 1][j + 2] == "K":
                        removed_knights += 1
                if is_valid_index(i + 2) and is_valid_index(j - 1):
                    if board[i + 2][j - 1] == "K":
                        removed_knights += 1
                if is_valid_index(i + 2) and is_valid_index(j + 1):
                    if board[i + 2][j + 1] == "K":
                        removed_knights += 1
                total_knights[current_knight] = {"index": (i, j), "removed_knights": removed_knights}
    return total_knights

rows = int(input())
board = []
for idx in range(rows):
    board.append(list(input()))

total_knights = dict(sorted(total_knights_actualization().items(), key=lambda x: -x[1]["removed_knights"]))

is_finished = False
counter = 0
while len(total_knights) > 0:
    is_not_valid = False
    first_key = next(iter(total_knights))
    curr_i, curr_j = total_knights[first_key]["index"]
    for i in range(rows):
        for j in range(rows):
            if board[i][j] == "K":
                if is_valid_index(i - 2) and is_valid_index(j - 1):
                    if board[i - 2][j - 1] == "K":
                        is_not_valid = True
                        break
                if is_valid_index(i - 2) and is_valid_index(j + 1):
                    if board[i - 2][j + 1] == "K":
                        is_not_valid = True
                        break
                if is_valid_index(i - 1) and is_valid_index(j - 2):
                    if board[i - 1][j - 2] == "K":
                        is_not_valid = True
                        break
                if is_valid_index(i - 1) and is_valid_index(j + 2):
                    if board[i - 1][j + 2] == "K":
                        is_not_valid = True
                        break
                if is_valid_index(i + 1) and is_valid_index(j - 2):
                    if board[i + 1][j - 2] == "K":
                        is_not_valid = True
                        break
                if is_valid_index(i + 1) and is_valid_index(j + 2):
                    if board[i + 1][j + 2] == "K":
                        is_not_valid = True
                        break
                if is_valid_index(i + 2) and is_valid_index(j - 1):
                    if board[i + 2][j - 1] == "K":
                        is_not_valid = True
                        break
                if is_valid_index(i + 2) and is_valid_index(j + 1):
                    if board[i + 2][j + 1] == "K":
                        is_not_valid = True
                        break
        if is_not_valid:
            board[curr_i][curr_j] = 0
            counter += 1
            break
        else:
            is_finished = True
    if is_finished:
        break
    else:
        total_knights.clear()
        total_knights = dict(sorted(total_knights_actualization().items(), key=lambda x: -x[1]["removed_knights"]))


print(counter)
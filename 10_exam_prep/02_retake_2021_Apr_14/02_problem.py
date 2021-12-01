def is_valid_index(row, col):
    if 0 <= row < 7 and 0 <= col < 7:
        return True
    return False


def point_counter(row, col):
    result = 0
    if board[row][col] == "D":
        result = (board[row][0] + board[row][-1] + board[0][col] + board[-1][col]) * 2
    elif board[row][col] == "T":
        result = (board[row][0] + board[row][-1] + board[0][col] + board[-1][col]) * 3
    else:
        result = board[row][col]
    return result


player_1, player_2 = input().split(", ")
board = []
for r in range(7):
    board.append([int(x) if x.isdigit() else x for x in input().split()])

player_data = {
    player_1: {"score": 501, "throws": 0},
    player_2: {"score": 501, "throws": 0}
}

current_player_row = 1
while True:
    if current_player_row % 2 == 1:
        current_player = player_1
    else:
        current_player = player_2

    x, y = [int(x) for x in input()[1:-1].split(", ")]
    player_data[current_player]["throws"] += 1
    if is_valid_index(x, y):
        if board[x][y] == "B":
            print(f"{current_player} won the game with {player_data[current_player]['throws']} throws!")
            break
        else:
            player_data[current_player]["score"] -= point_counter(x, y)
    if player_data[current_player]["score"] <= 0:
        print(f"{current_player} won the game with {player_data[current_player]['throws']} throws!")
        break
    current_player_row += 1

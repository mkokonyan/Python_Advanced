def is_valid_hit(row, col):
    if 0 <= row <= 6 and 0 <= col <= 6:
        return True
    return False


def sum_of_score(row, col):
    left_score = int(board[row][0])
    right_score = int(board[row][-1])
    up_score = int(board[0][col])
    down_score = int(board[-1][col])
    return left_score + right_score + up_score + down_score


player_one, player_two = input().split(", ")
board = []
for r in range(7):
    board.append(input().split())

players_data = {player_one: {"score": 501, "throws": 0},
                player_two: {"score": 501, "throws": 0}
                }

current_hit = input()
index = 1
while current_hit:
    row_hit, col_hit = [int(x) for x in current_hit[1:-1].split(", ")]

    if index % 2 == 1:
        current_player = player_one
    else:
        current_player = player_two
    players_data[current_player]["throws"] += 1
    if is_valid_hit(row_hit, col_hit):
        if board[row_hit][col_hit] == "B":
            print(f"{current_player} won the game with {players_data[current_player]['throws']} throws!")
            break
        elif board[row_hit][col_hit] == "D":
            players_data[current_player]["score"] -= sum_of_score(row_hit, col_hit) * 2
        elif board[row_hit][col_hit] == "T":
            players_data[current_player]["score"] -= sum_of_score(row_hit, col_hit) * 3
        else:
            players_data[current_player]["score"] -= int(board[row_hit][col_hit])
    if players_data[current_player]["score"] <= 0:
        print(f"{current_player} won the game with {players_data[current_player]['throws']} throws!")
        break
    current_hit = input()
    index += 1

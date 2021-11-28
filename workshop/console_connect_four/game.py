DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMNS_COUNT = 7
DEFAULT_WIN_CONDITION_COUNT = 4


def create_board(rows_count=DEFAULT_ROWS_COUNT, columns_count=DEFAULT_COLUMNS_COUNT):
    return [[0] * columns_count for _ in range(rows_count)]


def get_player_choice(player):
    print(f"Player {player}, please choose a column")
    return int(input()) - 1


def get_lowest_row_index(board, column_index):
    rows_count = len(board)
    for row_index in range(rows_count - 1, -1, -1):
        if board[row_index][column_index] == 0:
            return row_index
    return None


def apply_player_choice(board, column_index, player):
    row_index = get_lowest_row_index(board, column_index)
    board[row_index][column_index] = player


def in_range(value, max_value):
    return 0 <= value < max_value


def is_win_condition_value(board, row_index, column_index, player, rows_count, columns_count):
    return in_range(row_index, rows_count) \
           and in_range(column_index, columns_count) \
           and board[row_index][column_index] == player


def has_win_condition_from_position(board, row_index, column_index,
                                    player, win_condition_count=DEFAULT_WIN_CONDITION_COUNT):
    rows_count = len(board)
    columns_count = len(board[0])

    left_horizontal_values = [
        is_win_condition_value(board, row_index, column_index + d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    right_horizontal_values = [
        is_win_condition_value(board, row_index, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    down_vertical_values = [
        is_win_condition_value(board, row_index + d, column_index, player, rows_count, columns_count)
        for d in range(win_condition_count)]
    down_left_diagonal_values = [
        is_win_condition_value(board, row_index + d, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    down_right_diagonal_values = [
        is_win_condition_value(board, row_index + d, column_index + d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    up_left_diagonal_values = [
        is_win_condition_value(board, row_index - d, column_index - d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    up_right_diagonal_values = [
        is_win_condition_value(board, row_index - d, column_index + d, player, rows_count, columns_count)
        for d in range(win_condition_count)]

    return all(left_horizontal_values) or all(right_horizontal_values) or all(down_vertical_values) \
           or all(down_left_diagonal_values) or all(down_right_diagonal_values) \
           or all(up_left_diagonal_values) or all(up_right_diagonal_values)


def has_win_condition(board, player):
    rows_count = len(board)
    for row_index in range(rows_count):
        columns_count = len(board[row_index])
        for column_index in range(columns_count):
            if has_win_condition_from_position(board, row_index, column_index, player):
                return True
    return False


def print_board(board):
    for row in board:
        print(row)


def is_choice_valid(board, choice):
    return 0 <= choice < len(board[0]) and board[0][choice] == 0


def print_winner_message(player):
    print(f"The winner is player {player}")


def print_invalid_choice_message(player):
    print(f"Invalid choice by player {player}. Try again")


def play(board, player=1):
    while True:
        player_choice = get_player_choice(player)
        if not is_choice_valid(board, player_choice):
            print_invalid_choice_message(player)
            continue
        apply_player_choice(board, player_choice, player)
        print_board(board)
        if has_win_condition(board, player):
            print_winner_message(player)
            break
        player = 2 if player == 1 else 1


board = create_board()
play(board)

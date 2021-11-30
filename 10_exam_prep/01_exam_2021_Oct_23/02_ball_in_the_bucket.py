def is_valid_index(row, col):
    if 0 <= row < 6 and 0 <= col < 6:
        return True
    return False


board = []
hitted_buckets = []

points_collected = 0
for row in range(6):
    board.append([int(x) if x.isdigit() else x for x in input().split()])
for throw in range(3):
    row, col = [int(x) for x in input()[1:-1].split(", ")]
    if is_valid_index(row,col) and board[row][col] == "B":
        if not (row, col) in hitted_buckets:
            hitted_buckets.append((row, col))
            for r in range(6):
                if not board[r][col] == "B":
                    points_collected += board[r][col]

won_prize = None
if 100 <= points_collected <= 199:
    won_prize = "Football"
elif 200 <= points_collected <= 299:
    won_prize = "Teddy Bear"
elif points_collected >= 300:
    won_prize = "Lego Construction Set"

if points_collected < 100:
    print(f"Sorry! You need {100-points_collected} points more to win a prize.")
else:
    print(f"Good job! You scored {points_collected} points, and you've won {won_prize}.")
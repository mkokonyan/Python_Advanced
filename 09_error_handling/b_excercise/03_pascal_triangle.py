def generate_empty_triangle(size):
    triangle = []
    for r in range(size):
        triangle.append([0] * (r + 1))
    return triangle


def populate_triangle(triangle):
    triangle[0][0] = 1
    for row_idx, row in enumerate(triangle):
        for col_idx, col in enumerate(row):
            left = right = 0
            if (row_idx, col_idx) == (0, 0):
                continue
            if (0 <= row_idx - 1 < len(triangle)) and (0 <= col_idx - 1 < len(triangle[row_idx - 1])):
                left = triangle[row_idx - 1][col_idx - 1]
            if (0 <= row_idx - 1 < len(triangle)) and (0 <= col_idx < len(triangle[row_idx - 1])):
                right = triangle[row_idx - 1][col_idx]
            triangle[row_idx][col_idx] = left + right


def get_magic_triangle(n):
    triangle = generate_empty_triangle(n)
    populate_triangle(triangle)
    return triangle


if __name__ == '__main__':
    print(get_magic_triangle(5))

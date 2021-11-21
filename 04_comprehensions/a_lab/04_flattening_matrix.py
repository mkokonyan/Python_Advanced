n = int(input())

matrix = [[int(el) for el in (input().split(", "))] for _ in range(n)]
flatten_nums = [num for sublist in matrix for num in sublist]
print(flatten_nums)


n = list(map(int, input().split()))
result = []
for i in range(len(sorted(n, reverse=True))):
    result.append(n.pop())
print(*result)


# numbers = input().split()
# for i in range(len(numbers)):
#     print(numbers.pop(), end=" ")
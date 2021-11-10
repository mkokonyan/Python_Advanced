n =list(map(int, input().split()))
result = []
for i in range(len(sorted(n, reverse=True))):
    result.append(n.pop())
print(*result)
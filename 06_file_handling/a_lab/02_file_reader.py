file = open("numbers.txt")
result = 0

for line in file:
    result += int(line)

print(sum([int(line) for line in open("numbers.txt")]))
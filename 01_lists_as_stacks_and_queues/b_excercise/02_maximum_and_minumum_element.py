lines = int(input())
stack = []
for i in range(lines):
    command = input()
    if "1" in command:
        stack.append(int(command.split()[1]))
    if stack:
        if command == "2":
            stack.pop()
        elif command == "3":
            print(max(stack))
        elif command == "4":
            print(min(stack))
result = []
while stack:
    result.append(stack.pop())
print(", ".join(list(map(str, result))))

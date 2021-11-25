command = input()
numbers = [int(el) for el in input().split()]

if command == "Even":
    filtered = filter(lambda x: x % 2 ==0, numbers)
elif command == "Odd":
    filtered = filter(lambda x: x % 2 !=0, numbers)

result = sum(filtered) * len(numbers)
print(result)
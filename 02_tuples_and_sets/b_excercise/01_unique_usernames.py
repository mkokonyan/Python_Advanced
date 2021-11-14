number_of_names = int(input())
unique_names = set()
for i in range(number_of_names):
    name = input()
    unique_names.add(name)

[print(x) for x in unique_names]
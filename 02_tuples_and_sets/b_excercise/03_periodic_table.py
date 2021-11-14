lines_count = int(input())
chemical_element = set()
for el in range(lines_count):
    for e in input().split():
        chemical_element.add(e)

[print(x) for x in chemical_element]
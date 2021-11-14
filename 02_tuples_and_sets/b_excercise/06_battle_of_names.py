lines = int(input())
odd_set = set()
even_set = set()
for i in range(1, lines + 1):
    name = input()
    name_sum = 0
    for ch in name:
        name_sum += ord(ch)
    name_sum //= i
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    print(f"{', '.join(list(map(str, odd_set.union(even_set))))}")
elif sum(odd_set) > sum(even_set):
    print(f"{', '.join(list(map(str, odd_set.difference(even_set))))}")
elif sum(odd_set) < sum(even_set):
    print(f"{', '.join(list(map(str, odd_set.symmetric_difference(even_set))))}")

# lines = int(input())
# odd_set = set()
# even_set = set()
# for i in range(1, lines + 1):
#     name = input()
#     name_sum = 0
#     for ch in name:
#         name_sum += ord(ch)
#     name_sum //= i
#     if name_sum % 2 == 0:
#         even_set.add(name_sum)
#     else:
#         odd_set.add(name_sum)
#
# if sum(odd_set) == sum(even_set):
#     print(f"{', '.join(list(map(str, odd_set.union(even_set))))}")
# elif sum(odd_set) > sum(even_set):
#     print(f"{', '.join(list(map(str, odd_set.difference(even_set))))}")
# elif sum(odd_set) < sum(even_set):
#     print(f"{', '.join(list(map(str, odd_set.symmetric_difference(even_set))))}")

n = int(input())

even_numbers_set = set()
odd_numbers_set = set()
for i in range(1, n+1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // i
    if current_sum % 2 == 0:
        even_numbers_set.add(current_sum)
    else:
        odd_numbers_set.add(current_sum)

sum_evens = sum(even_numbers_set)
sum_odds = sum(odd_numbers_set)

if sum_evens == sum_odds:
    print(f"{', '.join([str(el) for el in even_numbers_set.union(odd_numbers_set)])}")
elif sum_odds > sum_evens:
    print(f"{', '.join([str(el) for el in odd_numbers_set.difference(even_numbers_set)])}")
else:
    print(f"{', '.join([str(el) for el in odd_numbers_set.symmetric_difference(even_numbers_set)])}")
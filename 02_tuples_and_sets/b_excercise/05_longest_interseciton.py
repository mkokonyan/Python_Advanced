# n = int(input())
# range_1 = set()
# range_2 = set()
# max_interesting_lenght = 0
# intersection_range = set()
# for i in range(n):
#     first_range, second_range = input().split("-")
#     first_start, first_end = first_range.split(",")
#     second_start, second_end = second_range.split(",")
#     for r1 in range(int(first_start), int(first_end)+1):
#         range_1.add(r1)
#     for r2 in range(int(second_start), int(second_end)+1):
#         range_2.add(r2)
#     if len(range_1.intersection(range_2)) >= max_interesting_lenght:
#         max_interesting_lenght = len(range_1.intersection(range_2))
#         intersection_range = range_1.intersection(range_2)
#     range_1.clear()
#     range_2.clear()
# print(f"Longest intersection is [{', '.join(list(map(str,intersection_range)))}] with length {max_interesting_lenght}")

n = int(input())

intersections = []
for _ in range(n):
    data = input()
    first_seq_data, second_seq_data = data.split("-")
    start, stop = [int(el) for el in first_seq_data.split(",")]
    first_seq = range(start, stop+1)
    start, stop = [int(el) for el in second_seq_data.split(",")]
    second_seq = range(start, stop+1)
    intersection = set(first_seq).intersection(second_seq)
    intersections.append(intersection)
longest = sorted(intersections, key=lambda x: -len(x))[0]
print(f"Longest intersection is {list(longest)} with length {len(longest)}")
clothes_in_box = [int(x) for x in input().split()]
rack = int(input())
clothes_sum = 0
rack_counter = 1
current_rack = rack
while clothes_in_box:
    last_clothes = clothes_in_box.pop()
    if not last_clothes <= current_rack:
        rack_counter += 1
        current_rack = rack
    current_rack -= last_clothes
print(rack_counter)

from collections import deque

cups = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))
wasted_litters = 0
while cups:
    if bottles:
        current_bottle = bottles.pop()
        if current_bottle > cups[0]:
            wasted_litters += current_bottle - cups[0]
        cups[0] -= current_bottle
        if cups[0] <= 0:
            cups.popleft()
    else:
        break
if bottles:
    print(f"Bottles: {' '.join(list(map(str,bottles)))}")
else:
    print(f"Cups: {' '.join(list(map(str, cups)))}")
print(f"Wasted litters of water: {wasted_litters}")

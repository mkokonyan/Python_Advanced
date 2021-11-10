from collections import deque

food_quantity = int(input())
queue = deque([int(x) for x in input().split()])
print(max(queue))
orders_complete = True
while queue:
    if food_quantity >= queue[0]:
        food_quantity -= queue.popleft()
    else:
        orders_complete = False
        print(f"Orders left: {' '.join(list(map(str, queue)))}")
        break
if orders_complete:
    print("Orders complete")


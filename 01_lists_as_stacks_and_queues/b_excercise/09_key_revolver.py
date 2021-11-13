from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

bullet_count = 0
is_unlocked = False
while bullets:
    if bullet_count % gun_barrel_size == 0 and not bullet_count == 0:
        print("Reloading!")
    bullets_left = gun_barrel_size
    bullet_count += 1
    current_bullet = bullets.pop()
    current_lock = locks[0]
    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
        if not locks:
            is_unlocked = True
            if bullet_count % gun_barrel_size == 0:
                if bullets:
                    print("Reloading!")
            break
    else:
        print("Ping!")

bullet_cost = bullet_count * bullet_price
earned = intelligence_value - bullet_cost
if is_unlocked:
    print(f"{len(bullets)} bullets left. Earned ${earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
from collections import deque


def is_succeeded():
    if created_fireworks["Palm Fireworks"] >= 3 \
            and created_fireworks["Willow Fireworks"] >= 3 \
            and created_fireworks["Crossette Fireworks"] >= 3:
        return True
    return False


fireworks = [int(x) for x in input().split(", ") if int(x) > 0]
fireworks = deque(fireworks)
explosive_power = [int(x) for x in input().split(", ") if int(x) > 0]

created_fireworks = {"Palm Fireworks": 0,
                     "Willow Fireworks": 0,
                     "Crossette Fireworks": 0
                     }

while True:
    if fireworks and explosive_power:
        current_firework = fireworks.popleft()
        current_explosive_power = explosive_power.pop()
        fireworks_sum = current_firework + current_explosive_power
        if fireworks_sum % 3 == 0 and not fireworks_sum % 5 == 0:
            created_fireworks["Palm Fireworks"] += 1
        elif not fireworks_sum % 3 == 0 and fireworks_sum % 5 == 0:
            created_fireworks["Willow Fireworks"] += 1
        elif fireworks_sum % 3 == 0 and fireworks_sum % 5 == 0:
            created_fireworks["Crossette Fireworks"] += 1
        else:
            current_firework -= 1
            if current_firework > 0:
                fireworks.append(current_firework)
                explosive_power.append(current_explosive_power)
            else:
                explosive_power.append(current_explosive_power)
    if len(fireworks) <= 0 or len(explosive_power) <= 0 or is_succeeded():
        break

if is_succeeded():
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: {', '.join(list(map(str, fireworks)))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(list(map(str, explosive_power)))}")
for key, value in created_fireworks.items():
    print(f"{key}: {value}")

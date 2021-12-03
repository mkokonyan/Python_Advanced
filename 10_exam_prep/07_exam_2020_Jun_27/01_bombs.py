from collections import deque

effects = [int(x) for x in input().split(", ")]
effects = deque(effects)
castings = [int(x) for x in input().split(", ")]

bombs_created = {"Cherry Bombs": 0,
                 "Datura Bombs": 0,
                 "Smoke Decoy Bombs": 0
                 }
is_succeeded = False

while effects and castings:
    current_effect = effects[0]
    current_casting = castings[-1]
    mixed_sum = current_effect + current_casting
    if mixed_sum == 40:
        bombs_created["Datura Bombs"] += 1
        effects.popleft()
        castings.pop()
    elif mixed_sum == 60:
        bombs_created["Cherry Bombs"] += 1
        effects.popleft()
        castings.pop()
    elif mixed_sum == 120:
        bombs_created["Smoke Decoy Bombs"] += 1
        effects.popleft()
        castings.pop()
    else:
        castings[-1] -= 5
    if bombs_created["Datura Bombs"] >= 3 and bombs_created["Cherry Bombs"] >= 3 \
            and bombs_created["Smoke Decoy Bombs"] >= 3:
        is_succeeded = True
        break

if is_succeeded:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effects:
    print(f"Bomb Effects: {', '.join(list(map(str,effects)))}")
else:
    print(f"Bomb Effects: empty")
if castings:
    print(f"Bomb Casings: {', '.join(list(map(str,castings)))}")
else:
    print(f"Bomb Casings: empty")
for key, value in bombs_created.items():
    print(f"{key}: {value}")

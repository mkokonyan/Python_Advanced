from collections import deque

litters = int(input())
queues = deque()
name = input()
while not name == "Start":
    queues.append(name)
    name = input()

command = input()
while not command == "End":
    if command.startswith("refill"):
        litters += int(command.split()[-1])
    else:
        litters_wanted = int(command)
        name = queues.popleft()
        if litters >= litters_wanted:
            litters -= litters_wanted
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    command = input()
print(f"{litters} liters left")
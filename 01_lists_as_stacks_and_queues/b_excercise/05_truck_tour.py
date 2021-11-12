from collections import deque

index_of_pumps = [x for x in range(0, int(input()))]
petrol_deque = deque()
distance_deque = deque()

for ind in range(len(index_of_pumps)):
    amount_of_petrol, distance = input().split()
    amount_of_petrol = int(amount_of_petrol)
    distance = int(distance)
    distance_deque.append(distance)
    petrol_deque.append(amount_of_petrol)
index = 0
current_petrol = 0
is_finished = False
while True:
    if is_finished:
        break
    for i in range(0, len(index_of_pumps)):
        current_petrol += petrol_deque[i]
        current_distance = distance_deque[i]
        if current_petrol >= current_distance:
            current_petrol -= current_distance
            if i == len(index_of_pumps) - 1:
                if current_petrol >= 0:
                    print(index_of_pumps[index])
                    is_finished = True
        else:
            distance_deque.append(distance_deque.popleft())
            petrol_deque.append(petrol_deque.popleft())
            index += 1
            current_petrol = 0
            break
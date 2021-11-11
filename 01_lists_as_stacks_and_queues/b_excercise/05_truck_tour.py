from collections import deque

index_of_pumps = [x for x in range(0, int(input()))]
distance_deque = deque()
petrol_deque = deque()
for i in range(len(index_of_pumps)):
    amount_of_petrol, distance = input().split()
    amount_of_petrol = int(amount_of_petrol)
    distance = int(distance)
    distance_deque.append(distance)
    petrol_deque.append(amount_of_petrol)
index = 0
current_index = 0
current_distance = 0
current_petrol = 0
while True:
    if distance_deque[current_index] <= petrol_deque[current_index]:
        current_distance = distance_deque[current_index]
        current_petrol = petrol_deque[current_index]
        current_petrol -= current_distance
    else:
        distance_deque.append(distance_deque.popleft())
        petrol_deque.append(petrol_deque.popleft())
    index += 1
    if current_petrol == 0:
        print(index_of_pumps[index])
        break

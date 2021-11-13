# from collections import deque
#
# index_of_pumps = [x for x in range(0, int(input()))]
# petrol_deque = deque()
# distance_deque = deque()
#
# for ind in range(len(index_of_pumps)):
#     amount_of_petrol, distance = input().split()
#     amount_of_petrol = int(amount_of_petrol)
#     distance = int(distance)
#     distance_deque.append(distance)
#     petrol_deque.append(amount_of_petrol)
# index = 0
# current_petrol = 0
# is_finished = False
# while True:
#     if is_finished:
#         break
#     for i in range(0, len(index_of_pumps)):
#         current_petrol += petrol_deque[i]
#         current_distance = distance_deque[i]
#         if current_petrol >= current_distance:
#             current_petrol -= current_distance
#             if i == len(index_of_pumps) - 1:
#                 if current_petrol >= 0:
#                     print(index_of_pumps[index])
#                     is_finished = True
#         else:
#             distance_deque.append(distance_deque.popleft())
#             petrol_deque.append(petrol_deque.popleft())
#             index += 1
#             current_petrol = 0
#             break

from collections import deque

queue = deque()
n = int(input())
for _ in range(n):
    gas_pump = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])

for i in range(n):
    fuel_tank = 0
    gas_pumps_traveled = 0
    for gas_pump in queue:
        fuel, distance_to_next = gas_pump[0], gas_pump[1]
        fuel_tank += fuel
        if fuel_tank < distance_to_next:
            break
        fuel_tank -= distance_to_next
        gas_pumps_traveled +=1
    if gas_pumps_traveled == len(queue):
        print(i)
        break
    queue.rotate(-1)

def time_print(time):
    hours = time // 3600
    time -= hours * 3600
    if hours > 23:
        hours = 0
    minutes = time // 60
    seconds = time % 60
    return f"[{hours:02d}:{minutes:02d}:{seconds:02d}]"


from collections import deque

data_line = input().split(";")
robot_names = []
time_processing = []

for i in range(len(data_line)):
    name, time = data_line[i].split("-")
    robot_names.append(name)
    time_processing.append(int(time))

starting_time = input().split(":")
current_time = int(starting_time[2]) + 60 * int(starting_time[1]) + 3600 * int(starting_time[0])

product = input()
product_line = deque()
robot_active_time = [0] * len(robot_names)

while not product == "End":
    product_line.append(product)
    product = input()


while product_line:
    current_time += 1
    for i in range(0, len(robot_names)):
        if robot_active_time[i] == 0:
            robot_active_time[i] += current_time + time_processing[i]
            print(f"{robot_names[i]} - {product_line.popleft()} {time_print(current_time)}")
            break
        elif current_time >= robot_active_time[i]:
            robot_active_time[i] += time_processing[i]
            print(f"{robot_names[i]} - {product_line.popleft()} {time_print(current_time)}")
            break
        else:
            if i == len(robot_names) - 1:
                product_line.append(product_line.popleft())

from collections import deque

green_light_duration = int(input())
free_window = int(input())
data = input()
is_crashed = False
total_cars_passed = 0

current_green = green_light_duration
current_free_window = free_window
while not data == "END":
    if not data == "green":
        car_model = deque(list(data))
        for i in range(len(car_model)):
            if current_green >= 1:
                current_green -= 1
            else:
                current_green = 0
                current_free_window -= 1
            if current_free_window < 0:
                is_crashed = True
                print("A crash happened!")
                print(f"{data} was hit at {car_model[0]}.")
                break
            car_model.popleft()
        if not car_model:
            total_cars_passed += 1
    else:
        current_green = green_light_duration
        current_free_window = free_window
    if current_green > 0:
        data = input()
    else:
        break
if not is_crashed:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")

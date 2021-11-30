from collections import deque

pizza_orders = [int(el) for el in input().split(", ") if 0 < int(el) <= 10]
pizza_orders = deque(pizza_orders)
employees_capacity = [int(el) for el in input().split(", ")]

pizzas_made = 0
while True:
    if pizza_orders and employees_capacity:
        current_order = pizza_orders.popleft()
        current_employee = employees_capacity.pop()
        if current_order > current_employee:
            pizzas_made += current_employee
            diff = current_order - current_employee
            pizza_orders.appendleft(diff)
        else:
            pizzas_made += current_order
    else:
        break

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    if employees_capacity:
        print(f"Employees: {', '.join(list(map(str, employees_capacity)))}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(list(map(str, pizza_orders)))}")

from collections import deque

customers = [int(el) for el in input().split(", ")]
customers = deque(customers)
taxis = [int(el) for el in input().split(", ")]

total_time = 0
while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis[-1]
    if current_customer <= current_taxi:
        total_time += current_customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()
if not customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
else:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(list(map(str, customers)))}")
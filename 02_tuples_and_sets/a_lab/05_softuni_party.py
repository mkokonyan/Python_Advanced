n = int(input())
all_guests = set()

for _ in range(n):
    all_guests.add(input())

ticket = input()

arrived = set()
while not ticket == "END":
    arrived.add(ticket)
    ticket = input()

print(len(all_guests.difference(arrived)))
for ticket in sorted([x if x[0].isdigit() else x for x in all_guests.difference(arrived)]):
    print(ticket)

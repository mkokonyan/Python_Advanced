def flights(*args):
    flights_data = {}
    destination = None
    for i in range(len(args)):
        if not args[i] == "Finish":
            if not isinstance(args[i], int):
                destination = args[i]
                if destination not in flights_data:
                    flights_data[destination] = 0
            else:
                passengers = args[i]
                if destination in flights_data:
                    flights_data[destination] += passengers
        else:
            break
    return flights_data


print(flights('Vienna', 256, 'Vienna', 26,
              'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215,
              'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

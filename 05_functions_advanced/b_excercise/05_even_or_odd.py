def is_even(num):
    return num % 2 == 0
def is_odd(num):
    return not is_even(num)


def even_odd(*args):
    command = args[len(args) - 1]
    numbers = args[0:-1]
    if command == "even":
        return list(filter(is_even, numbers))
    elif command == "odd":
        return list(filter(is_odd, numbers))

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

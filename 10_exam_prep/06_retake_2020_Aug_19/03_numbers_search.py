def numbers_searching(*args):
    duplicates = []
    missing_value = 0
    numbers = sorted(set(args))
    for i in range(numbers[0], numbers[-1]+1):
        if i not in numbers:
            missing_value = i
        if args.count(i) > 1:
            duplicates.append(i)
    result = [missing_value, sorted(duplicates)]

    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
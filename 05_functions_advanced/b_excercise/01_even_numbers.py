def is_even(num):
    return num % 2 == 0

def myfilter(filter_func, sequence):
    filtered = []
    for element in sequence:
        if filter_func(element) is True:
            filtered.append(element)
    return filtered


print(list(myfilter(is_even, [int(word) for word in input().split()])))

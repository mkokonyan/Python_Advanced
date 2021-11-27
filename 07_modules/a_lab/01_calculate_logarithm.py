from math import log


def calc_log(x, b):
    if b == "natural":
        return log(x)
    else:
        return log(x, b)


tests = [
    ('natural', 10),
    (2, 1024)
]

[print(f"{calc_log(x, b):.2f}") for (b, x) in tests]


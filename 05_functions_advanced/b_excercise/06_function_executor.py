def func_executor(*funcs_with_args):
    res = []

    for func, fargs in funcs_with_args:
        func_result = func(*fargs)
        res.append(func_result)
    return res

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

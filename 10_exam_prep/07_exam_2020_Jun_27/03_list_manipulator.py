def list_manipulator(nums, second_param, third_param, *args):
    result = None
    if second_param == "add" and third_param == "beginning":
        result = list(args) + nums
    elif second_param == "add" and third_param == "end":
        result = nums + list(args)
    elif second_param == "remove" and third_param == "beginning":
        if args:
            removed_numbers = args[0]
            result = nums[removed_numbers::]
        else:
            nums.pop(0)
            result = nums
    elif second_param == "remove" and third_param == "end":
        if args:
            removed_numbers = args[0]
            result = nums[:len(nums)-removed_numbers]
        else:
            nums.pop(-1)
            result = nums
    return result


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

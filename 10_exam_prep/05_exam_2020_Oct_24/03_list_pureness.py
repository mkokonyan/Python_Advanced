from collections import deque

def best_list_pureness(nums, k):
    nums = deque(nums)
    best_pureness = 0
    best_rotation = 0
    for i in range(k+1):
        pureness = 0
        for j in range(len(nums)):
            pureness += j * nums[j]
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = i
        nums.rotate(1)
    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

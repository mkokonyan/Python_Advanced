numbers = [int(el) for el in input().split()]
positive = filter(lambda num: num >= 0, numbers)
negative = filter(lambda num: num < 0, numbers)
sum_positive = sum(positive)
sum_negative = sum(negative)

print(sum_negative)
print(sum_positive)
if sum_positive > abs(sum_negative):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")

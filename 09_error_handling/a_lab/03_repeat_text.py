text = input()

try:
    number = int(input())
    print(text*number)
except ValueError:
    print("Variable times must be an integer")
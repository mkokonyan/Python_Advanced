text = input()

try:
    number = int(input())
except ValueError:
    print("Variable times must be an integer")
else:
    print(text*number)
finally:
    print("Printed no matter what")
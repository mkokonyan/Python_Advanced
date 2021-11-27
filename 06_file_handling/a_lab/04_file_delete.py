import os

try:
    os.remove("asd.txt")
except FileNotFoundError:
    print("File already removed")

#Option Two
# if os.path.exists("asd.txt"):
#     os.remove("asd.txt")
# else:
#     print("File already removed")
from os import path

#First
if path.exists("text.txt"):
    print("File found")
else:
    print("File not found")

#Second way
try:
    open("text .txt")
    print("File found")
except FileNotFoundError:
    print("File not found")
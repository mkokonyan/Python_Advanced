sequence = input()
stack = []
is_valid = False
for index in range(len(sequence)):
    char = sequence[index]
    oposite_char = ""
    if char == "}" or char == "]":
        oposite_char = chr(ord(char) - 2)
    else:
        oposite_char = chr(ord(char) - 1)
    if char == "{" or char == "[" or char == "(":
        stack.append(char)
    if stack:
        if oposite_char == stack[-1]:
            stack.pop()
            if not stack and index == len(sequence) - 1:
                is_valid = True
                break
    else:
        break
if is_valid:
    print("YES")
else:
    print("NO")
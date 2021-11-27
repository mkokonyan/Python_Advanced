import re

with open("text.txt") as file:
    lines = file.readlines()

for idx, line in enumerate(lines):
    if not idx % 2 == 0:
        continue
    current_line = re.sub(r"[-,.!?]", "@", line)
    current_line = ' '.join(reversed(current_line.split()))
    print(current_line.strip())


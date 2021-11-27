import re

with open("words.txt") as file:
    searched_words = file.read().split()

occs = {}

with open("input.txt") as file:
    content = file.read().lower()
    for s_word in searched_words:
        result = re.findall(rf"(?<=(-|\s)){s_word}(?=(.|))", content)
        occs[s_word] = len(result)

sorted_result = sorted(occs.items(), key=lambda x: -x[1])
for key, value in sorted_result:
    print(f"{key}-{value}")
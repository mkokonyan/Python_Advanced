from collections import deque

males = [int(x) for x in input().split() if int(x) > 0]
females = [int(x) for x in input().split() if int(x) > 0]
females = deque(females)

matches = 0
while True:
    if males and females:
        current_male = males[-1]
        current_female = females[0]
        if current_male % 25 == 0:
            males.pop()
            if males:
                males.pop()
                continue
            else:
                break
        if current_female % 25 == 0:
            females.popleft()
            if females:
                females.popleft()
                continue
            else:
                break
        if current_male == current_female:
            males.pop()
            females.popleft()
            matches += 1
        else:
            males[-1] -= 2
            if males[-1] <= 0:
                males.pop()
            females.popleft()

    else:
        break

print(f"Matches: {matches}")
if not males:
    print(f"Males left: none")
else:
    print(f"Males left: {', '.join(list(map(str, males[::-1])))}")
if not females:
    print(f"Females left: none")
else:
    print(f"Females left: {', '.join(list(map(str, females)))}")
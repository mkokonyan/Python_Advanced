text = input()
for ch in sorted(set(text)):
    print(f"{ch}: {text.count(ch)} time/s")

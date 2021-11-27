import os

_, _, files = next(os.walk(input()))
by_extensions = {}
for file in files:
    ext = file.split(".")[-1]
    if ext not in by_extensions:
        by_extensions[ext] = []

    by_extensions[ext].append(file)

with open(os.path.expanduser('~/Desktop/report.txt'), 'w') as out_file:
    for ext in sorted(by_extensions.keys()):
        files = sorted(by_extensions[ext])
        out_file.write(f".{ext}\n")
        for file in files:
            out_file.write(f"---{file}\n")
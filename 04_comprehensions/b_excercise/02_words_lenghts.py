print(', '.join([f"{name} -> {len(name)}" for name in input().split(',')]))

print(*[f"{name} -> {len(name)}" for name in input().split(',')], sep=", ")
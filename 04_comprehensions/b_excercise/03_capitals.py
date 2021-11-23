countries = input().split(', ')
capitals = input().split(', ')

result = {countries[index]:capitals[index] for index in range(len(countries))}
print(*[f"{key} -> {value}" for key, value in result.items()], sep='\n')
from collections import deque


def is_gift_created(product_sum):
    if 100 <= product_sum <= 199:
        if not "Gemstone" in presents:
            presents["Gemstone"] = 0
        presents["Gemstone"] += 1
        return True
    elif 200 <= product_sum <= 299:
        if not "Porcelain Sculpture" in presents:
            presents["Porcelain Sculpture"] = 0
        presents["Porcelain Sculpture"] += 1
        return True
    elif 300 <= product_sum <= 399:
        if not "Gold" in presents:
            presents["Gold"] = 0
        presents["Gold"] += 1
        return True
    elif 400 <= product_sum <= 499:
        if not "Diamond Jewellery" in presents:
            presents["Diamond Jewellery"] = 0
        presents["Diamond Jewellery"] += 1
        return True
    return False


def invalid_product_sum(material, magic, product_sum):
    if product_sum < 100:
        if product_sum % 2 == 0:
            rev_product = material * 2 + magic * 3
        else:
            rev_product = product_sum * 2
    else:
        rev_product = material // 2 + magic // 2
    return rev_product


materials = [int(x) for x in input().split()]
magic_levels = [int(x) for x in input().split()]
magic_levels = deque(magic_levels)

presents = {}

while True:
    if not len(materials) == 0 and not len(magic_levels) == 0:
        current_material = materials.pop()
        current_magic_level = magic_levels.popleft()
        product_sum = current_material + current_magic_level
        if not is_gift_created(product_sum):
            is_gift_created(invalid_product_sum(current_material, current_magic_level, product_sum))
    else:
        break

if ("Gemstone" in presents and "Porcelain Sculpture" in presents) \
        or ("Gold" in presents and "Diamond Jewellery" in presents):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(list(map(str, materials)))}")
if magic_levels:
    print(f"Magic left: {', '.join(list(map(str, magic_levels)))}")

for key, value in sorted(presents.items()):
    print(f"{key}: {value}")

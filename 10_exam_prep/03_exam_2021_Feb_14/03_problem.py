def stock_availability(inventory, action, *args):
    if action == "delivery":
        for el in args:
            inventory.append(el)
    elif action == "sell":
        if args:
            if isinstance(args[0], int):
                inventory = inventory[args[0]:]
            else:
                for i in range(len(args)):
                    if args[i] in inventory:
                        inventory = list(filter(lambda x: x != args[i], inventory))
        else:
            inventory.pop(0)
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

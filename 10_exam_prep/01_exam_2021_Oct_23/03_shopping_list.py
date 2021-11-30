def shopping_list(budget, **kwargs):
    buyed_products = []
    if budget < 100:
        return "You do not have enough budget."
    for product_name, value in kwargs.items():
        price, quantity = [float(x) for x in value]
        total_price = price * quantity
        if total_price <= budget:
            budget -= total_price
            if len(buyed_products) < 5:
                buyed_products.append(f"You bought {product_name} for {total_price:.2f} leva.")
            else:
                break
    return "\n".join(buyed_products)



print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

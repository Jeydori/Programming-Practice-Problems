#Sequential Problem 6
item_names = []
item_prices = []

while True:
    item_name = input("Enter the name of the item (or 'done' to finish): ")
    if item_name.lower() == 'done':
        break
    item_price = float(input("Enter the price of the item: "))
    item_names.append(item_name)
    item_prices.append(item_price)

    for n, p in zip(item_names, item_prices):
        print(n, ':', p)

subtotal = sum(item_prices)
total_cost = subtotal * (1 + 0.1)

for n, p in zip(item_names, item_prices):
    print(n, ':', p)

print("Total cost including tax: ", total_cost, 'php')

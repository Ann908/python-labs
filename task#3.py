list_products = [
    {'product': 'apple', 'quantity': 12, 'cost': 100},
    {'product': 'apple', 'quantity': 10, 'cost': 50},
    {'product': 'chery', 'quantity': 15, 'cost': 80},
    {'product': 'pineapple', 'quantity': 3, 'cost': 200},
    {'product': 'pineapple', 'quantity': 6, 'cost': 200},
    {'product': 'strawberry', 'quantity': 2, 'cost': 30}
]

def cost_product(list_products):
    total_cost = {}
    for item in list_products:
        product_ = item['product']
        quantity_ = item['quantity']
        cost_ = item['cost']
        total = quantity_ * cost_ #Number of sell
        if product_ in total_cost:
            total_cost[product_] += total
        else:
            total_cost[product_] = total
    return total_cost

total_cost_products = cost_product(list_products)
print(f"Total income for each product {total_cost_products}")

list_product = []

for item in total_cost_products:
    print("item", item)
    print("value", total_cost_products[item])
    if total_cost_products[item] > 1000:
        list_product.append(item)

print(f"Products have income more than 1000 {list_product}")
my_dict_products = {'butter': 1, 'milk': 2, 'apple': 7}
def my_func(name_product, quantity):
    if name_product in my_dict_products:
        my_dict_products[name_product] += quantity
    else:
        my_dict_products[name_product] = quantity

my_func("banana", 9)
my_func("butter", 2)
my_func("milk", 2)
my_func('apple', -2)
print(f"Name of products with quantity {my_dict_products}")
# del my_dict_products['banana']
# print(my_dict_products)

my_list_product = []
for item in my_dict_products:
    if my_dict_products[item] < 5:
        my_list_product.append(item)

print(f"Name of products have quantity less than 5 {my_list_product}")

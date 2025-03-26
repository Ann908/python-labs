my_str = "dog cat dog bird cat dog dog cat cat"
my_dictionary = {}
def string_function(my_str):
    words = my_str.split()
    for item in words:
        if item in my_dictionary:
            my_dictionary[item] += 1
        else:
            my_dictionary[item] = 1
    return my_dictionary

dictionary = string_function(my_str)
print(f"Unic words with quantity {dictionary}")

my_list = []
for item in dictionary:
    if dictionary[item] > 3:
        my_list.append(item)
print(f"Unic words have quantity more than 3 {my_list}")

# dictionaries are like hash arrays, key/value pairs
# the key is actually a hashed value
# no duplicate keys
# no guarantee in the order returned

fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "smelly fruit": "horrible smelly fruit"}

# add to dictionary
fruit["pear"] = "an odd shape apple"

# overwrite element
fruit["lime"] = "great with tequila"

# delete a element
del fruit["smelly fruit"]

print(fruit)
print(fruit["lemon"])
print(fruit["lime"])

for key in fruit:
    print("{}: {}".format(key, fruit[key]))

for key, value in fruit.items():
    print("{}: {}".format(key, value))

print("\nOrdered list: ")
for key in sorted(list(fruit.keys())):
    print("\t{}: {}".format(key, fruit[key]))

# get tuples from dictionary, you can also go the other way
f_tuple = tuple(fruit.items())
print(f_tuple)

print("\n---------------------------------------------------------------------")

bike = {"make": "Honda", "model": "250 dream", "color": "red", "engine_size": 250}
print(bike)
print(bike["engine_size"])

print("\n---------------------------------------------------------------------")




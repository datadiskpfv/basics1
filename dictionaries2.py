fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "smelly fruit": "horrible smelly fruit"}

print(fruit)
print("------------------------------------------------")

veg = {"cabbage", "every child's favourite",
       "spouts", "mmmmm, lovely",
       "spinach", "can I have some more fruit, please"}

print(veg)
print("------------------------------------------------")

# combining dictionaries
veg.update(fruit)   # veg is overwritten, nothing is returned
print(veg)
print("------------------------------------------------")

# copy dictionaries
fruit2 = fruit.copy()
print(fruit2)
print("------------------------------------------------")

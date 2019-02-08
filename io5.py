########################################
# Using shelve to read and write files
########################################

# no guarantee of order when retrieving elements

# BE CAREFUL on what you load, bad files can contain shell code to delete all files for example

import shelve

# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "a sweet, orange, citrus fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"

fruit = shelve.open('ShelfTest')
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour, yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])

fruit["lime"] = "great with tequila"

for snack in fruit:
    print(snack + ": " + fruit[snack])
fruit.close()

print("\n")
print(fruit)



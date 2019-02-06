# sets are mutable objects (unless you use a frozen set)
# there is no ordering

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

wild_animals.add("horse")
wild_animals.add("ant")
print(wild_animals)

# you can also use discard
wild_animals.remove("ant")
print(wild_animals)

# to create a empty set, dont use {} this is a dictionary
empty_set = set()
print(empty_set.__class__)

even = set(range(0, 40, 2))
print(even)
print(len(even))

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(squares)
print(len(square_tuple))

print("Union")
print(even.union(squares))
print(even | squares)                   # can also use this instead of above
print(len(even.union(squares)))

print("Intersection")
print(even.intersection(squares))
print(even & squares)                   # can also use this instead of above
print(len(even.intersection(squares)))

print("difference")
print(sorted(even.difference(squares)))
print(sorted(even - squares))           # can also use this instead of above
print(len(even - squares))

print("Symmetric Difference")
print(even.symmetric_difference(squares))
print(even ^ squares)                   # can also use this instead of above
print(len(even.symmetric_difference(squares)))

print("Subsets and supersets")
tuple1 = set([4, 6, 16])
print("tuple1 is a subset of squares {}".format(tuple1.issubset(squares)))          # can use <= as well
print("squares is a superset of tuple1 {}".format(squares.issuperset(tuple1)))      # can use >= as well

frozen_set = frozenset(range(0, 10, 2))
#frozen_set.add          ## add/pop, etc does not exist as its an immutable object


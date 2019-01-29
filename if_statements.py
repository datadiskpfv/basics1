name = input("Please enter your name: ")

# convert string into int using int() function
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# normal >=, <=, !=, ==, and, or can be used
if 18 <= age < 21:      # same as (age >= 18) and (age < 21), dont need brackets but makes it easy to read
    print("You are old enough to vote but not drive a HGV")
elif age >= 21:
    print("You are old enough to vote and drive a HGV")
else:
    print("Please come back in {0} years and then you can vote and drive a HGV".format(18 - age))


# Strings
parrot = "Norwegian Blue"

letter = input("Enter a character")

if letter in parrot:                # could use not in
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")

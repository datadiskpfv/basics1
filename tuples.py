my_tuple = "a", "b", "c"    # you can surround with brackets
print(my_tuple)             # notice the printed brackets

print(("a", "b", "c"))      # notice the printed brackets
print("a", "b", "c")

print("\n---------------------------------------------------------")
welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Ban Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lighting", "Metallica", 1984

print(metallica)
print(metallica[0])

# tuples are immutable, below will throw an error
# metallica[0] = "Master of puppets"
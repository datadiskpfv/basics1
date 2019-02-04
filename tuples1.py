# Use tuple (instead of lists) when you need different types, they are
# are also immutable

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

# bit of cheat to get around the immutable tuple object, by reassigning
imelda = imelda[0], "Imelda", imelda[2]
print(imelda)

print("\n--------------------------------------------------------------------")
# Lists are mutable
metallica2 = ["Ride the Lighting", "Metallica", 1984]
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)

print("\n--------------------------------------------------------------------")
title, artist, year = imelda
print(imelda)
print("Title: {}".format(title))
print("Artist: {}".format(artist))
print("Year: {}".format(year))

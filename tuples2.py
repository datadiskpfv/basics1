# Use tuple (instead of lists) when you need different types, they are
# are also immutable

welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Ban Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011, ([(1, "Pulling the rug"),
                                             (2, "Psycho"),
                                             (3, "Mayhem"),
                                             (4, "Kentish Town Waltz")])

print(imelda)
title, artist, year, tracks = imelda

# because we have a list of tuples we can append
tracks.append((5, "All for You"))

print(title)
print(artist)
print(year)

for track in tracks:
    print("{}. {}".format(track[0], track[1]))
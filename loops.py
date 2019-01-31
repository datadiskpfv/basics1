# will print numbers 1 to 19
for i in range(1, 20):
    print("i is now {}".format(i))

print("------------------------------------------------------------")

# simply loop through all the numbers
number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    print(number[i])

print("------------------------------------------------------------")

# numbers with separators
number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):
    if number[i] in '0123456789':
        # by default \n is added but you can change using end=,
        # it's not remember on next print statement
        print(number[i], end=' ')   

print("\n------------------------------------------------------------")

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

print("\n------------------------------------------------------------")

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)

print("\n------------------------------------------------------------")

for i in range(0, 100, 5):      # step in 5's
    print(i, end=' ')

print("\n------------------------------------------------------------")

for i in range(1, 13):
    for j in range(1, 13):
        print("{} X {} = {}".format(i, j, i*j))
    print("=========================")

my_list = list(range(10))
print(my_list)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))
print(even)
print(odd)

my_string = "abcdefghijklmnopqrstuvwxyz"

print(my_string.index('e'))
print(my_string[4])

small_decimals = range(0, 10)
print(small_decimals)
print(small_decimals[3])

# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by severn".format(x))

print("\n-------------------------------------------------")
print(small_decimals)
my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))

decimals = range(0, 100)
my_decimals_range = decimals[3:40:3]  # start at 3, end at 40, in increments of 3
print(my_decimals_range)

for i in my_decimals_range:
    print(i, end=', ')


print("\n-------------------------------------------------")
r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i, end=', ')
print('\n')

for i in range(99, 0, -2):
    print(i, end=', ')


string = "1234567890"

# for char in string:       # for loop changes to for char in iter(string):
#     print(char)

my_iterator = iter(string)
print(my_iterator)
print(my_iterator.__class__)

print(next(my_iterator))  # get next element in iterator
print(next(my_iterator))

print("\n-------------------------------------------------------")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

my_number_iterator = iter(list1)

for number in range(0, len(list1)):
    print(next(my_number_iterator), end = ', ')

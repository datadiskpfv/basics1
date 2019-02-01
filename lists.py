# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

parrot_list = ["not pinin", "no more", "a stiff", "bereft of life"]
parrot_list.append("Norwegian Blue")
for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers.sort()                          # sort and save to original object
numbers_in_order = sorted(numbers)      # create new sorted object
print(numbers)

numbers_reversed = numbers              # both objects point to same list, use list() to create new object
numbers_reversed.sort(reverse=True)     # can reverse order, there is also reverse() function

# could use numbers_reversed = sorted(numbers, reverse=True)

print(numbers_in_order)
print(numbers_reversed)

if numbers == numbers_in_order:          # checking contents, not if objects are same
    print("numbers equals numbers_in_order")
else:
    print("numbers DOES NOT equals numbers_in_order")

print("\n------------------------------------------------------------------")

# the below are the same, create an empty list
list_1 = []
list_2 = list()

print(list_1.__class__)
print(list_2.__class__)

list_3 = list("This should be broken into separate elements")
print(list_3)

print("\n------------------------------------------------------------------")
even_1 = [0, 2, 4, 6, 8]
odd_1 = [1, 3, 5, 7, 9]

list_within_list = [even_1, odd_1]
print(list_within_list)

print("\n------------------------------------------------------------------")
menu = list()
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

print(menu)

for meal in menu:
    if not "spam" in meal:
        for item in meal:
          print(item, end=', ')

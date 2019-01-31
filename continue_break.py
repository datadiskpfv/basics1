shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

for item in shopping_list:
    print("Buy " + item + ', ', end=' ')

print("\n------------------------------------------------------------------------------")

for item in shopping_list:
    if item == 'spam':
        continue

    print("Buy " + item + ', ', end=' ')

print("\n------------------------------------------------------------------------------")

for item in shopping_list:
    if item == 'spam':
        break

    print("Buy " + item + ', ', end=' ')

print("\n------------------------------------------------------------")

for i in range(0, 6):
    print(i)
else:
    print("Inside for else statement")

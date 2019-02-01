for i in range(10):
    print("{}".format(i), end=', ')

print("\n-------------------------------------------------------------")
i = 0
while i < 10:
    print("{}".format(i), end=', ')
    i += 1

print("\n-------------------------------------------------------------")
available_exits = ['east', 'north east', 'south']

chosen_exit = ''
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == 'quit':
        print("Game Over!")
        break
else:
    print("aren't you glad you got out of there!")

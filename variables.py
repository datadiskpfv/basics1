greeting = "Paul"
_myName = "Paul"
Paul99 = "Good"
Paul_was_here = "Good"
Greeting = "Hello"

print(Greeting + ' ' + greeting)

## below will cause an error int and String mix
# age = 24
# print(age)
# print(greeting + age)

a = 12
b = 3
c = 12.45

print(a.__class__)
print(b.__class__)
print(c.__class__)
print(greeting.__class__)

print(a + b)
print(a - b)
print(a * b)
print(a / b)    # divide returns a float
print(a // b)   # double slash means divide but return a int
print(a % b)

print(a + b / 3 - 4 * 12)
print((((a + b) / 3) - 4) * 12)     # correct answer = 12

parrot = "Norwegian Blue"
print(parrot[3])                    # start at zero
print(parrot[-1])                   # start at end of string

print(parrot[0:6])                  # get a range, don't include 6
print(parrot[:6])                   # start at beginning to 6
print(parrot[6:])                   # start at 6 until end
print(parrot[0:6:2])                # start at 0 up to 6 skip 2
print("1, 2, 3, 4, 5, 6, 7"[0::3])  # print just the numbers

string1 = "he's "
string2 = "probably"
print(string1 + string2)
print("hello " * 5)

today = "Friday"
print("day" in today)               # returns boolean
print("parrot" in today)            # returns boolean


# for very long strings pycharm may flag this
input_prompt1 = "this is a very long sentence to be used in a user prompt and will probably be flagged by Pycharm, so we can use two different method as below"

# use a slash to split a line
input_prompt2 = "this is a very long sentence to be used in a user prompt and" \
                "will probably be flagged by Pycharm, so we can use two different method as below"

# the preferred way is to use brackets
input_prompt3 = ("this is a very long sentence to be used in a user prompt and"
                 "will probably be flagged by Pycharm, so we can use two different method as below")

a = b = c = d = 12
print(c)
print(b)

e, f = 13, 14
print(e)
print(f)

x = 99
y = 100
x, y = y, x     # switch values in x and y
print("x is {}".format(x))
print("y is {}".format(y))




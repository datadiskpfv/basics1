def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(width, text):
    text = str(text)        # make sure parameter is a str
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# there are better ways to handle multiple arguments
def multi_arg(*args, end=', '):      # end has a default of ', '
    for i in args:
        print(str(i), end=end)


# return data
def return_data(text):
    return "Returned Data: " + text

# call function
python_food()
center_text(80, "spam and eggs")
center_text(80, 12)

# multi-argument
multi_arg("first", "second", 3, 4, "five")
print()
multi_arg("first", "second", 3, 4, "five", end=': ')

# returning data
print("\n" + return_data("Hello World!"))
r1 = return_data("Some returned text")
print(r1)


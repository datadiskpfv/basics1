def average(*args):
    print(type(args))
    print("args is {}".format(args))
    print("*args is", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


# return a tuple
def build_tuple(*args):
    print(type(args))
    return args


print(average(1, 2, 3, 4))

print(build_tuple(1,2,3,4))

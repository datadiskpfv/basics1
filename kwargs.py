# * unpacks a tuple
# ** unpacks a dictionary


# def print_backwards(*args, end=' ', **kwargs):
def print_backwards(*args, **kwargs):
    print(type(kwargs))
    print(kwargs)
    # if we need to break a specific dictionary, in this case end
    end = kwargs.pop('end', ' ')
    for word in args[::-1]:
        print(word[::-1], end=end, **kwargs)


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "world", "take", "me", "to", "your", "leader", sep=':', file=backwards)
    print_backwards("hello", "world", "take", "me", "to", "your", "leader", end='\n', sep=':')

backwards_print("hello", "world", "take", "me", "to", "your", "leader")

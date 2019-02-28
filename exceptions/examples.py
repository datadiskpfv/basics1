import sys


def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    number = input("Enter a number:")
    print(factorial(int(number)))
except EOFError as error:
    print("Ctrl-D was caught, program terminated!")
    sys.exit(9)
except (RecursionError, OverflowError):
    # perform any tidy up or retry operation
    print("This program cannot calculate factorials that large")
except (NameError, TypeError, ValueError):
    print("Please enter a number not a character")
except Exception:
    print("Base class for all exceptions, catch all but should use specific exception")
else:
    print("Program executed correctly, else wont be called if program terminates")
finally:
    print("finally will always execute, good for tidying up!")

print("Back to main program - Program terminating")

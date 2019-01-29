age = 24
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))

city = "Milton Keynes"
print("My age is {0} years and lives in {1}".format(age, city))

# Old way and no longer used depreciated - Python 2
print("My age is %d years and lives in %s" % (age, city))

for i in range(1, 12):
    print("No, %2d squared is %d and cubed is %d" % (i, i ** 2, i ** 3))

print("PI is approx %12f" % (22 / 7))
print("PI is approx %12.50f" % (22 / 7))

# the new way and should use going forward
for i in range(1, 12):
    print("No, {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("PI is approx {0:12}".format(22 / 7))
print("PI is approx {0:12.50}".format(22 / 7))

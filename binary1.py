print("Binary")
print("--------------------------------------------")
for i in range(17):
    # first column is width of 2 align to right
    # second column is width of 8 align to right and pack front with zero's
    print("{0:>2} in binary is {0:>08b}".format(i))

print("0b1111 should be {}".format(0b1111))
print("0b1001 should be {}".format(0b1011))

print("\nHex")
print("--------------------------------------------")
for i in range(17):
    print("{0:>2} in hex is {0:0x}".format(i))

print("0x20 should be {}".format(0x20))
print("0x0a should be {}".format(0x0a))

print("\nOctal")
print("--------------------------------------------")
for i in range(17):
    print("{0:>2} in hex is {0:0o}".format(i))

print("0o20 should be {}".format(0o20))
print("0o07 should be {}".format(0o7))
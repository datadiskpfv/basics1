########################################
# Reading files
########################################

# can use full path
# jabber = open("C:\\python_projects\\basics1\\sample.txt", 'r')

print("using open to read the file")
jabber1 = open("sample.txt", 'r')
for line1 in jabber1:
    if "jabberwock" in line1.lower():
        print(line1, end='')

jabber1.close()

print("\nusing with to read the file")
with open("sample.txt", 'r') as jabber2:     # automatically closes the file
    for line2 in jabber2:
        if "jabberwock" in line2.lower():
            print(line2, end='')


print("\nusing with to read the file and readline method")
with open("sample.txt", 'r') as jabber3:     # automatically closes the file
    line3 = jabber3.readline()
    while line3:
        if "jabberwock" in line3.lower():
            print(line3, end='')
        line3 = jabber3.readline()

print("\nread the whole file in one go, it will contained in a list")
with open("sample.txt", 'r') as jabber4:     # automatically closes the file
    line4 = jabber4.readlines()
print(line4)

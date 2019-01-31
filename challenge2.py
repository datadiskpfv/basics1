ip_address = input("Enter an ip address: ")

if ip_address[-1] != '.':
    ip_address += '.'

segment = 1
segment_length = 0

for char in ip_address:
    if char == '.':
        print("segment {} contains {} character".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

# if char != '.':
#     print("segment {} contains {} character".format(segment, segment_length))

buffer = [4, 8, 73, 7, 954, 1, 73, 0, 8, 73, 2, 73, 121, 83]

while 73 in buffer:
    buffer.remove(73)

buffer.sort(reverse=True)

print(buffer)
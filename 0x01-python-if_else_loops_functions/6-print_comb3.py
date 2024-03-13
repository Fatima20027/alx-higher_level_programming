#!/usr/bin/python3
for j in range(0, 9):
    for i in range(1, 10):
        if j == 8 and i == 9:
            end = "\n"
        else:
            end = ", "
        if j < i:
            print("{j}{i}".format(j=j, i=i), end=end)


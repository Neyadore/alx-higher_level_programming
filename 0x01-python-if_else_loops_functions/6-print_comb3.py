#!/usr/bin/python3
for a in range(0, 8):
    b = a + 1
    for b in range(b, 10):
        print("{:d}{:d}".format(a, b), end=", ")
print("89")

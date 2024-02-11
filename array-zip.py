#!/usr/bin/python3

a = [1, 2, 3]
b = ["one", "two", "three"]

for val1, val2 in zip(a, b):
    print (val1, val2)
    # use zip function since call in a,b is error prone.
#!/usr/bin/env python

import random

s = "hi"
print(s)
print(s + " planet" + " " + str(len(s)))

raw = "\nThis!\n\tThat!"
print(raw)
multi_line = """Whis?
        What?"""
print(multi_line)
print(multi_line.upper())
print(multi_line.lower())
print(multi_line.isalpha())
print(multi_line.replace("W", "C"))
split_line = multi_line.split(" ")
print(split_line)

print("\nFOR loop test:")
for i in range(10):
    print(i)

print("\nWHILE loop test:")
j=0
while j in range(100):
    if(j % 5 == 0):
        print("%i is divisible by 5!" % (j))
    else:
        print(j)
    j = j + 3

print("\nList:")
test_list = []
k = 1
while k in range(1,53):
    test_list.append(k)
    k += 1
print(test_list)
test_list.reverse()
print(test_list)
random.shuffle(test_list)
print(test_list)
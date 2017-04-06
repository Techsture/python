#!/usr/bin/env python

# Print out the 1 through 25.
# If the number is divisible by 3, print FIZZ
# If the number is divisible by 5, print BUZZ
# If the number is divisible by both 3 and 5, print FIZZBUZZ

for i in range(1, 26):
    if(((i %3) == 0) and ((i % 5) == 0)):
        print("FIZZBUZZ")
    elif((i % 3) == 0):
        print("FIZZ")
    elif((i % 5) == 0):
        print("BUZZ")
    else:
        print i

#!/usr/bin/env python3

# PROBLEM:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    list_of_multiples = []
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            list_of_multiples.append(i)
    print(sum(list_of_multiples))

if __name__ == '__main__':
    main()

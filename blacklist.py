#!/usr/local/bin/python

# Generate a random number in a range, but don't return a number in the blacklist.

import random

def main():
    blacklist = [2, 4, 6, 8, 9, 10]
    for i in range(1,101):
        number = 0
        while number == 0:
            number = random.randint(1, 10)
            if number in blacklist:
                number = 0
            else:
                print("%i: %i" % (i, number))


if __name__ == "__main__":
    main()
#!/usr/bin/env python

# Given a list of numbers:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    print("The list is: %s" % a)
    num = int(raw_input("Give me a number: "))
    for i in a:
        if(i < num):
            b.append(i)
    print("The new list is: %s" % b)

if __name__ == '__main__':
    main()

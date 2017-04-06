#!/usr/bin/env python

# Given list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
# Write one line of Python that makes a new list that has only the even elements of this list in it.

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [i for i in a if i % 2 == 0]
    print("Original list: %s" % a)
    print("Even numbers: %s" % b)

if __name__ == "__main__":
    main()
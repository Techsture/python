#!/usr/bin/env python

# Script to recursively add together all off the integers up to and including the integer passed in.

import argparse


def recursive_add(integer):
    if integer == 0:
        return 0
    return integer + recursive_add(integer - 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("integer", help="interger", type=int)
    args = parser.parse_args()
    if args.integer > 997:
        print("Number is too large!")
        exit()
    elif args.integer < 1:
	print("Number is too small!")
	exit()
    else:
        print(recursive_add(args.integer))


if __name__ == '__main__':
    main()
    

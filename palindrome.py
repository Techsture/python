#!/usr/local/bin/python

# Test if a given string is a palindrome.

import argparse

def main():
    # Parse the argument:
    parser = argparse.ArgumentParser()
    parser.add_argument("parameter", help="string to test", type=str)
    args = parser.parse_args()
    # Actual program starts here:
    parsed_string = args.parameter.lower()
    if parsed_string == parsed_string[::-1]:
        print("%s is a palindrome!" % args.parameter)
    else:
        print("%s is not a palindrome." % args.parameter)


if __name__ == "__main__":
    main()

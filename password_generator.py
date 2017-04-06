#!/usr/bin/env python

# Generate a password containing a mixture of uppercase, lowercase, numbers, and symbols ( !@#$%^&*() )

import argparse
import random
import string

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("length", help="length", type=int)
    args = parser.parse_args()
    possible_chars = string.letters + string.digits + string.punctuation
    password = ""
    i = 0
    while i < args.length:
        character = str(random.choice(possible_chars)) 
        password += character
        i += 1
    print(password)

if __name__ == "__main__":
    main()
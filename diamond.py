#!/usr/bin/env python

# This has been stolen from Maninder Pal Singh, with a couple edits.  Original here:
#   http://gamesandapps.blogspot.com/2012/12/python-program-to-generate-diamond.html

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help="size of diamond", type=int)
    args = parser.parse_args()
    j = args.size
    k = args.size
    p = 1
    for i in range(args.size + 1):
        # This 'if' just skips printing the blank line at the beginning.
        if i == 0:
            k -= 1
            continue
        print " " * k," *" *  i
        k -= 1
    while j > 1:
        j -= 1
        print " " * p," *" * j
        p += 1


if __name__ == "__main__":
    main()

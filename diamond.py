#!/usr/bin/env python

# This has been stolen from Maninder Pal Singh, with a couple edits.  Original here:
#   http://gamesandapps.blogspot.com/2012/12/python-program-to-generate-diamond.html

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help="size of diamond", type=int)
    args = parser.parse_args()
    top_half = args.size
    bottom_half = args.size
    spaces = 1
    for points in range(args.size + 1):
        # This 'if' just skips printing the blank line at the beginning.
        if points == 0:
            top_half -= 1
            continue
        print " " * top_half," ." *  points
        top_half -= 1
    while bottom_half > 1:
        bottom_half -= 1
        print " " * spaces," ." * bottom_half
        spaces += 1


if __name__ == "__main__":
    main()

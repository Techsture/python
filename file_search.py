#!/usr/bin/env python

# Takes two arguments: <directory> <search_term>
# First, check that <directory> exists on the machine
# Then, match <search_term> to any files in <directory> and print them on-screen or to a file

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description="search a directory for files")
    parser.add_argument("path", help="directory you'd like to search")
    parser.add_argument("search_term", help="term you'd like to search for in filenames")
    args = parser.parse_args()
    # Shove the contents of os.listdir() into a variable so we can work with the results
    contents = os.listdir(args.path)
    print("Here's the matches for \"%s\" in \"%s\":" % (args.search_term, args.path))
    for file in contents:
        if(args.search_term.lower() in file.lower()):
            print file

if __name__ == "__main__":
    main()

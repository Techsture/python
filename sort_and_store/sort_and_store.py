#!/usr/bin/env python

# Given a text file passed via command line (numbers_unsorted.txt):
# 1.) Read the file
# 2.) Sort the contents
# 3.) Output to a new text file (numbers_sorted.txt)

import argparse

def read_file(filename):
    # Read the file
    in_file = open(filename, 'r')
    # Read each line into an list, dropping the \n and mapping all items in the list from str to int
    lines = map(int, in_file.read().splitlines())
    # Close in_file
    in_file.close()
    return lines

def sort_contents(lines):
    # Sort the list and store it in sorted_list
    sorted_list = sorted(lines)
    return sorted_list

def write_file(sorted_list):
    # Open out_file for writing
    out_file = open('numbers_sorted.txt', 'w')
    # Write each line with a \n at the end
    for line in sorted_list:
        out_file.write("%s\n" % line)
    # Close out_file
    out_file.close()
    return


def main():
    # Read the filename passed via argument
    parser = argparse.ArgumentParser(description="read a file, sort each line, and output a new file")
    parser.add_argument("filename", help="name of file you'd like to sort")
    args = parser.parse_args()
    lines = read_file(args.filename)
    sorted_list = sort_contents(lines)
    write_file(sorted_list)
    exit()


if __name__ == "__main__":
    main()

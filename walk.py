#!/usr/bin/env python

import argparse
import os

def main():
    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="path you'd like to walk", type=str)
    parser.add_argument("search_term", help="what you're looking for", type=str)
    args = parser.parse_args()
    # Walk the path
    for root, dirs, files in os.walk(args.file_path):
        for name in files:
            if args.search_term.lower() in name.lower():
                print(os.path.join(root, name))


if __name__ == "__main__":
    main()
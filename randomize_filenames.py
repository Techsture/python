#!/usr/bin/env python3

# This file renames all the files in a directory while preserving the file extension.

import argparse
import os
import random


def generate_filename():
    counter = 0
    filename_length = 8
    acceptable_characters = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    randomized_filename = ''
    while counter < filename_length:
        randomized_filename = randomized_filename + random.choice(acceptable_characters)
        counter += 1
    return randomized_filename


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='System path to directory containing files.')
    args = parser.parse_args()
    directory = args.directory
    for (dirpath, dirnames, filenames) in os.walk(directory):
        for filename in filenames:
            if filename == '.DS_Store':
                print(f"Deleting {filename}")
                os.remove(f'{directory}/.DS_Store')
                continue
            else:
                file_extension = os.path.splitext(filename)[1]
                randomized_filename = generate_filename()
                print(f"Renaming {filename} to {randomized_filename}{file_extension}")
                os.rename(f'{directory}/{filename}', f'{directory}/{randomized_filename}{file_extension}')
    exit()


if __name__ == '__main__':
    main()

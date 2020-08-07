#!/usr/bin/env python3

# Divide the contents of a directory randomly into an arbitrary number of subdirectories.

import argparse
import os
import random


def get_file_list(directory):
    file_list = []
    for file in os.listdir(directory):
        file_list.append(file)  
    return file_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('number_of_subdirectories', help='The number of directories to divide into.', type=int)
    parser.add_argument('directory', help='System path to directory containing files.  Be sure to include the trialing slash!')
    args = parser.parse_args()
    number_of_subdirectories = args.number_of_subdirectories
    directory = args.directory
    file_list = get_file_list(directory)
    random.shuffle(file_list)
    for i in range(0, number_of_subdirectories):
        os.mkdir(directory + f'{i}')
    for i in range(0, len(file_list)):
        subdirectory_name = i % number_of_subdirectories
        os.rename(f'{directory}/{file_list[i]}', f'{directory}/{subdirectory_name}/{file_list[i]}')
    exit()


if __name__ == '__main__':
    main()

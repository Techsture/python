#!/usr/bin/env python3

import argparse
import os
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='System path to directory containing files.')
    args = parser.parse_args()
    directory = args.directory
    for (dirpath, dirname, filenames) in os.walk(directory):
        for filename in filenames:
            if dirpath[-1].isdigit():
                #print(f'{dirpath}/{filename}', f'/Volumes/Music/Sound Library (Sync\'d)/Disting Samples/{filename}')
                shutil.move(f'{dirpath}/{filename}', f'/Volumes/Music/Sound Library (Sync\'d)/Disting Samples/{filename}')
    exit()


if __name__ == '__main__':
    main()

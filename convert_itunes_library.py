#!/usr/bin/env python3

# To use this, delete the initial dict at the top of the XML file, as
# well as the arrays at the bottom for the playlist information.

import argparse
import json
from pathlib import Path
import plistlib
from operator import itemgetter
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=Path, help='File Path')
    args = parser.parse_args()
    file_path = args.file_path
    with file_path.open(mode='rb') as library_file:
        library = []
        plist = plistlib.load(library_file)
        for _, value in plist.items():
            library.append(value)
        track_list = []
        for track in library:
            try:
                track_list.append([track['Name'], track['Artist'], track['Album'], track['Genre']])
            except:
                track_list.append([track['Name'], track['Artist'], "none", track['Genre']])
    print(tabulate(sorted(track_list, key=itemgetter(1)), headers=['Track Name', 'Artist', 'Album', 'Genre']))
    exit()


if __name__ == '__main__':
    main()

#!/usr/bin/env python

# This script will parse Hold'Em log files in the format:
# nnn: P1: Rs,Rs | P2: Rs,Rs | P3: Rs,Rs | P4: Rs,Rs | P5: Rs,Rs | CC: Rs,Rs,Rs,Rs,Rs
#
# 'nnn' is the log line, 'R' is the rank of a card, and 's' is the suit of the card.
#
# It assumes that the log files are in the ./logs folder.


import os
import re


def get_list_of_logs():
    list_of_logs = []
    contents = os.listdir('./logs')
    for file in contents:
        list_of_logs.append(file)
    return list_of_logs


def main():
    list_of_logs = get_list_of_logs()
    


if __name__ == '__main__':
    main()

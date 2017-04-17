#!/usr/bin/env python

# This script will parse Hold'Em log files in the format:
# nnn: P1: Rs,Rs | P2: Rs,Rs | P3: Rs,Rs | P4: Rs,Rs | P5: Rs,Rs | CC: Rs,Rs,Rs,Rs,Rs
#
# 'nnn' is the log line, 'R' is the rank of a card, and 's' is the suit of the card.
#
# It assumes that the log files are in the ./logs folder.


import os
import re


def find_pocket_pairs(list_of_logs):
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8" ,"9", "T", "J", "Q", "K"]
    counter_hands = 0
    counter_matched = 0
    for file in list_of_logs:
        filename = './logs/' + file
        opened_file = open(filename, "r")
        #print("Found pocket pairs on these lines in file " + file + ":")
        for line in opened_file.readlines():
            counter_hands += 1
            for rank in ranks:
                pattern = re.compile("\s%s\w,%s\w\s" % (rank, rank))
                if pattern.findall(line):
                    #print(line.strip("\n "))
                    counter_matched += 1
    percentage = int((float(counter_matched) / float(counter_hands * 5)) * 100)
    print("%s pocket pairs found in %s total player hands (%s%%)." % (counter_matched, counter_hands * 5, percentage))


def find_suited_hole_cards(list_of_logs):
    suits = ["c", "d", "h", "s"]
    counter_hands = 0
    counter_matched = 0
    for file in list_of_logs:
        filename = './logs/' + file
        opened_file = open(filename, "r")
        #print("Found suited hole cards on these lines in file " + file + ":")
        for line in opened_file.readlines():
            counter_hands += 1
            for suit in suits:
                pattern = re.compile("\s\w%s,\w%s\s" % (suit, suit))
                if pattern.findall(line):
                    #print(line.strip("\n "))
                    counter_matched += 1
    percentage = int((float(counter_matched) / float(counter_hands * 5)) * 100)
    print("%s suited hole cards found in %s total player hands (%s%%)." % (counter_matched, counter_hands * 5, percentage))    


def get_list_of_logs():
    list_of_logs = []
    contents = os.listdir('./logs')
    for file in contents:
        list_of_logs.append(file)
    return list_of_logs


def main():
    list_of_logs = get_list_of_logs()
    find_pocket_pairs(list_of_logs)
    find_suited_hole_cards(list_of_logs)


if __name__ == '__main__':
    main()

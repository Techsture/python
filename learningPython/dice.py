#!/usr/bin/env python3

from random import randint


def roll():
    die_roll = randint(1, 6)
    print(die_roll)
    return die_roll


def main():
    success = False
    counter = 0
    while success is False:
        counter += 1
        print("\n")
        if roll() == 1:
            if roll() == 2:
                if roll() == 3:
                    if roll() == 4:
                        if roll() == 5:
                            if roll() == 6:
                                success = True
    print("Success!  It took {0} tries.".format(counter))
    exit()


if __name__ == '__main__':
    main()

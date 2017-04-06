#!/usr/bin/env python

from random import randint
import sys

# Choose a type of die (d2, d4, d6, d8, d10, d12, d20, d100).
# Roll That Die.
# Print the result.

def choose_die():
    valid_die = False
    while valid_die is False:
        die_choice = raw_input()
        if die_choice in [ "d2", "d4", "d6", "d8", "d10", "d12", "d20", "d100" ]:
            valid_die = True
        else:
            print("Invalid die choice!  Try again...\n")
    return die_choice

def print_result_with_proper_grammar(roll_result):
    begin_with_eight_test = str(roll_result)[:1]
    if begin_with_eight_test is not "8":
        print("You rolled a %d." % (roll_result))
    else:
        print("You rolled an %d." % (roll_result))
    return

def get_number_of_sides(die_choice):
    number_of_sides = int(die_choice.lstrip('d'))
    return number_of_sides

def roll(number_of_sides):
    roll_result = randint(1, number_of_sides)
    return roll_result


def main(argv):
    print("\n*** Dungeon Dice ***")
    print("Choose a die: ")
    print("d2 (Coin)")
    print("d4")
    print("d6")
    print("d8")
    print("d10")
    print("d12")
    print("d20")
    print("d100\n")
    die_choice = choose_die()
    number_of_sides = get_number_of_sides(die_choice)
    # print("\nYou chose a %s, which has %d sides." % (die_choice, number_of_sides))
    print("\nRolling!")
    roll_result = roll(number_of_sides)
    print_result_with_proper_grammar(roll_result)
    exit()


if __name__ == "__main__":
    main(sys.argv)

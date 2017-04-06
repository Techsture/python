#!/usr/bin/env python

from random import randint
import sys

# Ask the user to pick a number between 1 and 10 (inclusive).
# Generate a number.
# Compare them and say whether the guess was right or not.

def generate_number():
	number = randint(1, 2)
	return number

def get_guess():
	valid_choice = False
	while valid_choice is False:
		guess = raw_input()
		if(guess in [ "1", "2" ]):
			valid_choice = True
		else:
			print("That is not a valid choice!  Please pick 1 for heads or 2 for tails.\n")
	return guess

def compare_numbers(guess, number):
	if(guess == number):
		result = True
	else:
		result = False
	return result

def convert_number_to_name(number):
	if(number is 1):
		side_name = "Heads"
	else:
		side_name = "Tails"
	return side_name


def main(argv):
	print("\nHeads or tails?")
	print("1.) Heads")
	print("2.) Tails\n")
	guess = int(get_guess())
	number = generate_number()
	side_name = convert_number_to_name(number)
	if(compare_numbers(guess, number) is True):
		print("%s! You win!" % (side_name))
	else:
		print("%s... you lose." % (side_name))
	exit()


if __name__ == '__main__':
	main(sys.argv)

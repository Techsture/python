#!/usr/bin/env python3

from random import randint


def create_list():
	items = []
	for i in range(42):
		items.append(randint(0, 999))
	return items


def main():
	# Create a list of random numbers between 0 and 999 of 42 elements.
	items = create_list()
	# Print the initial list
	print("\nBefore Sort:")
	print(items)
	# Sort the list

	# Print the list
	print("\nAfter Sort:")
	print(items)


if __name__ == '__main__':
	main()

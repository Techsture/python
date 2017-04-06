#!/usr/bin/env python3

from random import randint


def create_list():
	items = []
	for i in range(42):
		items.append(randint(0, 999))
	return items


def quicksort(items):
	less_than = []
	pivot_list = []
	greater_than = []
	if len(items) <= 1:
		return items
	else:
		pivot = items[0]
		for i in items:
			if i < pivot:
				less_than.append(i)
			elif i > pivot:
				greater_than.append(i)
			else:
				pivot_list.append(i)
		less_than = quicksort(less_than)
		greater_than = quicksort(greater_than)
		return less_than + pivot_list + greater_than


def main():
	# Create a list of random numbers between 0 and 999 of 42 elements.
	items = create_list()
	# Print the initial list
	print("\nBefore Sort:")
	print(items)
	# Sort the list
	items = quicksort(items)
	# Print the list
	print("\nAfter Sort:")
	print(items)


if __name__ == '__main__':
	main()

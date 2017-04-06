#!/usr/bin/env python3

from random import randint


def create_list():
	items = []
	for i in range(42):
		items.append(randint(0, 999))
	return items


def merge(left, right):
	result = []
	left_index = 0
	right_index = 0
	while left_index < len(left) and right_index < len(right):
		if left[left_index] <= right[right_index]:
			result.append(left[left_index])
			left_index += 1
		else:
			result.append(right[right_index])
			right_index += 1
	if left:
		result.extend(left[left_index:])
	if right:
		result.extend(right[right_index:])
	return result


def mergesort(items):
	if len(items) <= 1:
		return items
	else:
		middle = len(items) // 2
		left = items[:middle]
		right = items[middle:]
		left = mergesort(left)
		right = mergesort(right)
	return merge(left, right)


def main():
	# Create a list of random numbers between 0 and 999 of 42 elements.
	items = create_list()
	# Print the initial list
	print("\nBefore Sort:")
	print(items)
	# Sort the list
	items = mergesort(items)
	# Print the list
	print("\nAfter Sort:")
	print(items)


if __name__ == '__main__':
	main()

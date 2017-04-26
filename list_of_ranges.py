#!/usr/local/bin/python

# Given two lists, combine them so that the ranges expand when necessary.
# list_a = [0, 2-5, 7, 9, 12]
# list_b = [1, 2, 8, 10]
# combined_list = [0-5, 7-10, 12]

import re

def main():
    list_a = [0, '2-5', 7, 9, 12]
    list_b = [1, 2, 8, 10]
    combined_list = []
    list_of_ranges = []
    final_list = []
    found_range = []
    pattern = re.compile(r'-')
    print("List A: %s" % list_a)
    print("List B: %s" % list_b)
    for i in list_a:
        if re.search(pattern, str(i)):
            num_range = i.split('-')
            for j in range(int(num_range[0]), int(num_range[1])+1):
                combined_list.append(j)
        else:
            combined_list.append(i)
    for i in list_b:
        combined_list.append(i)
    for i in sorted(combined_list):
        if not list_of_ranges:
            list_of_ranges.append(i)
        elif i in list_of_ranges:
            continue
        elif i+1 in combined_list:
            list_of_ranges.append(i)
        else:
            found_range = str(list_of_ranges[0]) + '-' + str(i)
            final_list.append(found_range)
            list_of_ranges = []
    if len(list_of_ranges) <=1:
        final_list.append(str(list_of_ranges[0]))
            
    print("Final List: %s" % sorted(final_list))


if __name__ == '__main__':
    main()

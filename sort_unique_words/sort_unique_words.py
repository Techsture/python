#!/usr/local/bin/python

# Given a file, sort all the words in that file.
# Print out all the words in a list.
# If a word already exists in the list, don't add it again.

# Need to import 'string' so punctuation can be stripped easily
import string


def main():
    # Open the file
    in_file = open("gibberish.txt", 'r')
    # Split the file on whitespace so that you get a list of words
    word_list = in_file.read().split()
    unique_list = []
    for item in word_list:
        # Convert each item to lowercase and strip off the punctuation
        lowercase_item = item.lower().translate(None, string.punctuation)
        # If the item isn't in the list, add it
        if lowercase_item not in unique_list:
            unique_list.append(lowercase_item)
    # Sort the list and print it
    unique_list.sort()
    print(unique_list)


if __name__ == "__main__":
    main()

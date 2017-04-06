#!/usr/bin/env python

word = "Reverse"
print(word)
# First, reverse the entire word with slices
print(word[::-1])
# Now try putting each character of the word into a list
character_word = list(word)
print(character_word)
# Use slices to interate through the list backwards
for character in (character_word[::-1]):
    print(character)
# Use the reverse function on the entire list
character_word.reverse()
print(character_word)
# Sort the list
character_word.sort()
print(character_word)
# Convert the characters to lowercase using a list comprehension and sort the result
characters_lowercase = [ character.lower() for character in character_word ]
characters_lowercase.sort()
print(characters_lowercase)
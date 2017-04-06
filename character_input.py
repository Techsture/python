#!/usr/bin/env python

# Ask the user their name (name)
# Ask the user their age (age)
# Ask the user for a number (counter)
# Print out a message addressed to them that tells them the 
#  year they'll turn 100 the number of times specified by
#  counter on separate lines.

import datetime

def main():
    name = raw_input("What is your name? ")
    age = raw_input("What is your age? ")
    counter = int(raw_input("What's your favorite number? "))
    # print("%s %s %s" % (name, age, counter))

    current_year = datetime.datetime.now().year
    # print("%s" % current_year)
    hundredth_year = int(current_year) + (100 - int(age))

    for i in range(0, counter):
        print("%s: Hi %s!  In the year %s you will be 100 years old.\n" % (i+1, name, str(hundredth_year)))

if __name__ == '__main__':
    main()

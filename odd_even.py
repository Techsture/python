#!/usr/bin/env python

# Ask the user for a number (num) 
# Depending on whether the number is even or odd, print out an appropriate message to the user
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (numerator) and one number to divide by (denominator).
#   Tell the user if numerator is divisible by denominator or not.

def main():
    num = int(raw_input("Give me a number: "))

    if(num % 2 == 0):
        print("%s is an even number." % num)
    else:
        print("%s is an odd number." % num)
    if(num % 4 == 0):
        print("%s is divisible by 4." % num)
    else:
        print("%s is not divisible by 4." % num)

    numerator = int(raw_input("Give me a number to be divided: "))
    denominator = int(raw_input("Give me a number to divide by: "))

    if(numerator % denominator == 0):
        print("%s is divisible by %s." % (numerator, denominator))
    else:
        print("%s is not divisible by %s." % (numerator, denominator))

if __name__ == '__main__':
    main()
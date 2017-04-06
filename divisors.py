#!/usr/bin/env python

# Given a number, print all divisors of that number.

def main():
    num = int(raw_input("Give me a number: "))
    divisors = []
    for i in range(1, (num + 1)):
        if(num % i == 0):
            divisors.append(i)
    print("Here are the divisors of %s: " % num)
    print(divisors)

if __name__ == "__main__":
    main()
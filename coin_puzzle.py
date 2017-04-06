#!/usr/bin/env python

# 100 coins are on a table.  
#   90 are showing tails.
#   10 are showing heads.
# Separate the coins into two piles so that the same number of coins are heads up in each pile.

import random

def main():
    # Generate the coins.
    pile_a = []
    pile_b = []
    for i in range(100):
        pile_a.append(0)
    # Flip 10 of them face up.
    for i in range(10):
        pile_a[i] = 1;
    # Scatter tham around the table
    random.shuffle(pile_a)
    # Take the first 10 coins and the last 90 coins and put them into separate piles
    for i in range(10):
        pile_b.append(pile_a[i])
        pile_a.remove(pile_a[i])
    # Flip all the coins in the smaller pile over
    pile_b = [0 if coin == 1 else 1 for coin in pile_b]
    # Count the number of heads up coins in each pile:
    count_a = 0
    count_b = 0
    for coin in pile_a:
        if coin is 1:
            count_a += 1
    for coin in pile_b:
        if coin is 1:
            count_b += 1
    print("Coin pile A = %s" % pile_a)
    print("Coin pile A has %s heads up coins in it." % count_a)
    print("Coin pile B = %s" % pile_b)
    print("Coin pile B has %s heads up coins in it." % count_b)
    if(count_a == count_b):
        print("Number of heads up coins matches!")
    else:
        print("Number of heads up coins is different... something went wrong!")


if __name__ == "__main__":
    main()
    
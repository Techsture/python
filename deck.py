#!/usr/bin/env python

import random


def create_deck():
    deck = []
    for i in range(4):
        if i == 0:
            suit = "s"
        elif i == 1:
            suit = "h"
        elif i == 2:
            suit = "d"
        else:
            suit = "c"
        for j in range(1,14):
            if j == 1:
                card = "A" + suit
            elif j == 11:
                card = "J" + suit
            elif j == 12:
                card = "Q" + suit
            elif j == 13:
                card = "K" + suit
            else:
                card = str(j) + suit
            deck.append(card)
    return deck


def main():
    # Create deck of cards
    deck = create_deck()
    # Shuffle deck of cards
    random.shuffle(deck)
    # Deal two cards to each player
    player_one = []
    player_two = []
    for position in range(2):
        player_one.append(deck.pop())
        player_two.append(deck.pop())
    # Print out the hands
    print("Player one has:")
    print(player_one)
    print("Player two has:")
    print(player_two)


if __name__ == "__main__":
    main()

#!/usr/bin/env python

import random
import time


def add_cards(hand):
    accumulator = 0
    card = 0
    while card < len(hand):
        value = 0
        rank = hand[card][:1]
        if rank is 'A':
            value += 1
        elif rank is 'J' or rank is 'Q' or rank is 'K' or rank is 'T':
            value += 10
        elif rank is 'X':
            value += 0
        else:
            value += int(rank)
        card += 1
        accumulator += value
    return accumulator

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
            elif j == 10:
                card = "T" + suit
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

def test_bust(player_hand, player_name):
    print("\n")
    print(player_hand)
    print("%s has %i" % (player_name, add_cards(player_hand)))
    bust = False
    if add_cards(player_hand) > 21:
        bust = True
    return bust

def who_wins(player, dealer):
    # Print out the hands
    print("\n")
    print(player)
    print("Player has %i" % add_cards(player))
    print("\n")
    print(dealer)
    print("Dealer has %i" % add_cards(dealer))
    if add_cards(player) > add_cards(dealer):
        return "Player"
    elif add_cards(player) < add_cards(dealer):
        return "Dealer"
    else:
        return "Push"


def main():
    # Create deck of cards
    deck = create_deck()
    # Shuffle deck of cards
    random.shuffle(deck)
    # Deal two cards to each player
    player = []
    dealer = []
    dealer_showing = []
    for position in range(2):
        player.append(deck.pop())
        dealer.append(deck.pop())
    dealer_showing.append("Xx")
    dealer_showing.append(dealer[1])
    print("\n")
    print(player)
    print("Player has %i" % add_cards(player))
    print("\n")
    print(dealer_showing)
    print("Dealer shows %i" % add_cards(dealer_showing))
    hit_or_stand = ""
    while hit_or_stand is not 's':
        hit_or_stand = raw_input("(H)it or (S)tand? ")
        if hit_or_stand is "h":
            player.append(deck.pop())
            if test_bust(player, "Player") is True:
                print("Player busts!")
                exit()
        else:
            break
    print("\n")
    print(dealer)
    print("Dealer has %i" % add_cards(dealer))
    while add_cards(dealer) <= 16:
        time.sleep(1)
        dealer.append(deck.pop())
        if test_bust(dealer, "Dealer") is True:
            print("Dealer busts!  Player wins!")
            exit()
    winner = who_wins(player, dealer)
    if winner is "Player":
        print("Player wins!")
    elif winner is "Dealer":
        print("Dealer wins.")
    else:
        print("Push... try again.")


if __name__ == "__main__":
    main()

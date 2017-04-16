#!/usr/bin/env python

# The purpose of this script is to create a parseable "log file" of hold'em hands
# The program takes one parameter: number of log lines to generate


import argparse
import random
import time


def add_players():
    players = []
    for i in range(1, 6):
        player_dict = {
            "name": "P"+ str(i),
            "card1": None,
            "card2": None,
        }
        players.append(player_dict)
    return players


def append_to_logfile(run_counter, players, community_cards, logfile):
    line_to_write = str(run_counter) + ": "
    for player in players:
        line_to_write += player['name'] + ": " + player['card1'] + "," + player['card2'] + " | "
    line_to_write += "CC: "
    comma_counter = 0
    for card in community_cards:
        if comma_counter != 4:
            line_to_write += card + ","
            comma_counter += 1
        else:
            line_to_write += card + "\n"
    logfile.write(line_to_write)


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


def deal_community_cards(deck):
    burn_pile = []
    community_cards = []
    # Burn one card then deal three cards (flop):
    burn_pile = deck.pop()
    community_cards.append(deck.pop())
    community_cards.append(deck.pop())
    community_cards.append(deck.pop())
    # Burn one card then deal one card (turn):
    burn_pile = deck.pop()
    community_cards.append(deck.pop())
    # Burn one card then deal last card (river):
    burn_pile = deck.pop()
    community_cards.append(deck.pop())
    return community_cards


def deal_hands(deck, players):
    for player in players:
        player['card1'] = deck.pop()
    for player in players:
        player['card2'] = deck.pop()
    return players


def main():
    # Parse the argument
    parser = argparse.ArgumentParser()
    parser.add_argument("number_of_runs", help="number_of_runs", type=int)
    args = parser.parse_args()
    # Create the logfile
    logfile_name = "holdem_logfile-" + str(int(time.time())) + ".log"
    logfile = open("logs/" + logfile_name, "w+")
    # Deal the player cards, community cards, and record the outcome to the logfile
    for run_counter in range(1,args.number_of_runs+1):
        # Create deck of cards
        deck = create_deck()
        # Shuffle deck of cards
        random.shuffle(deck)
        # Add players to the game
        players = add_players()
        # Deal two cards to each player
        players = deal_hands(deck, players)
        # Deal the community cards
        community_cards = deal_community_cards(deck)
        append_to_logfile(run_counter, players, community_cards, logfile)
    print("Done generating log file!")


if __name__ == "__main__":
    main()

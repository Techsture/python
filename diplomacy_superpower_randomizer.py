#!/usr/bin/python

import random

PLAYER_ONE = 'Andrei'
PLAYER_TWO = 'Dave'
PLAYER_THREE = 'Jarrod'
PLAYER_FOUR = 'Jeremy'
PLAYER_FIVE = 'Matthew'
PLAYER_SIX = 'Valerie'
PLAYER_SEVEN = 'Yassine'

def main():
  player_list = [PLAYER_ONE, PLAYER_TWO, PLAYER_THREE, PLAYER_FOUR, PLAYER_FIVE, PLAYER_SIX, PLAYER_SEVEN]
  superpowers = ['Austria', 'England', 'France', 'Germany', 'Italy', 'Russia', 'Turkey']
  random.shuffle(superpowers)
  while(superpowers):
    for player in player_list:
      print("{} is playing as {}".format(player, superpowers.pop()))
  exit()

if __name__ == '__main__':
  main()
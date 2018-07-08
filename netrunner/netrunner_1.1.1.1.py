#!/usr/bin/python

# This script picks a random configuration for playing 1.1.1.1 Netrunner.
# - 1 Core Set (Either Original or Revised)
# - 1 Expansion Set
# - 1 Datapack
# - 1 Random Card from all available cards

import random
from cards import card_list
from core import core_list
from datapacks import datapack_list
from expansions import expansion_list


def main():
  core_set = random.choice(core_list)
  expansion_set = random.choice(expansion_list)
  datapack = random.choice(datapack_list)
  print("Your Netrunner 1.1.1 configuration is:")
  print("1 \"{}\" set.".format(core_set))
  print("1 \"{}\" expansion.".format(expansion_set))
  print("1 \"{}\" datapack.".format(datapack))
  exit()


if __name__ == '__main__':
  main()

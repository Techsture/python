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
from original_core_set import original_core_set_list
from revised_core_set import revised_core_set_list


def main():
  corp_card = None
  runner_card = None
  core_set = random.choice(core_list)
  expansion_set = random.choice(expansion_list)
  datapack = random.choice(datapack_list)
  while corp_card is None:
    corp_card = random.choice(card_list)
    if corp_card['side_code'] is "runner":
      #print("{} is a Runner card (needs to be a Corp card).".format(corp_card['title']))
      corp_card = None
    try:
      if corp_card['pack_code'] in expansion_set or corp_card['pack_code'] in datapack:
        #print("Corp card \"{}\" is already included in either the chosen expansion ({}) or datapack ({}).".format(corp_card['title'], expansion_set, datapack))
        corp_card = None
    except:
      continue
    if core_set == "Original Core":
      for card in original_core_set_list:
        try:
          if card['title'] in corp_card['title']:
            #print("Corp card \"{}\" is already included in Original Core set.".format(corp_card['title']))
            corp_card = None
        except:
          continue
    else:
      for card in revised_core_set_list:
        try:
          if card['title'] in corp_card['title']:
            #print("Corp card \"{}\" is already included in Revised Core set.".format(corp_card['title']))
            corp_card = None
        except:
          continue
  while runner_card is None:
    runner_card = random.choice(card_list)
    if runner_card['side_code'] is "corp":
      #print("{} is a Corp card (needs to be Runner card).".format(runner_card['title']))
      runner_card = None
    try:
      if runner_card['pack_code'] in expansion_set or runner_card['pack_code'] in datapack:
        #print("Runner card \"{}\" is already included in either the chosen expansion ({}) or datapack ({}).".format(runner_card['title'], expansion_set, datapack))
        runner_card = None
    except:
      continue
    if core_set == "Original Core":
      for card in original_core_set_list:
        try:
          if card['title'] in runner_card['title']:
            #print("Runner card \"{}\" is already included in Original Core set.".format(runner_card['title']))
            runner_card = None
        except:
          continue
    else:
      for card in revised_core_set_list:
        try:
          if card['title'] in runner_card['title']:
            #print("Runner card \"{}\" is already included in Revised Core set.".format(runner_card['title']))
            runner_card = None
        except:
          continue
  print("Your Netrunner 1.1.1.1 configuration is:")
  print("- 1 \"{}\" set.".format(core_set))
  print("- 1 \"{}\" expansion.".format(expansion_set))
  print("- 1 \"{}\" datapack.".format(datapack))
  print("- 1 \"{}\" card for the corp.".format(corp_card['title']))
  print("- 1 \"{}\" card for the runner.".format(runner_card['title']))
  exit()


if __name__ == '__main__':
  main()

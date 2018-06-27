#!/usr/bin/python

# This script picks a configuration for playing 1.1.1 Netrunner.
# - 1 Core Set (Either Original or Revised)
# - 1 Expansion Set
# - 1 Datapack

import random


def main():
  core_list = [
    "Original Core",
    "Revised Core"
  ]
  expansion_list = [
    "Creation and Control",
    "Honor and Profit",
    "Order and Chaos",
    "Data and Destiny",
    "Reign and Reverie"
  ]
  datapack_list = [
    "What Lies Ahead (Genesis Cycle)",
    "Trace Amount (Genesis Cycle)",
    "Cyber Exodus (Genesis Cycle)",
    "A Study in Static (Genesis Cycle)",
    "Humanity's Shadow (Genesis Cycle)",
    "Future Proof (Genesis Cycle)",
    "Opening Moves (Spin Cycle)",
    "Second Thoughts (Spin Cycle)",
    "Mala Tempora (Spin Cycle)",
    "True Colors (Spin Cycle)",
    "Fear and Loathing (Spin Cycle)",
    "Double Time (Spin Cycle)",
    "Upstalk (Lunar Cycle)",
    "The Spaces Between (Lunar Cycle)",
    "First Contact (Lunar Cycle)",
    "Up and Over (Lunar Cycle)",
    "All That Remains (Lunar Cycle)",
    "The Source (Lunar Cycle)",
    "The Valley (SanSan Cycle)",
    "Breaker Bay (SanSan Cycle)",
    "Chrome City (SanSan Cycle)",
    "The Underway (SanSan Cycle)",
    "Old Hollywood (SanSan Cycle)",
    "The Universe of Tomorrow (SanSan Cycle)",
    "Kala Ghoda (Mumbad Cycle)",
    "Business First (Mumbad Cycle)",
    "Democracy and Dogma (Mumbad Cycle)",
    "Salsette Island (Mumbad Cycle)",
    "The Liberated Mind (Mumbad Cycle)",
    "Fear the Masses (Mumbad Cycle)",
    "23 Seconds (Flashpoint Cycle)",
    "Blood Money (Flashpoint Cycle)",
    "Escalation (Flashpoint Cycle)",
    "Intervention (Flashpoint Cycle)",
    "Martial Law (Flashpoint Cycle)",
    "Quorum (Flashpoint Cycle)",
    "Daedalus Complex (Red Sand Cycle)",
    "Station One (Red Sand Cycle)",
    "Earth's Scion (Red Sand Cycle)",
    "Blood and Water (Red Sand Cycle)",
    "Free Mars (Red Sand Cycle)",
    "Crimson Dust (Red Sand Cycle)",
    "Sovereign Sight (Kitara Cycle)",
    "Down the White Nile (Kitara Cycle)",
    "Council of the Crest (Kitara Cycle)",
    "The Devil and the Dragon (Kitara Cycle)",
    "Whispers in Nalubaale (Kitara Cycle)",
    "Kampala Ascendent (Kitara Cycle)"
  ]
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

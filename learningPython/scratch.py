#!/usr/bin/env python3

import re
import sys

testString = 'shrubbery'
print(testString)
testList = list(testString)
print(testList)
testList[1] = 'c'
print(testList)
testList.reverse()
print(testList)
testString = ''.join(testList)
print(testString)
testSplit = re.split('[/:]', '/usr/home/test')
print(testSplit)
print("My {1[kind]} runs {0.platform}".format(sys, {'kind': 'laptop'}) + '.')

quitProgram = False
while quitProgram is False:
  testNumber = int(input("Type a number: "))
  remainder = testNumber % 2
  if remainder is 0:
    print("{0} is an even number.".format(testNumber))
  else:
    print("{0} is an odd number.".format(testNumber))
  keepGoing = None
  while keepGoing is None:
    keepGoing = input("Do you want to continue? ").upper()
    if keepGoing in ['y', 'Y', 'yes', 'Yes', 'YES']:
      quitProgram = False
    elif keepGoing in ['n', 'N', 'no', 'NO']:
      print("Exiting...")
      quitProgram = True
    else:
      print("Input not recognized, please try again.")
      keepGoing = None

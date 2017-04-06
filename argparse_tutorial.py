#!/usr/bin/env python

# argparse Tutorial: https://docs.python.org/dev/howto/argparse.html

import argparse

# Initialize ArgumentParser object as parser
parser = argparse.ArgumentParser()
# Add expected argument to parser.  Needs to be type int for ** to work.
parser.add_argument("base", help="base", type=int)
# Add expected argument to parser.  Needs to be type int for ** to work.
parser.add_argument("exponent", help="exponent", type=int)
## If this option is set, store "True" in its place.
# parser.add_argument("-v", "--verbose", help="set verbosity flag", action="store_true")
# Add optional argument that takes parameters; if it's set to 1 then the output will be maths.  If set to 2, the output will be English (sentence format).
parser.add_argument("-v", "--verbose", help="set verbosity flag. 1=maths, 2=English", type=int, choices=[1, 2], default=0)
# Parse arguments
args = parser.parse_args()
# Calculate the square of the number passed
answer = (args.base ** args.exponent)
# If -v is set, be verbose, depending on the type requested:
if(args.verbose == 1):
	print("%d^%d = %d" % (args.base, args.exponent, answer))
elif(args.verbose == 2):
	print("%d to the power of %d equals %d." % (args.base, args.exponent, answer))
else:
	print(answer)

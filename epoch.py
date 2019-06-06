#!/usr/bin/python

# Get current UTC epoch time in milliseconds

import time

milliseconds = int(round(time.time() * 1000))
print(milliseconds)

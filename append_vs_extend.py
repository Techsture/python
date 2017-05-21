#!/usr/bin/env python

# Demonstrates the difference between append() and extend()

def main():
  a = [1, 2, 3]
  print("a = %s" % a)
  a.append([4, 5])
  print("append [4, 5] onto a = %s" % a)
  a.extend([6, 7])
  print("extend [6, 7] onto a = %s" % a)


if __name__ == "__main__":
  main()


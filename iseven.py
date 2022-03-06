#!env python
# implements an isEven check
import sys

def isEven(num):
  if num&1 == 0:
    return True
  else:
    return False

print(isEven(int(sys.argv[1])))
#!/usr/bin/env python

# Given an array and a value, how to implement a function to remove all
# instances of that value in place and return the new length?
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.

import sys

ar0 = sys.argv
ar0.pop(0)  # remove the command from the input array
num_to_remove = ar0.pop(0)

for i in range(0, len(ar0)-1):
    if ar0[i] == num_to_remove:
        ar0.pop(i)

print(ar0)

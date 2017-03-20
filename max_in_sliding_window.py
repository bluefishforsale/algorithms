#!/usr/bin/env python

# Given an array of numbers and a sliding window size,
# how to get the maximal numbers in all sliding windows?

import sys

# remove command name
ar0 = sys.argv
ar0.pop(0)

window_size = int(ar0.pop(0))
print("window size: %d" % window_size)

def slide(array, window_size):
    if len(array) > window_size:
        max = int(array.pop(0))

        for i in range(0, window_size):
            if int(array[i]) >  max:
                max = int(array[i])

        print("current array: %s, Max: %d" % (array[0:window_size], max))
        slide(array, window_size)
    else:
        return

slide(ar0, window_size)

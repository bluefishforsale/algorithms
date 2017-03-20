#!/usr/bin/env python

# Given an array,
# please determine whether it contains three numbers
# whose sum equals to 0.

import sys

input_array = sys.argv
input_array.pop(0)
print input_array

def sum_of_three(array):
    if len(array) > 3:
        x = array.pop(0)
        if int(x) + int(array[1]) + int(array[2]) == 0:
            print("%s + %s + %s = 0" % (x ,array[1], array[2]))
        sum_of_three(array)
    return


sum_of_three(input_array)

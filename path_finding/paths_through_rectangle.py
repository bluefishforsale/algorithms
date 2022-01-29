#!env python2

# Write a function which returns the count of unique routes through
# a rectangle of N * M. No diagonals allowed. Each path may only be used once.
# Examples:
# inputs: n=4, m=2
# output = 4
# inputs: n=3, m=4
# output = 10

def rect_path(x,y):
  # re-orient
  bigger = max(x,y)
  smaller = min(x,y)
  # if any is zero, we have a point.
  # start and end are the same I guess, return zero
  if smaller == 0:
    return 0
  # if the smallest dimension is 1, then we  have a line.
  # return the length of the line
  if smaller == 1:
    # there is only one path through a line, no matter how long
    return bigger
  # all other cases have both dimensions >= 2
  # imagine the box to only be two rows but X columns
  # we call outself every time with a reduced smaller until
  # it fails the base case
  return rect_path(bigger, smaller-1) + rect_path(bigger-1, smaller)


for n in range(2,12):
  for m in range(1,10):
    print("inputs: ({},{}) = {}".format(n, m, rect_path(n, m)))
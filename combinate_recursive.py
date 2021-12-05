def flatten(nested):
    # print(nested)
    return [ first for second in nested for first in second ]

def combinate(data):
    # called with zero length
    if len(data) == 0:
        return
    # called with only one item, no combinations possible
    # return as a list to be safe
    if len(data) ==1:
        return [data]
    # internal local ephemeral list to append resulting combinations lists
    res = list()
    # called with >= 2 items, combinations possible
    # loop over the array, create combinations at each index element (i)
    for i in range(len(data)):
        # store the cursor position element
        cur = data[i]
        # all items in list except cursor using slices
        others = data[:i] + data[i+1:]
        # iterate over recursive function call results (oc)
        # call recursive with all non-cursor elements of array
        for oc in combinate(others):
            # prepend cursor on each combination
            res.append(flatten([cur] + [oc]))
    # supposedly we're done, return the list of combinations
    return res


print(combinate('123'))
print(combinate( [1,2,3] ))
print(combinate('abc'))
print(combinate(['a', 'b', 'c']))
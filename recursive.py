def flatten(nested):
    print(nested)
    return [ first for second in nested for first in second ]

def permute(data):
    if len(data) == 0:
        return
    if len(data) ==1:
        return [data]
    res = list()
    # all other cases
    for i in range(len(data)):
        # cursor
        cur = data[i]
        # all but cursor
        others = data[:i] + data[i+1:]
        # permute all others but cursor
        for op in permute(others):
            # prepend cursor on each permutation
            # print(op)
            res.append(flatten([cur] + [op]))
    return res


print(permute('123'))
print(permute( [1,2,3] ))
print(permute('abc'))
print(permute(['a', 'b', 'c']))
# print(recurive('1234567'))
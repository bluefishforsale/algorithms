#!env python2

def permute(data):
    # are we a list of lists?
    if isinstance(data[0], list):
        return permute(data[0])
    if len(data) == 0:
        return
    if len(data) == 1:
        return data
    res = list()
    for i in range(len(data)):
        pos = data[i]
        oth = data[:i] + data[i+1:]
        for j in permute(oth):
            # if isinstance(pos, int):
            #     pos = [pos]
            # if isinstance(j, int):
            #     j = [j]
            res.append([pos] + [j])
    return res

print(permute('123'))
print(permute(['123']))
print(permute([1,2,3]))
print(permute( [[1,2,3], [4,5,6]] ))
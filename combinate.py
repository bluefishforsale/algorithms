#!env python2

# def combinate_loop(data):
#     res = list()
#     for sub in data:
#       for i in range(len(sub)):
#           res.append( sub[i::] + sub[:i] )
#     return res

# print(combinate_loop( [[1,2,3], [1,4,5], [2,0,6]] ))
# print(combinate_loop( [["#",2,3], [1,"#",5], [2,0,"#"]] ))
# print(combinate_loop( [["#","X","0"], ["%","_","*"], ["&","@","+"]] ))

# def flatten(nested):
#     return [ first for second in nested for first in second ]

# def flip2(A, B):
#     return [B, A]

# def combinate_heap(data):
#     comb = list()
#     for i in range(0, len(data)*2):
#         new = flatten([ flip2( data[i], data[i+1] ), data[i+2:] ])
#         comb.append( new )
#         data.append(data[0])
#     return comb


# print(combinate_heap( [1,2,3] ))
# print(combinate_heap( [1,2,3,4] ))
# print(combinate_heap( [[1,2,3], [1,4,5], [2,0,6]] ))
# print(combinate_heap( [["#",2,3], [1,"#",5], [2,0,"#"]] ))
# print(combinate_heap( [["#","X","0"], ["%","_","*"], ["&","@","+"]] ))


def permutate(data):
    if len(data) == 0:
        return
    if len(data) == 1:
        return data
    tmp = list()
    for i in range(len(data)):
        cur = data[i]
        others = data[:cur] + data[cur+1:]
        for j in permutate(others):
            tmp.append([cur] + j)
    return tmp

print(permutate( '123' ))
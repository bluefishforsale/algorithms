#!env python

def combinate(data):
    res = list()
    for sub in data:
      for i in range(len(sub)):
          res.append( sub[i::] + sub[:i] )
    return res

print(combinate( [[1,2,3], [1,4,5], [2,0,6]] ))
print(combinate( [["a",2,3], [1,"x",5], [2,0,"j"]] ))
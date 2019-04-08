#!/usr/bin/python

a = [1, 2, 3]
b = [2, 3, 4]

def intersect_list(list1, list2):
  intersect = []
  i = 0
  j = 0

  while (i < len(list1) and j < len(list2)): 
    if list1[i] == list2[j]:
      intersect.append(list1[i])
      i += 1
      j += 1

    elif list1[i] > list2[j]:
      j += 1

    elif list1[i] < list2[j]:
      i += 1

  return intersect


print(intersect_list(a,b))
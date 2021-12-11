#!env python2

def rreverse(data):
    if len(data) == 0:
        return
    if len(data) == 1:
        return data
    this = list()
    for i in range(len(data)):
        return data[-1] + rreverse(data[i:-1])

print(rreverse('abc'))
print(rreverse('1234567890'))

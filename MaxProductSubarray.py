data = [2, 3, -2, 4]
data =  [ -1, -2, 0 ]

def product(value):
  product = 1
  for x in value:
    product = product * x
  return product

def max_product_subarray(value):
  subarray = value
  p = product(subarray)
  # walk the full length
  for i in range(0, len(value) -1):
  # walk increasing ranges starting at i
    for j in range(1, len(value)):
      print(i, j, value[i:i+j], product(value[i:i+j]))
      if product(value[i:i+j]) >= p:
        subarray = value[i:i+j]
        p = product(value[i:i+j]) 
  return p, subarray

print(data)
print(max_product_subarray(data))
data = [2, 3, -2, 4]
# data = [2, 3, -2, 4, 2, 3, 1]

def product(input):
  product = 1
  for x in input:
    product = product * x
  return product

def max_product_subarray(input):
  subarray = input
  p = product(subarray)
  # walk the full length
  for i in range(0, len(input) -1):
  # walk increasing ranges starting at i
    for j in range(1, len(input) -1):
      if product(input[i:i+j]) >= p:
        subarray = input[i:i+j]
        p = product(input[i:i+j]) 
  return p, subarray

print(max_product_subarray(data))
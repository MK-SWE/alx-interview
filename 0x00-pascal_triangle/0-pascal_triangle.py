#!/usr/bin/python3
"""
pascal_triangle
a function that create a list of lists to solve pascal's triangle
"""
def pascal_triangle(n):
  if n == 1:
    return [[1]]
  elif n <= 0:
    return [[]]
  result = [[1]]
  arr = [1]
  for i in range(n - 1):
    c = []
    arr.insert(0, 0)
    arr.append(0)
    for j in range(len(arr) - 1):
      c.append(arr[j] + arr[j+1])
    arr.pop(0)
    arr.pop()
    arr = c
    result.append(arr)
  return result

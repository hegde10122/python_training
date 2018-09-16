'''
Arithmetic with numpy arrays
-----------------------------------

Arrays are important because they enable you to express batch operations on data
without writing any for loops. This is also called as vectorization. Any arithmetic
operations between equal-size arrays applies the operation element-wise
'''
import numpy as np

arr = np.array([[1.2,3.4, 5.6],[4,5,6]])
print(arr)

print(arr * arr)
print(1/arr)
print(arr ** 0.5)
print(arr - arr)

arr2 = np.array([[1.22,3.24, 15.6],[14,5,6]])

print(arr2 > arr) # comparing elementwise of similar sized arrays yeilds boolean array


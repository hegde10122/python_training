'''
INDEXING AND SLICING of ndarrays
'''

import numpy as np

arr = np.arange(10)
print(arr)

print(arr[5:8]) #index 8 is not included ---only 3 elemnts at index 5,6,7

arr[5:8] = 19
print(arr)

'''
If you assign a scalar value to a slice, as in arr[5:8] = 19, the value is propagated (or broadcasted henceforth)
to the entire selection.

An important first distinction from Python’s built-in lists is that array slices are views on the original array.
This means that the data is not copied, and any modifications to the view will be
reflected in the source array. 
'''
arr_slice = arr[5:8]
print(arr_slice)

arr_slice[1] = 22
print(arr) #The changes are reflected in the original array

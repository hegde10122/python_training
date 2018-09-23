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

'''
In a two-dimensional array, the elements at each index are no longer scalars but rather one-dimensional
arrays
'''
arr2d = np.array([[1, 12, 3], [4, 5, 16], [7, 11, 9]])
print(arr2d[2])

'''
Individual elements can be accessed recursively. But that is a bit too much
work, so you can pass a comma-separated list of indices to select individual elements.
So these are equivalent
'''
print(arr2d[0][1])
print(arr2d[0,1])

'''
In multidimensional arrays, if you omit later indices, the returned object will be a lower dimensional ndarray 
consisting of all the data along the higher dimensions. 
'''

arr3d = np.array([[[1, 2, 3], [4, 15, 6]], [[7, 18, 9], [10, 11, 12]]]) # 2 X 2 X 3 array
print(arr3d[0]) # gives a 2x3 array

'''
Both scalar values and arrays can be assigned to arr3d[0]
'''

old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)

'''
arr3d[1, 0] gives you all of the values whose indices start with (1, 0),
forming a 1-dimensional array

Note that in all of these cases where subsections of the array have been selected, the
returned arrays are views.
'''
print(arr3d[1, 0])

'''
Indexing with slices

Like one-dimensional objects such as Python lists, ndarrays can be sliced with the
familiar syntax
'''
print(arr[1:4])

'''
Consider the two-dimensional array from before, arr2d. Slicing this array is a bit
different.
'''

print(arr2d[:2]) #select the first two rows of arr2d.

'''
You can pass multiple slices just like you can pass multiple indexes
When slicing like this, you always obtain array views of the same number of dimensions.
'''

print(arr2d[:2, 1:])

'''
By mixing integer indexes and slices, you get lower dimensional slices.
For example, You can select the second row but only the first two columns
'''
print(arr2d[1, :2])

'''
Similarly, I can select the third column but only the first two rows 
'''
print(arr2d[:2, 2])

'''
 Note that a colon by itself means to take the entire axis, so you can slice only higher dimensional axes by doing

'''
print(arr2d[:, :1])

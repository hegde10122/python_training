'''
CREATING ndarrays by using array functions
'''

'''
Problem 4)
Using a list to create ndarray
'''

import numpy as np
data1 = [4.5, 6.7, 1]
arr1 = np.array(data1) # array function used to create ndarray from a list
print(arr1)

'''
Problem 5)
Using list of lists to create multidimensional array
'''
data2 = [[1.4,5.6,7],[5.8, 9,0.3]]
arr2 = np.array(data2) # array function to create multidimensional array using list of lists

#Since data2 was a list of lists, the NumPy array arr2 has two dimensions with shape inferred from the data. 
print(arr2) 

'''
Problem 6)
Find the dimension and shape of arr2 above
'''
print(arr2.ndim)
print(arr2.shape) # 2 dimensions having 3 columns each is depicted by the tuple (2, 3)


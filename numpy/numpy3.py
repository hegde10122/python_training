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

'''
Problem 7)
create an ndarray of 0s of length 50 
'''
arr3 = np.zeros(50) 
print(arr3)

'''
Problem 8)
create an ndarray of 1s of length 25 and shape 6
'''
arr4 = np.ones((25, 6))  # passing tuple as the parameter containing the length value 25 and the shape value 6
print(arr4)

'''
Problem 9)
Create an ndarray of length 16 and shape 3 without initialising its value to any particular value
'''

arr5 = np.empty((16,3))
print(arr5) # uninitialised garbage values are returned

'''
Problem 10)
create an ndarray of ones using arr5 above with specifying shape and length values explicitly
create an ndarray of zeros using arr4 above with specifying shape and length values explicitly
'''

arr6 = np.ones_like(arr5)
print(arr6)

arr7 = np.zeros_like(arr4)
print(arr7)

'''
Problem 11)
create an ndarray with ones on the main diagonal and zeros elsewhere containg 6 rows, 5 columns and data type integer
'''
arr8 = np.eye(6,5,0,dtype=int) # 0 refers to the main diagonal
print(arr8)


'''
Problem 12)
create an ndarray with ones on the 3rd lower diagonal and zeros elsewhere containg 10 rows, 9 columns and data type float
'''
arr9 = np.eye(10,9,-3,dtype=float) # -3 refers to the third lower diagonal
print(arr9)

'''
Problem 13)
create an ndarray with ones on the 6th upper diagonal and zeros elsewhere containg 10 rows, 10 columns and data type int
'''

arr10 = np.eye(10,10,6,dtype = int)
print(arr10)

'''
Problem 14) 
create an ndarray with 3 rows with cells having value 2.9 and store the data in C-contiguous order in memory
'''

arr11 = np.full(3,2.9,dtype=float,order='C')
print(arr11)

'''
Problem 15) 
create an ndarray with 7 rows and 13 columns with cells having value 6 and store the data in Fortran-contiguous order in memory
'''
arr12 = np.full((7,13), 6, dtype = int,order = 'F')
print(arr12)

'''
Problem 16)
Using arr12 above create identical shaped array but this time with all the cells filled with value 8.75
'''

arr13 = np.full_like(arr12,8.75,dtype=float)
print(arr13)

'''
Problem 17)
Create an identity matrix of size 13 X 13 with all cells treated as an integer value
'''

arr14 = np.identity(13,dtype = int)

# dtype is a special object containing information the ndarray needs to interpret a chunk of memory as a particular type of data
# dtype in short is the metadata (data about data)
print(arr14)


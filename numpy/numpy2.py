'''
The NumPy ndarray: A Multidimensional Array Object

One of the key features of NumPy is its N-dimensional array object, or ndarray,
which is a fast, flexible container for large datasets in Python. 
Arrays enable you to perform mathematical operations on whole blocks of data using similar syntax to the 
equivalent operations between scalar elements.
'''

'''
Problem 2) 
Generating random data using ndarray
'''

import numpy as np

data1 = np.random.randn(3) # returns a random sample
print(data1) # run the program in python terminal to see the result --- row-vector with 3 elements is produced

data2 = np.random.randn(2,4) # returns a random array with 2 rows and 4 columns each
print(data2) # run the program in python terminal to see the result --- array with 2 rows and 4 columns is produced

# performing mathematical operations on the ndarray
data3 = data2 * 5 # multiply each element by 5
print(data3)

# produces a new array wherein each "cell" of data2 is added to each other
data4 = data2 + data2
print(data4)


'''
Problem 3)
To find size of each dimension of data4 produced above and also finding the data type of the array
'''
# to get the size of each dimension of data4 we use the shape method that returns the tuple
print(data4.shape) # prints a tuple (2, 4) indicating that there are 2 dimensions with size 4 each

# to get the data type of the array we use the object dtype
print(data4.dtype) # prints float64 indicating each cell value is a floating-point value occupying 64 bits in memory

'''
numpy tutorial - part 1

salient features of numpy
--------------------------
1) It contains ndarray, an efficient multidimensional array providing fast array-oriented arithmetic operations
 and flexible broadcasting capabilities.

2) Mathematical functions for fast operations on entire arrays of data without having to write loops

3) Tools for reading/writing array data to disk and working with memory-mapped files.

4) Linear algebra, random number generation, and Fourier transform capabilities

5) A C API for connecting NumPy with libraries written in C, C++, or FORTRAN.

6) Fast vectorized array operations for data munging and cleaning, subsetting and 
   filtering, transformation, and any other kinds of computations

7) Common array algorithms like sorting, unique, and set operations

8) Efficient descriptive statistics and aggregating/summarizing data

9) Data alignment and relational data manipulations for merging and joining together heterogeneous datasets

10) Expressing conditional logic as array expressions instead of loops with if-elif-else branches

11) Group-wise data manipulations (aggregation, transformation, function application)

-------------------------------------------------------------

Note:-
-----

While NumPy provides a computational foundation for general numerical data processing, it is efficient to use 
pandas as the basis for most kinds of statistics or analytics, especially on tabular data. 
Pandas also provides some more domainspecific functionality like time series manipulation, which is not present in NumPy.

Importance of Numpy
---------------------

1) 
NumPy internally stores data in a contiguous block of memory, independent of other built-in Python objects. 
NumPy’s library of algorithms written in the C language can operate on this memory without any type checking or other overhead.
NumPy arrays also use much less memory than built-in Python sequences.

2) NumPy operations perform complex computations on entire arrays without the need for Python for loops.

'''

# importing the packages numpy and time
import numpy as np
import time
'''
Problem 1)

TO check the performance difference of a Numpy array and the equivalent python list of 10 million integers
'''

my_arr = np.arange(10000000) # arange is a built-in method that returns ndarray

my_list = list(range(10000000))

# multiplying each sequence by 2

#starting the timer
start = time.time()

for _ in range(10):
    my_arr2 = my_arr * 2

end = time.time()

# run the program in python terminal to see the result
print(end - start) # prints the time to execute the multiplication using numpy array

# The above operation happens in about 0.5 secs approximately

# Repeating the above process again but this time for the python list

start = time.time()

for _ in range(10):
    my_list2 = [x * 2 for x in my_list]

end = time.time()

# run the program in python terminal to see the result
print(end - start) # prints the time to execute the multiplication using python list

# The above operation happens in about 12 secs approximately

# Thus the numpy array is faster in comparison to the python list operation (12 / 0.5) = 24 times

# The numbers will differ on your machine depending upon memory

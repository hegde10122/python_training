'''
problem 18)
cast an integer ndarray to floating-type ndarray
'''
import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr.dtype)

float_arr = arr.astype(np.float64)
print(float_arr,float_arr.dtype)


'''
problem 19)
cast a floating-point ndarray to an integer array
'''
arr1 = np.array([1.2, 3.4, -2.6, 7.8,-0.73])
arr2 = arr1.astype(np.int32)
print(arr2)

'''
problem 20)
convert an ndarray of strings representing numbers to an array in numeric form
'''

arr3 = np.array(['1.33', '.43', '-23.4'],dtype=np.string_)
print(arr3,arr3.dtype)

arr4 = arr3.astype(float)
print(arr4)

'''
SALIENT FEATURES OF PANDAS
-------------------------------------

1) The python tool Pandas contains data structures and data manipulation tools designed to make data cleaning
and analysis fast and easy in Python. 

2) Pandas is often used in tandem with numerical computing tools like NumPy and SciPy, analytical libraries like statsmodels and
scikit-learn, and data visualization libraries like matplotlib. 

3) Pandas adopts significant parts of NumPy’s idiomatic style of array-based computing, especially array-based
functions and a preference for data processing without for loops.

4) While pandas adopts many coding idioms from NumPy, the biggest difference is that pandas is designed for working with tabular or heterogeneous data.
   NumPy, by contrast, is best suited for working with homogeneous numerical array data.

'''
import pandas as pd #importing packages
import numpy as np

'''
You may also find it easier to import Series and DataFrame into the local namespace since they are so fre‐
quently used

from pandas import Series, DataFrame

To get started with pandas, you will need to get comfortable with its two workhorse data structures: Series and DataFrame.
'''

#####################################################################################################################################
########################   Series ############################################
#####################################################################################################################################

'''
A Series is a one-dimensional array-like object containing a sequence of values and an associated array of data labels, called its index.
The simplest Series is formed from only an array of data.

The string representation of a Series displayed interactively shows the index on the 
left and the values on the right. Since we did not specify an index for the data, a 
default one consisting of the integers 0 through N - 1 (where N is the length of the data) is created.
'''
obj = pd.Series([4, 71, -15, 13])
print(obj)

'''
You can get the array representation and index object of the Series via
its values and index attributes, respectively
'''
print(obj.values)
print(obj.index)

'''
Often it will be desirable to create a Series with an index identifying each data point with a label
'''
obj2 = pd.Series([4, 71, -15, 13], index=['d', 'b', 'a', 'c'])
print(obj2)

print(obj2.values)
print(obj2.index)

'''
You can use labels in the index when selecting single
values or a set of values
'''
print(obj2['a'])
obj2['d'] = 6
print(obj2)

print(obj2[['c', 'a', 'd']])

print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

'''
Another way to think about a Series is as a fixed-length, ordered dict, as it is a map‐
ping of index values to data values. It can be used in many contexts where you might
use a dict
'''
print('b' in obj2)
print('e' in obj2)

'''
Should you have data contained in a Python dict, you can create a Series from it by
passing the dict
'''
sdata = {'Oswal': 3500, 'Trax': 7000, 'Owata': 1000, 'Umbrella': 50780}
obj3 = pd.Series(sdata)
print(obj3)

'''
When you are only passing a dict, the index in the resulting Series will have the dict’s
keys in sorted order. You can override this by passing the dict keys in the order you
want them to appear in the resulting Series.

Here, three values found in sdata were placed in the appropriate locations, but since
no value for 'Tripura' was found, it appears as NaN (not a number), which is con‐
sidered in pandas to mark missing or NA values. Since 'Umbrella' was not included in
states, it is excluded from the resulting object.
'''
states = ['Oswal', 'Trax', 'Owata', 'Tripura']
obj4 = pd.Series(sdata, index=states)
print(obj4)

'''
The isnull and notnull functions in pandas should be used to detect missing data
'''
print(pd.isnull(obj4))
print(obj4.isnull())

'''
Both the Series object itself and its index have a name attribute, which integrates with
other key areas of pandas functionality
'''
obj4.name = 'population'
obj4.index.name = 'state'

print(obj4)

'''
A Series’s index can be altered in-place by assignment
'''
obj4.index = ['Babba', 'Shani', 'Gyani', 'Rafa']
print(obj4)

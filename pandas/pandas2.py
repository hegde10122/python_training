import pandas as pd
import numpy as np
'''
DataFrame

A DataFrame represents a rectangular table of data and contains an ordered collec‐
tion of columns, each of which can be a different value type (numeric, string,
boolean, etc.). The DataFrame has both a row and column index; it can be thought of
as a dict of Series all sharing the same index. Under the hood, the data is stored as one
or more two-dimensional blocks rather than a list, dict, or some other collection of
one-dimensional arrays. 

While a DataFrame is physically two-dimensional, you can use it to
represent higher dimensional data in a tabular format using hierarchical indexing.
'''


'''
There are many ways to construct a DataFrame, though one of the most common is
from a dict of equal-length lists or NumPy arrays
'''

data = {'state': ['Oshiwara', 'Oshiwara', 'Oshiwara', 'Navapura', 'Navapura', 'Navapura'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

print(frame)

'''
For large DataFrames, the head method selects only the first five rows
'''
print(frame.head())

'''
If you specify a sequence of columns, the DataFrame’s columns will be arranged in
that order
'''
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

'''
If you pass a column that isn’t contained in the dict, it will appear with missing values
in the result
'''
print(pd.DataFrame(data, columns=['year', 'state', 'pop','clean']))

'''
A column in a DataFrame can be retrieved as a Series either by dict-like notation or
by attribute.

frame2[column] works for any column name, but frame2.column
only works when the column name is a valid Python variable
name

'''

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four','five', 'six'])
print(frame2)
print(frame2.columns)
print(frame2['state'])
print(frame2.year)

'''
Rows can also be retrieved by position or name with the special loc attribute
'''
print(frame2.loc['three'])

'''
Columns can be modified by assignment. For example, the empty 'debt' column
could be assigned a scalar value or an array of values
'''
frame2['debt'] = 14.52
print(frame2)

frame2['debt'] = np.arange(6.)
print(frame2)

'''
When you are assigning lists or arrays to a column, the value’s length must match the
length of the DataFrame. If you assign a Series, its labels will be realigned exactly to
the DataFrame’s index, inserting missing values in any holes
'''
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

'''
Assigning a column that doesn’t exist will create a new column. The del keyword will
delete columns as with a dict
'''
frame2['east'] = frame2.state == 'Oshiwara'
print(frame2)

# The del method can then be used to remove this column
del frame2['east']
print(frame2)
print(frame2.columns)

'''
The column returned from indexing a DataFrame is a view on the
underlying data, not a copy. Thus, any in-place modifications to the
Series will be reflected in the DataFrame. The column can be
explicitly copied with the Series’s copy method
'''

'''
Another common form of data is a nested dict of dicts
'''

pop = {'Navapura': {2001: 2.4, 2002: 2.9},'Oshiwara': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

'''
If the nested dict is passed to the DataFrame, pandas will interpret the outer dict keys
as the columns and the inner keys as the row indices
'''
frame3 = pd.DataFrame(pop)
print(frame3)

'''
You can transpose the DataFrame (swap rows and columns) with similar syntax to a NumPy array
'''
print(frame3.T)

'''
The keys in the inner dicts are combined and sorted to form the index in the result.
This isn’t true if an explicit index is specified
'''
#print(pd.DataFrame(pop, index=[2001, 2002, 2003]))

'''
Dicts of Series are treated in much the same way
'''
pdata = {'Oshiwara': frame3['Oshiwara'][:-1],'Navapura': frame3['Navapura'][:2]}
print(pd.DataFrame(pdata))

'''
If a DataFrame’s index and columns have their name attributes set, these will also be
displayed
'''
frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3)

'''
As with Series, the values attribute returns the data contained in the DataFrame as a
two-dimensional ndarray
'''
print(frame3.values)

'''
If the DataFrame’s columns are different dtypes, the dtype of the values array will be
chosen to accommodate all of the columns
'''
print(frame2.values)

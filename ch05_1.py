#
# * Chapter 05, Series

#%%
# * import libs
import numpy as np
import pandas as pd 
from pandas import Series, DataFrame
import matplotlib.pyplot as plt 


np.random.seed(12345)
# %%
# * Create Pandas Series
obj = Series([4, 7, -5, 3])
obj
# %%
# * check Series value and index 
# ? Series is one dimensional array-like object, containing (1) a sequence of 
# ? values, (2) an associated array of data labels, called *index*
obj.values
# %%
obj.index
# %%
# * create a Series with a designated index
obj2 = Series([4,7,-5,3], index=['d','b','a','c'])
obj2
# %%
obj2.index
# %%
obj2['d']
#%%
obj2[['a', 'b', 'c']]
# %%
# * Using numpy functions/operations will preserve the index-value links
obj3 = obj2[obj2 > 0]
obj3
# %%
obj3 = obj2*2
obj3
# %%
# * we can think about Series is as ordered dictionary
'b' in obj2
# %%
'f' in obj2
# %%
# * Actually, we can create Series from a python dict
# * the key in dict is index in Series, the value in dict is value in Series
obj3 = Series({'a':123, 'b': 456, 'c': 789})
obj3
# %%
# * When creating Series using dict, index can be override
letters = ['x','y','z', 'a', 'b', 'c']
obj4 = Series({'a':123, 'b': 456, 'c': 789}, index=letters)
obj4
# %%
# * static and instance methods to check null/NaN
pd.isnull(obj4)
# %%
pd.notnull(obj4)
# %%
obj4.isnull()
# %%
obj4.notnull()
# %%
# * both Series and its index have a name attribute, default is nothing
obj4.name = 'seqence number'
# %%
obj4.index.name = 'letters'
# %%
obj4
# %%
# * index can be altered in-place
obj
# %%
obj.index=['Alex','Bob','Cindy', 'Daisy']
# %%
obj
# %%

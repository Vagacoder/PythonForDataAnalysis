#
# * Chapter 05, DataFrame

#%%
# * import libs
import numpy as np
import pandas as pd 
from pandas import Series, DataFrame
import matplotlib.pyplot as plt 


np.random.seed(12345)
# %%
data = {
    'state': ['Ohio', 'Ohio','Ohio', 'Nevada', 'Nevada','Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}
frame = DataFrame(data)
# %%
frame
# %%
frame.head()
# %%
# * get a sub dataframe or rearrange column orders
DataFrame(data, columns=['year', 'state'])
# %%
# * a column does not exsits, will get NaN for its values
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                    index=['one','two','three', 'four', 'five', 'siz'])
frame2
# %%
# * check dataframe attributes
frame2.columns
# %%
frame2.values
# %%
frame2.index
# %%
# ! access **COLUMN** value through dataframe index 
frame2['state']
# %%
# ! access **COLUMN** value through datafram . operator
frame2.state
# %%
# ! access **ROW** of dataframe
frame2.loc['three']
# %%
# TODO P.131
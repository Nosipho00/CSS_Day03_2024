# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:39:11 2024

@author: NosiphoM
"""

import pandas as pd
# import methplotlib.pyplot as plt
df=pd.pandas.read_csv("time_series_data.csv")
print(df.info())

df['Date']= pd.to_datetime(df['Date'],format="%Y-%m-%d")
print(df.info())

# plt.plot(df['Date'], df['Temperature'])

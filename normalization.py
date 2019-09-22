# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:23:41 2019

@author: YIFAN DANG
"""
import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing

small_business=pd.read_csv('Maryland SBDC Data 4 UMD Data Challenge 2019.csv',sep=',',
                           header=0)

np.mean(small_business.iloc[:,6])
np.std(small_business.iloc[:,6])
np.mean(small_business.iloc[:,7])
np.std(small_business.iloc[:,7])
np.mean(small_business.iloc[:,8])
np.std(small_business.iloc[:,8])
np.mean(small_business.iloc[:,10])
np.std(small_business.iloc[:,10])
np.mean(small_business.iloc[:,11])
np.std(small_business.iloc[:,11])   

nan_row=small_business[small_business['Impact: Capital Investments'].isnull()]
small_business.isnull().sum()
small_business=small_business.drop(small_business.index[92])

def scale(df):
    for i in list:
        df.iloc[:,i]=preprocessing.scale(df.iloc[:,i])
    return df
    
small_business=scale(small_business)
small_business.to_excel("small_business scale.xlsx")




# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 20:45:45 2019

@author: yifan
"""
from pathlib import Path
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('C:/Users/yifan.000/Desktop/data challenge')
small_business=pd.read_excel('Maryland SBDC Data 4 UMD Data Challenge 2019.xlsx')
small_business=small_business.drop(small_business.index[:19])
new_header=small_business.iloc[0]
small_business=small_business[1:]
small_business.columns=new_header
small_business.index=range(len(small_business.index))
small_business.drop(small_business.columns[[0]]).to_csv('small_business.csv')

small_business.info()
small_business.describe
n_index=[4,6,7,8,10,11]

numerical=small_business.describe(include='float64')
categorical=small_business.describe(include='object')

###plot### 
plt.hist(small_business.iloc[:,10], density=True,edgecolor='black')
plt.show
plt.title('counseling time')
plt.xlabel('hours')
plt.ylabel('frequencies')



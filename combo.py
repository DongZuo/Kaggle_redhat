# -*- coding: utf-8 -*-
"""
Created on Mon Sep  17 12:01:25 2016

@author: DZ
"""

import pandas as pd
import numpy as np
leak=pd.read_csv(r"D:\python\red hat\dataset\leak.csv")
xgb=pd.read_csv(r"D:\python\red hat\dataset\raddar.csv")

'''
# change column name
filled=leak.outcome
leak['filled']=filled
del leak['outcome']
'''


nan_in_leak=leak[np.isnan(leak['filled'])]
nan_to_filled=nan_in_leak.merge(xgb,how='left',on='activity_id')

nan_to_filled.filled=nan_to_filled.outcome
del nan_to_filled['outcome']

leak_without_nan=leak.dropna()
print(leak_without_nan.count())
print(nan_to_filled.count())

submit=leak_without_nan.append(nan_to_filled)
output=pd.DataFrame({'activity_id':submit['activity_id'],'outcome':submit['filled']})
output.head()
output.to_csv('combo.csv',index=False)

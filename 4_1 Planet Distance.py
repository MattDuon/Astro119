# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:24:51 2019

@author: maduong
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils

Plan_Dist = np.genfromtxt('planet_distance.txt', usecols=(1,2))
x = Plan_Dist[:,0]
y = Plan_Dist[:,1]
#plt.loglog(x,y)
#plt.show()

dDic = opt_utils.lin_LS(np.log10(x), np.log10(y))
print dDic
a_yhat = 10**(dDic['a']*x**dDic['b'])
b = dDic['b']
print b

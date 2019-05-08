# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:02:21 2019

@author: maduong
"""
"""
    1 - create synthetic well pressure time series
    2 - compute mean in each well
    3 - compute stdev in each well
    
"""
import numpy as np
import matplotlib.pyplot as plt


#===================
#parameters
#===================
iWells = 10
iMeas  = 12

#===================
# create synthetic
#===================
a_mu_syn = np.random.random_integers(20, 40, iWells)
a_std_syn = np.random.random_integers(1, 10, iWells)*.1

m_Data = np.array( [])
for i in range (iWells):
    if i == 0:
        m_Data = a_mu_syn[i] + a_std_syn[i]*np.random.randn(iMeas)
    else: 
        m_Data = np.vstack( (m_Data, a_mu_syn[i] + a_std_syn[i]*np.random.randn(iMeas))


#===================
# statistics
#===================
a_mean = np.dot(m_Data, np.ones(iMeas, dtype = float).reshape(iMeas, 1))/iMeas
print('syn results', np.round(a_mu_syn,2))
print('computed means', np.round(a_mean.flatten(), 2))
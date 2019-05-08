# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 08:23:57 2019

@author: maduong
"""
"""
    
    determine the crossover point between two functions
    1 - as for loop
    2 - vectorized problem using numpy
    
"""

import numpy as np
import matplotlib.pyplot as plt

#===================
#Parameters
#===================
tmin, tmax = -10, 10
iN         = 10000
f_dt       = float(tmax-tmin)/(iN-1)

#fct params
t0 = 2.5 
c  = 1.1
A  = 9
eps= 0.01

#=================
# function def
#=================
def f_t(t,c,t0):
    return c*(t-t0)**2

def g_t(t,A):
    return A*t+t0

#================
# find cross-over point
#================
##A## for loop

f_curr_t = tmin
for i in range(iN):
    f_curr_t += f_dt
    f_curr_f_t = f_t(f_curr_t, c, t0)
    f_curr_g_t = g_t(f_curr_t, A)
    #print f_curr_t, f_curr_f_t, f_curr_g_t
    #fct value comparison
    if abs(f_curr_f_t - f_curr_g_t) < eps:
        print('cross over point at t=%.2f, f(t)=%.2f, g(t)=%.2f'%(f_curr_t, f_curr_f_t, f_curr_g_t))

##B## vectorized solution
a_t = np.linspace(tmin, tmax, iN)
#evaluate fct
a_ft= f_t(a_t, c, t0)
a_gt= g_t(a_t, A)
#find cross over
sel = abs (a_ft- a_gt) < eps
print 'cross over points', a_t[sel], a_ft[sel], a_gt[sel]

#================
# plot fct
#================

plt.plot(a_t, a_ft, 'ro', ms = 2)
plt.plot(a_t, a_gt, 'go', ms = 2)
plt.show()
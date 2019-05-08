# -*- coding: utf-8 -*-
"""
Created on Mon May  6 08:30:09 2019
    - Numerical integration of defininte intergals
    ex: f(t) = 3t**2*exp(t**3)
        F(t) = exp(t**3)
            between : a, b
            with F'(t) = f(t)
        
@author: maduong
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#                              fct definition
#==============================================================================
def fct_f(t):
    return 3*t**2*np.exp(t**3)

def fct_F(t):
    return np.exp(t**3)

#################integration fct####################
def trapezoidal(fct_x, x0, xn, N):
    """
        composite trapezoidal method implementation of eq. 3.17 page 60
        in Linge and Langtengen
    Params:
        fct_x  - comp. integral of this fct.
        x0, xn - integration bounds
        N      - number of trapezoids
    Return:
        value of the defininte integral of fct_x between x0 and xn
    """
    dx = float(xn-x0)/N
    #write sum as a for loop
    f_Integ = 0.5*(fct_x(x0) +fct_x(xn))
    for i in range (1, N):
        f_Integ += fct_x( x0 + i*dx)
    ## write sum in vectorized form
    f_Integ = 0.5*(fct_x(x0) +fct_x(xn)) + (fct_x(x0+dx*np.arange(1, N, 1))).sum()
    return dx*f_Integ
    

#==============================================================================
#                              parameters
#==============================================================================
xmin, xmax = 0, 1
N          = 10

#==============================================================================
#                           num integration and plotting
#==============================================================================
# exact sol
f_IntExact = fct_F(xmax) - fct_F(xmin)

#numerical approx.
f_IntNum = trapezoidal(fct_f, xmin, xmax, N)

#compare exact and numerical 
print ('exact integral: ', f_IntExact)
print ('num. approx', f_IntNum)
for curr_n in range (10, 1000, 200):
    f_IntNum = trapezoidal(fct_f, xmin, xmax, curr_n)
    print('increment dx: ', float(xmax - xmin)/curr_n),
    print ('exact integral: ', f_IntExact),
    print ('num. approx: ', f_IntNum)  




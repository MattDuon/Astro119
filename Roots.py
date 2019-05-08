# -*- coding: utf-8 -*-
"""
Created on Wed May  1 08:55:26 2019

@author: maduong
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils

#===================================================================================
#                           fct definitions
#===================================================================================
def fct(x):
    return -x**2 + 10*x + 9
def dfdx(x):
    return -2*x + 10

def my_Newton(fct, df_dx, x0):
    """
        - implementation of Newton's method for solving f(x) = 0, when f'(x)
        is known
    """
    xn = float(x0)
    eps = 1e-5
    N = 20
    i = 0
    while abs(fct (xn)) > eps and i < N:
        x_next = xn - fct(xn)/df_dx(xn)
        print(i , 'fct_value', abs(fct(xn)), x_next)
        xn = x_next
        i += 1
    if abs(fct(xn)) < eps:
        return x_next
    else: #solution did not converge
        return np.nan 

def my_Secant( fct, x0, x1, tol = 1e-5, N = 20):
    """
        - secant method
    """
    x0 = float (x0)
    x1 = float (x1)
    i = 0
    while abs( fct(x1)) > tol and i < N:
        # numerical approx. of derivative
        dfdt = (fct(x1) - fct(x0))/(x1 - x0)
        # basically Newton
        x_next = x1 - fct(x1)/(dfdt)
        
        x0     = x1
        x1     = x_next
        print(i , 'fct_value', abs(fct(x1)), x_next)
        i += 1
    #check if solution converges
    if abs (fct(x1)) > tol:
        return np.man
    else:
        return x1
#===================================================================================
#                           Parameters
#===================================================================================
x0 = -9
# independent variable range
xmin, xmax = -10, 15

#===================================================================================
#                           find roots
#===================================================================================
x_root = my_Newton( fct, dfdx, x0)
x_rootSc = my_Secant( fct, x0, x0+10, tol = 1e-2, N = 100)
#===================================================================================
#                           plots
#===================================================================================
a_x = np.linspace(xmin, xmax, 1000)
plt.figure(1)
plt.plot(a_x, fct(a_x), 'k-')
plt.plot( [x_root], [fct(x_root)], 'r*' , ms = 14)
plt.plot([x_rootSc], [fct(x_rootSc)], 'b*', ms = 10)
plt.plot([xmin, xmax], [0,0], 'r--')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('fct values')
plt.show()
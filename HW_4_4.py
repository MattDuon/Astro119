# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:24:25 2019
    - Solves for the roots of various functions using the Secant method.
    
@author: maduong
"""

from __future__ import division # need this for division 
import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils

#===================================================================================
#                           Parameters
#===================================================================================
xmin, xmax = -10, 10 # range of x for functions 1 and 2
xcmin, xcmax = -3, 3 # range of x for function 3
x0 = 1 # guess for x

#===================================================================================
#                           Fct Definitions
#===================================================================================
def f1(x):                            # all functions defined
    return -(x**5) + (x**2)/3 + (1/2)
def f2(x):
    return (np.cos(x))**2 + .1
def f3(x):
    return np.sin(x/3) + .1*(x+5)

#===================================================================================
#                           find roots
#===================================================================================
# root calculation, set tol to 1e-6 for more precise results
x_root1 = opt_utils.my_Secant( f1, x0, x0+10, tol = 1e-6, N = 20)
x_root2 = opt_utils.my_Secant( f2, x0, x0+10, tol = 1e-6, N = 20)
x_root3 = opt_utils.my_Secant( f3, x0, x0+10, tol = 1e-6, N = 20)

print 'root of f1(x):', x_root1
print 'root of f2(x): none' # x_root2 does not exist
print 'root of f3(x):', x_root3
#===================================================================================
#                           plots
#===================================================================================
#These plots are here to help see what is a good x0 guess.
a_x = np.linspace(xmin, xmax, 1000) 
plt.figure(1)
ax = plt.subplot(311)
ax.plot(a_x, f1(a_x), 'k-')
plt.plot([xmin, xmax], [0,0], 'r--')
bx = plt.subplot(312)
plt.plot(a_x, f2(a_x), 'b-')
plt.plot([xmin, xmax], [0,0], 'r--')
cx = plt.subplot(313)
c_x = np.linspace(xcmin, xcmax, 1000)
cx.plot(c_x, f3(a_x), 'r-')
plt.plot([xmin, xmax], [0,0], 'r--')
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:18:52 2019
    1. Solves for the crossover point(s) of two defined functions. 
    2. Plots out both functions, their difference and the crossover point(s).
    
@author: maduong
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils

#===================================================================================
#                           Parameters
#===================================================================================
t0 = 2.5 # First guess
t1 = 9.1 # Second guess
c = 1.1
A = 5
tmin, tmax = -10, 10

#===================================================================================
#                           Fct Definitions
#===================================================================================
def f(t):                     # all functiosn and their derivatives defined
    return c*(t-t0)**2
def dfdt(t):
    return 2*c*(t-t0)
def g(t):
    return A*t+t0
def dgdt(t):
    return A
def h(t):
    return f(t) - g(t)
def dhdt(t):
    return dfdt(t) - dgdt(t)

#===================================================================================
#                           find roots
#===================================================================================
t_root = opt_utils.my_Newton( h, dhdt, t0)
t_root1 = opt_utils.my_Newton( h, dhdt, t1)
print ('First t value', t_root, 'First f(t) and g(t) value', f(t_root))
print ('Second t value', t_root1, 'Second f(t) and g(t) value', f(t_root1))
# values for t, g(t), and f(t) of both crossover points. Note that g(t) and fIt) should be the same

#===================================================================================
#                           plots
#===================================================================================
a_t = np.linspace(tmin, tmax, 1000) # x axis
plt.figure(1)
plt.plot(a_t, f(a_t), 'k-')
plt.plot(a_t, g(a_t), 'b-')
# There are two crossover points

plt.plot( [t_root], [f(t_root)], 'r*' , ms = 14) # first crossover point
plt.plot([t_root], [g(t_root)], 'y*', ms = 10)
plt.plot( [t_root1], [f(t_root1)], 'g*' , ms = 14) # second crossover point
plt.plot([t_root1], [g(t_root1)], 'k*', ms = 10)
plt.figure(2)
plt.plot(a_t, h(a_t), 'k-')        # h(t) plot for part c
plt.plot( [t_root], [h(t_root)], 'r*', ms = 14) # first crossover point
plt.grid(True)
plt.show()
# when plotting h(t) and letting it overlap with the plot from InC_2_1,
# the same crossover point in both plots do not overlap 




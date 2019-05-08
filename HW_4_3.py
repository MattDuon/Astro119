# -*- coding: utf-8 -*-
"""
Created on Sat May  4 13:35:08 2019
    - A new function, "my_Newton", that solves for a root depending on how small
    the difference between the current and last fct value is, rather than how small
    the fct value, itself, is.
    
author: maduong
"""

import numpy as np

#===================================================================================
#                           Fct Definitions
#===================================================================================
def my_Newton(fct, df_dx, x0):
    """
        - implementation of Newton's method for solving f(x) = 0, when f'(x)
        is known
    """
    xn = float(x0)
    eps = 1e-6
    N = 20
    i = 1
    x_next = xn - fct(xn)/df_dx(xn) 
    # solved for the very first x_next term in order to define while loop
    print(0 , 'fct_(x_next) -', abs(fct(x_next) - fct(xn)), x_next) 
    # printed out first set of values
    while abs(fct(x_next) - fct(xn)) > eps and i < N:
        xn = x_next # sets the first x_next term defined earlier to the new xn
        x_next = xn - fct(xn)/df_dx(xn) # solved for new x_next
        print(i , 'fct_(x_next) -', abs(fct(x_next) - fct(xn)), x_next)
        i += 1
    if abs(fct(x_next) - fct(xn)) < eps: 
        # now the loop stops if the difference of the fct values is less than eps
        return x_next
    else: #solution did not converge
        return np.nan 

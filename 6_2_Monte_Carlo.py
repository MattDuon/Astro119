# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:24:05 2019

@author: maduong
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#                              fct definition
#==============================================================================
def fct_xy(x, y):
    return x*y**2

def fct_gxy(x, y):
    """
    - rectangular domain
    return -1 for points outside
    
    """
    f_retVal = -1
    if x > xmin and x <= xmax and y >= ymin and y <= ymax:
        f_relVal = 1
    return f_retVal


#==============================================================================
#                              parameters
#==============================================================================


#==============================================================================
#                              compute integral
#==============================================================================
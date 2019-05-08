# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:28:49 2019

@author: maduong
"""

import numpy as np

## coefficient matrix, A
mA= np.array( [[3,1],
               [1,2]])
#solution vector
a_b=np.array([9,8])


#solve for A-1 dot b
a_x = np.dot(np.linalg.inv(mA),a_b)
print(a_x)
a_x2= np.linalg.solve(mA, a_b)
print(a_x2)

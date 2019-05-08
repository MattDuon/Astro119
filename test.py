# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 09:16:00 2019

@author: maduong
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils
np.random.seed(12345)

#===================================================================================
#                         params, dirs, files
#=================================================================================== 
xmin, xmax = 0, 5
N          = 20
f_a        = 5.0
f_b        =-2.4
f_sigma    = .5 
#===================================================================================
#                         synthetic data
#===================================================================================
a_x = np.linspace(xmin, xmax, N)
a_y = f_b*a_x + f_a + np.random.randn(N)*f_sigma

#===================================================================================
#                         lin. LS. and plot
#===================================================================================
dLS = opt_utils.lin_LS(a_x, a_y)

plt.figure()
plt.title (str(dLS['R2']))
ax1 = plt.subplot(111)
ax1.plot(a_x, a_y, 'ko' , ms = 5, mew = 1.5, mfc = 'none' , label = 'obs.')
ax1.plot(a_x, dLS ['Y_hat'], 'r-', label = 'Model')
ax1.legend(loc = 'upper right')
plt.show()
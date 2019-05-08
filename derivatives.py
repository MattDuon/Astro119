# -*- coding: utf-8 -*-
"""
Created on Wed May  1 08:07:16 2019

@author: maduong
"""

import numpy as np
import matplotlib.pyplot as plt
import opt_utils as opt_utils

#===================================================================================
#                           Parameters
#===================================================================================
dt = .001 # time increment
a_t = np.arange(-np.pi, np.pi + dt, dt)

#fct to take derivative of 
a_sin = np.sin(a_t)

#===================================================================================
#                           derivatives
#===================================================================================
#exact solution
dfdt_exact = np.cos(a_t)

#numerical approximation
##A## - FD
#dfdt_FD = (np.sin(a_t+dt) - np.sin(a_t))/dt
#dt = a_t[1] - a_t[0]
dfdt_FD = (a_sin[1::] - a_sin[0:-1])/dt
##B## - BD
dfdt_BD = (np.sin(a_t) - np.sin(a_t - dt))/dt
#dfdt_BD = 

##C## - CD
#dfdt_CD = (np.sin(a_t + dt) - np.sin(a_t - dt))/(2*dt)
dfdt_CD = (a_sin[2::] - a_sin[0:-2])/(2*dt)
#===================================================================================
#                           plots
#===================================================================================
plt.figure(1)
ax = plt.subplot(111)
ax.plot(a_t, a_sin, '-', alpha = .5, lw = 2)
#derivatives
ax.plot(a_t, dfdt_exact, 'r--', label = "f'(t)-exact")
ax.plot(a_t[0:-1], dfdt_FD, 'g', label ="f(t) - FD")
ax.plot(a_t, dfdt_BD, 'b', label = "f'(t) - BD")
ax.plot(a_t[1:-1], dfdt_CD, 'y', label = "f'(t) - CD")
ax.legend (loc = 'upper left')
ax.grid(True)

plt.show()

# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:36:56 2019
    - Solves the velocity and acceleration of several data points using the 
    central difference approach. Plots out position, velocity, and acceleration
    in terms of time.

@author: maduong
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#===================================================================================
#                           Parameters and Files
#===================================================================================
file_in = 'HW4_vertTraj.txt'
file_out = 'HW4_5_plots'

#===================================================================================
#                           Load Data
#===================================================================================
mData = np.genfromtxt(file_in).T
dt = mData[0][2::] - mData[0][0:-2] # dt is the time interval based on the data in this case
# dt already has the 2 multipled in for the central difference approach

#===================================================================================
#                           derivatives
#===================================================================================
# Calculation for velocity, velocity will have two less values than position
v = (mData[1][2::] - mData[1][0:-2])/dt
# Calculation for accleration, will have two less values than velocity
a = (v[2::] - v[0:-2])/dt[1:-1]
 
#===================================================================================
#                           Plots
#===================================================================================
plt.figure(1)                     # all plots in rows on top of each other
px = plt.subplot(311)
# position plot should look like an upside down parabola
px.plot(mData[0], mData[1], 'k-')
px.set_ylabel('Position')
px.set_xlabel('Time')

pv = plt.subplot(312)
# velocity should be a negative slope
pv.plot(mData[0][1:-1], v, 'b-')
pv.set_ylabel('Velocity')
pv.set_xlabel('Time')

pa = plt.subplot(313)
# acceleration should be constant and -9.8 in theory 
pa.plot(mData[0][2:-2], a, 'r-') 
pa.set_ylabel('Acceleration')
pa.set_xlabel('Time')

plt.savefig(file_out)
plt.show()
# data seems to come from something like throwing a ball up and timing it's position.

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 08:23:24 2019

@author: maduong
"""

import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
#                         Files and Variables
#==============================================================================
file_in = 'exoplanet_transit.csv'

r_earth = 6378 
r_s = 80000 #[km]
Np  = 3
#==============================================================================
#                         Load Data
#==============================================================================
mData = np.loadtxt(file_in, delimiter = ',', skiprows = 1).T
N     = len(mData[0])
lenPer= int(float(N)/Np)
#compute difference between subsequent samples
aDiff = mData[1][1::] - mData[1][0:-1] 
#print(mData)
#print(mData[0][0:10])
#print(mData[1][0:10])

#==============================================================================
#                         Compute depth of transit
#==============================================================================
aDepth = np.zeros(Np)
for i in range (Np):
    #create index vector
    aID = np.arange(lenPer) + lenPer*i
    selMin = aDiff[aID] == aDiff[aID].min()
    selMax = aDiff[aID] == aDiff[aID].max()
    
    iID_min = aID[selMin][0]
    iID_max = aID[selMax][0]
    
    #compute mean depth of transit (for each period) 
    aDepth[i] = 1 - mData[1, iID_min:iID_max].mean()
    
##compute the size of the planet
aR_p = np.sqrt(aDepth)*r_s
print(aR_p)
print ('Size relative to earth', aR_p/r_earth)
#==============================================================================
#                         Plotting
#==============================================================================
plt.figure(1)
plt.subplot(211)
plt.plot(mData[0], mData[1], 'ko', ms = 2)
plt.xlabel('Transit Time [hr]')
plt.ylabel('Brightness')
plt.show()

plt.subplot(212)
plt.plot(mData[0][0:-1], aDiff, 'ro', ms = 2)
plt.xlabel ('Transit Time [hr]')
plt.ylabel ('Brightness Diff')
plt.show()
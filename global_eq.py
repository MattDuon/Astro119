# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:56:16 2019

@author: maduong
"""
"""
    animation of global earthquake locations from 2000 to 2019
    -plotted annually
    
"""

import numpy as np
import matplotlib.pyplot as plt

#=========================================================
#                  files and Parameters
#=========================================================
file_eq = 'globalEqs.txt'

#=========================================================
#                  Load Data
#=========================================================
aYr = np.genfromtxt(file_eq, skip_header = 1, usecols = (0), delimiter = '-',
                   dtype = int)
print(np.unique(aYr))
mLoc = np.genfromtxt(file_eq, skip_header = 1, delimiter =',', use_cols=(2,1),
                     dtype = float).T
#=========================================================
#                  PLot eq map using basemap
#=========================================================
for it in np.unique(aYr):
    sel_eq = it ==aYr
    print( 'no of eqs. in %i: %i'%(it, sel_eq.sum()))
    
    plt.figure(1, figsize = (16,14))
    plt.title(str(it))
    
    m = Basemap()
    m.drawcoastlines()
    
    a_X, a_Y = m(mLoc[0][sel_eq], mLoc[1][sel_eq])
    
    #plt.plot(a_X, a_Y, 'ro', ms = 5, mew =1.5, mfc = 'none')
    plt.scatter(a_x, a_y, c = mLoc[2][sel_eq], s- np.exp(mLoc[2][sel_eq]-3))
    cbar = plot.colorbar (plot1, orientation = 'horizontal' )
    cbar.set_label('Magnitude')    
    plt.pause(1.5)
    
    plt.clf()
#!/bin/python2.7
"""

--> 1) load ANSS seismicity data and well locations for Oklahoma
--> 2) plots eq rates and cumulative number
--> 3) plot eq locations and wells in map view in moving 6 months time windows

"""
from __future__ import division
import os
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

#------------my modules-----------------------
import seis_utils as seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'


dPar  =  {  'showRate'  : True,
            'dt_map'    : 6./12, # time step for plotting eq and wells in map view

             # for rate computations
             'k'         : 200,
             'dt_hist'   : 1./12, # bin spacing for histogram of earthquake rates
             'tmin'      : 2005, # play with this number to visualize historic rates
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'merc',# or 'aea' for equal area projections
           }

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt(file_eq).T
aTime  = seis_utils.dateTime2decYr( mSeis[1], mSeis[2], mSeis[3], mSeis[4], mSeis[5],mSeis[6])

mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt(file_well).T
#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------
# plot rate and cumulative number
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    at_den, a_rate = seis_utils.eqRate( aTime, dPar['k'])
    ax.plot( at_den, a_rate/12, 'b-', lw = 2, alpha = .5)
    ax.set_ylabel( 'Earthquake Rate [ev/mo]')
    ax2 = plt.subplot( 212)
    ax2.plot( sorted( mSeis[0]), np.cumsum( np.ones( mSeis[0].shape[0])), 'r--')
    ax2.set_xlabel( 'Time [dec. yr]')
    ax2.set_ylabel('Cumulative Number')
    ax2.set_xlim( ax.get_xlim())
    plt.show()

#--------------------------3---------------------------------------------
#                       map view of well and event locations
#------------------------------------------------------------------------
# create time vector with dt_map spacing
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    # select wells with start dates before t1
    sel_we =  mWells[1] < t1
    print t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum()
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                resolution = 'l',
                projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)
    m.drawstates( linewidth = 1.5)
    aX_eq, aY_eq = m(  mSeis[1][sel_eq], mSeis[2][sel_eq])
    aX_we, aY_we = m( mWells[2][sel_we], mWells[3][sel_we])

    m.plot(  aX_we, aY_we, 'bv', ms = 2, mew = 1.5, mfc = 'none', alpha = .6)
    m.plot(  aX_eq, aY_eq, 'ro', ms = 6, mew = 1.5, mfc = 'none')

    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------
    plt.pause(.5)















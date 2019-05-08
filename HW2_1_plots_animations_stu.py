#!/bin/python2.7
"""

--> 1) load ANSS seismicity data and well locations for Oklahoma
--> 2) plot eq rates
--> 3) plot cumulative rate
--> 4) seismicity and well map in moving time windows


@author: maduong
"""

from __future__ import division
import matplotlib.pyplot as plt
#from matplotlib
import numpy as np

from mpl_toolkits.basemap import Basemap

#------------my modules-----------------------

#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'


dPar  =  {  'showRate'  : True,
            'dt_map'    : 6./12, # time step for plotting eq and wells in map view

             # for rate computations
             'k_win'         : 200,

             'tmin'      : 2005, # play with this number to visualize historic rates
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'merc',# or 'aea' for equal area projections
           }
nDays = 365.25
#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq, comments = '#').T
aYr  = np.genfromtxt(file_eq, usecols=(1,2,3,4,5,6), dtype = float).T
#TODO: convert date-time to decimal year use seis_utils.dateTime2decYr
aTime = aYr[0,:]+(aYr[1,:]-1)/12 + (aYr[2,:]-1)/nDays + (aYr[3,:]/(nDays*24)) + (aYr[4,:]/(nDays*24*60)) + (aYr[5,:]/(nDays*24*3600))
#YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)

mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
mWells = np.loadtxt( file_well).T
#--------------------------2---------------------------------------------
#                  earthquake rates, cumulative number
#------------------------------------------------------------------------


# plot rate and cumulative number of events
if dPar['showRate'] == True:
    plt.figure(1)
    ax = plt.subplot( 211)
    # compute seismicity rates using seis_utils.eqRate
    def eqRate( at, k_win):
        # smoothed rate from overlapping sample windows normalized by delta_t
        aS          = np.arange( 0, at.shape[0]-dPar['k_win'], 1)
        aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
        iS = 0
        for s in aS:
            i1, i2 = s, s+k_win
            aBin[iS]  = 0.5*( at[i1]+at[i2])
            aRate[iS] = dPar['k_win']/( at[i2]-at[i1])
        iS += 1
        return (aBin, aRate)
        #TODO: plot seismicity rates
        ax.plot( aBin, aRate, 'r-')
        ax.set_xlabel( 'Time [dec. yr]')
        ax.set_ylabel( 'Earthquake Rate [ev/mo]')

ax1 = plt.subplot( 212)
#TODO: plot cumulative number of earthquakes
N = np.shape(aTime)
Num_Earth = np.cumsum(np.ones(N))
ax1.plot(aTime, Num_Earth, 'g-')
ax1.set_xlabel( 'Time [dec. yr]')
ax1.set_ylabel('Cumulative Number')
ax1.set_xlim( ax.get_xlim())
plt.show()

#--------------------------3---------------------------------------------
#                       map view of well and event locations
#------------------------------------------------------------------------
# create time vector with dt_map spacing
at_bin  = np.arange( dPar['tmin'], 2018, dPar['dt_map'])
for i in range( at_bin.shape[0]-1):
    t1, t2 = at_bin[i], at_bin[i+1]
    #TODO: select earthquakes between t1 and t2 use np.logical_and
    sel_eq = np.logical_and( mSeis[0]  >= t1, mSeis[0]   < t2)
    #TODO: select wells with start dates before t1
    sel_we = np.logical_and(mWells[0] <= t1, mWells[0] > 0)
    print t1, t2, 'No. earthquakes', sel_eq.sum(), 'No. of wells', sel_we.sum()
    ### create basemap object
    plt.figure(2)
    plt.cla()
    ax2 = plt.subplot(111)
    lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
    m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
                llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
                lon_0 = lon_0, lat_0 = lat_0,
                resolution = 'l',
                projection=dPar['projection'], )
    #TODO: draw state boundaries
    m.drawstates()

    #TODO: convert spherical to 2D coordinate system using basemap
    xpt,ypt = m(lon_0,lat_0)

    # TODO: plot seismicity and well locations
    plot1 = plt.scatter()
    plot2 = plt.scatter()
    
    # x and y labels
    m.drawparallels( np.arange( 33,   38,  1), fmt='%i',labels=[1,0,0,0])
    m.drawmeridians( np.arange(-100,  -92, 2), fmt='%i',labels=[0,0,0,1])
    #--------------

    #file_out = 'OK_seis_t_%.1f_%.1f.png'%( t1, t2)
    #plt.savefig(  file_out, dpi = 150)
    #plt.clf()

    plt.pause( .5)















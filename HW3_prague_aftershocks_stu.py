#!/bin/python2.7
"""

--> 1) load ANSS (or comcat) seismicity data using np.genfromtxt
--> 2) create time vector in days
--> 3) select events within area of interest
--> 4) compute aftershock decay rates and power-law fit

Note to students: If you use the template go through the code
                    line-by-line and comment-out the potion of
                    the code you are not working on

"""
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
#------------my modules-----------------------
import seis_utils as seis_utils
import opt_utils as opt_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
file_in  = 'prague_aftershock_clean.txt'

dPar  =  { 'k'    : 5, # TODO: change this parameter to see how fit and R2 will changes
           'MSmag': 5.7, #for a specific MS event having the event ID would be better, but MAG works here
           #TODO: change tmin and tmax
           #note - theoretically you would have to plot the data first and find the time window over which
           #       the data can be described by a powerlaw
           #  time range for PL fit
           'tmin'  : 1, 'tmax' : 100,
           'testPlot' : True, # set to False after initial debugging
           }

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
#TODO:  - find the correct data columns to import here (date-time, magnitde and location i.e. lon and lat)
mData   = np.genfromtxt(file_in, usecols=(0,1,2,3,4,5,6,7,8,9), skip_header = 2).T
print( 'total no. of eqs.', mData[0].shape[0])

#--------------------------2---------------------------------------------
#                  initial processing steps
#------------------------------------------------------------------------
#TODO: compute max. distance from mainshock for aftershock selection, this is the eq. at the top of page 3
dPar['rmax'] = ???
#A# select events within certain radius from MS
MS_ID = np.arange( mData[0].shape[0])[mData[9] == dPar['MSmag']][0]
#TODO:  compute the distance from mainshock to each event using: seis_utils.haversine (or a basemap equal-distance projection)
aR    = seis_utils.haversine(-97.1850, 35.6350, mData[7], mData[6])
#TODO: select events within rmax, i.e. dPar['rmax']
selR  = ???
print( 'maximum radius', dPar['rmax'], 'N  events within r_max: ', selR.sum(), 'N events outside of Rmax', (1-selR).sum())
mData = mData.T[selR].T


#B# update mainshock ID for smaller data-set
MS_ID = np.arange( mData[0].shape[0])[mData[9] == dPar['MSmag']]

#C# TODO: create time vector in units of days
at_days = mData[0]*365.25 + ??? + mData[2]  + mData[3]/24 + ??? + ???


#D# TODO: temporal decay rates, dN/dt see eq. page 3 of the assignment
at_bin, aN_bin = ???

if dPar['testPlot'] == True:
    # it is a good idea to create a test plot here for debugging purposes
    # if everything is done correctly you should see the events before the M5.7 Prague earthquake in balck
    # and all aftershocks in red
    # this plot is for debugging purposes and does not have to be handed in
    plt.figure()
    ax = plt.subplot( 111)
    ax.semilogy( at_bin/365.25, aN_bin, 'ko', label = 'all events')
    at_bin_tmp, aN_bin_tmp   = seis_utils.eqRate( at_days[MS_ID::], dPar['k'])
    ax.semilogy( at_bin_tmp/365.25, aN_bin_tmp , 'ro', mec= 'r', mew = 1.5, label = 'Aftershocks')
    ax.legend( loc = 'upper left')
    ax.set_xlabel( 'Time [dec. year]')
    ax.set_ylabel( 'events/day')
    plt.show()

#--------------------------3---------------------------------------------
#                    power-law fitting
#------------------------------------------------------------------------
# TODO: subtract time of mainshock (at_days[MS_ID]) from aftershock times (at_days[MS_ID+1??]- replace ??) - new vector has only AS with time relative to MS in days
at_AS = ???
# TODO: compute AS rates
at_bin_AS, aN_bin_AS   = ???
# select events within tmin and tmax for which the data can be described by a powerlaw
sel_t = np.logical_and( at_bin_AS >= dPar['tmin'], at_bin_AS <= dPar['tmax'])
# TODO: fot the powerlaw to the log-transformed data between tmin and tmax
dPL = opt_utils.lin_LS( ???, ???)
p_omori = dPL['b']
print 'Omori p-value: ', p_omori
#TODO: use dN/dt = alpha*t**(-p) to compute the modeled rates
aOmori_rate = 10**( np.log10( at_bin_AS)*p_omori + dPL['a'])

#--------------------------4---------------------------------------------
#                    plots
#------------------------------------------------------------------------
plt.figure()
ax = plt.subplot()

# note: careful with the different time vectors during plotting
# we have at_AS     - aftershock times in days after mainshock
#         at_bin_AS - binned time vector for rate computation, this vector is smaller than at_AS
#         at_days   - origin times of all events in days (we won't be using this one anymore)
# :TODO  plot observed aftershock decay rate
ax.loglog( ????, ???, 'ko', mfc = 'none', mew = 1.5, label = 'aftershocks, $N_{tot}$=%i'%( at_AS.shape[0]))
# :TODO plot modeled rates based on Omori law
????

ax.legend( loc = 'upper right')
# TODO: add the correct units for the time vector
ax.set_xlabel( 'Time [???]')
ax.set_ylabel( 'events/???')
# TODO: save the file make sure to include labels and the legend including the inverted p-value
plt.savefig( ????)
plt.show()











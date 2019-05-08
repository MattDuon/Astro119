# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:15:00 2019

@author: maduong
"""
"""
    Compute temporal earthquake rate change for KTB fluid injection 
    experiment
"""
import numpy as np
import matplotlib.pyplot as plt

#=========================================================
#                   FCT. Def
#=========================================================
def comp_rate(a_t, k):
    """
    -compute rate change for time vector a_t
    :input
            a_t - time vector
            k   - sample window - controls smoothness
    :output a_bin, a_rate
    """
    aS  = np.arange( 0, a_t.shape[0]-k, 1)
    a_bin = np.zeros( aS.shape[0])
    a_rate = np.zeros( aS.shape[0])
    iS = 0 
    for s_step in aS:
        i1, i2    = s_step, s_step+k
        a_rate[iS] = k/(a_t[i2] - a_t[i1])
        a_bin[iS] = 0.5*(a_t[i1] +a_t[i2])        
        iS += 1
    return a_bin, a_rate

#=========================================================
#                  parmas and files
#=========================================================
file_in = 'data/KTB_inject.txt'
file_eq = 'data/KTB_mag.txt'

#sample window
k_win   = 10

t0      = float() #starting time for plotting 
aT_eq   = np.array([]) #timing of earthquakes
aMag    = np.array([])

aT_inj  = np.array([])
aV      = np.array([])

#=========================================================
#                  Load data and comp. rates
#=========================================================
mData = np.loadtxt(file_eq).T
aT_eq = mData[0]
aMag  = mData[1]

mData = np.loadtxt(file_in).T
aT_inj= mData[0]
aV    = mData[1]

sel   = aV > 0
aV    = aV[sel]
aT_inj= aT_inj[sel]

#shift time vectors and change to hr
t0    = aT_inj[0]
aT_inj-= t0
aT_eq -= t0 
aT_inj = aT_inj/3600
aT_eq  = aT_eq/3600
###compute eq rates
a_tbin, a_rate = comp_rate(aT_eq, k_win)

#=========================================================
#                  Plots
#=========================================================
###test plot magnitudes
fig1=plt.figure(1, figsize =(14,16))
ax1 = plt.subplot(211)
ax1.plot (aT_inj, aV, '-b')
ax1.set_ylabel('Cumul. Inj. Rate [m3]')
ax2 = plt.subplot(212)
twinx2= ax1.twinx()
ax2.plot (a_tbin, a_rate, 'r-')
#plot comululative eq number
twinx2.plot(sorted(aT.eq), np.cumsum(np.ones(aT_eq.shape[0])))
ax2.set_xlim(ax1.get_xlim())
ax2.set_xlim( 'Time [hr]')
ax2.set_ylabel( 'Eq. Rate [ev/hr]')
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:09:47 2019

@author: maduong
"""

import numpy as np
import os

#==============================================================================
#                         Create ex data
#==============================================================================
file_out = 'dataIO_ex.txt'

N = 10
aX= np.arange(N)
aY= aX**2

#==============================================================================
#                         methods to load and save data
#==============================================================================
print( os.getcwd())
np.savetxt(file_out, np.array([aX, aY]).T, fmt='%4.0f%4.0f', header = 'X    x^2')

mData = np.loadtxt(file_out).T
print(mData) 

#reads file line by line
with open(file_out, 'r') as file_obj:
    file_obj.next()
    for line in file_obj:
        lStr = line.split(' ')
        print( lStr)
        for my_str in lStr:
            print ( int( float( my_str)))
            
#read and write binary 
import scipy.io
scipy.io.savemat(file_out.replace('txt', 'mat'), 
                 { 'X' :aX, 'Y' :aY })

dicData = scipy.io.loadmaxt(file_out.replace('txt', 'mat'))
print(dicData)
        
        
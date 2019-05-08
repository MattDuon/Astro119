#python2.7
"""
Created on Sat April 13, 2019

    This script does the following:
        Solve for the area of an irrgular polygon using vector notation.
        
@author: maduong
"""

import numpy as np

#================================================================
#                         Parameters
#================================================================
x0 = np.array([1,3,4,3.5,2]) 
y0 = np.array([1,2,5,4,1])
y1 = np.array([1,1,2,5,4])
x1 = np.array([3,4,3.5,2,1])
#Defined four sets of arrays based on the formula given

#================================================================
#                         Define function and Computation
#================================================================
X = x0*y0     #Set up various algebraic expressions into variables 
Y = y1*x1     #Multiple arrays together to get each term before addition
Z1 = np.sum(X) #add terms together for the first set of terms "X"
Z2 = np.sum(Y) #add terms togerther for the second set of terms "Y"
A = .5*(Z1-Z2) #apply results to given function to find the area
print ('Area of the polygon', A)
#python2.7
"""
Created on Sun April 14, 2019

    This script does the following:
        Solve for the value of b that gives the biggest area of a rectangle 
        inscribed by a circle.
        
@author: maduong
"""

import math as m

#================================================================
#                         Parameters
#================================================================
r = 12.6 #radius of a circle 
a = 1.5  #length of one side of a rectangle
b = 1    #starting b values at 1
#all values are in milimeters

#================================================================
#                         Define functions
#================================================================
R_area = a*b       #defined equation of a rectangle
C_area = m.pi*r**2 #defined the equation of a circle

#================================================================
#                         Computation
#================================================================
while b < 400:                 
    print b
    if (a*b > m.pi*r**2):
        break
    b += .1
    #will print out b values until R_area > C_area
#the answer is the second to last term, in this case, the value is 332.5
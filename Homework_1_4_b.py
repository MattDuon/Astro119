#python2.7
"""
Created on Sun April 14, 2019

    This script does the following:
        Solve for the fractional amount of Carbon-14 after 10kyr, 100kyr, and 
        1Myr.
        
@author: maduong
"""

import math as m

#================================================================
#                         Parameters
#================================================================
t1 = 10**4 #3 separate time values
t2 = 10**5
t3 = 10**6
tao = 5730 #halflife
#all values are in years

#================================================================
#                         Define function
#================================================================
N1 = m.e**(-t1/tao) #three separate equations defined
N2 = m.e**(-t2/tao)
N3 = m.e**(-t3/tao)
print ('fraction after 10kyr', N1) #a string with printed value
print ('fraction after 100kyr', N2)
print ('fraction after 1Myr', N3)
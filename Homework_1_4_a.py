#python2.7
"""
Created on Sun April 14, 2019

    This script does the following:
        Solve for the remaining amount of an element after a given time,
        halflife, and initial amount.
        
@author: maduong
"""

import math as m

#================================================================
#                         Parameters
#================================================================
N0 = float(raw_input('What is initial amount?'))
t = float(raw_input('What is the time?'))
tao = float(raw_input('What is the halflife?'))

#================================================================
#                         Define function
#================================================================
N = N0*m.e**(-t/tao)  #Given function
if N0 == 0:           #Condition if N0 is not given (equals zero) 
    N = m.e**(-t/tao)
print N               #Print N value
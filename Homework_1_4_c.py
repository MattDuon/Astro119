#python2.7
"""
Created on Sun April 14, 2019

    This script does the following:
        Solve for the remaining amount of an element after a given time and
        halflife.
        
@author: maduong
"""

import math as m

#================================================================
#                         Parameters
#================================================================
t = float(raw_input('What is the time?'))
tao = float(raw_input('What is the halflife?'))

#================================================================
#                         Define function, Computation, and Print
#================================================================
N = m.e**(-t/tao)  #Given function
print N            #Print N value


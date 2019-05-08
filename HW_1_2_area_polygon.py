#python2.7
"""
Created on Sat April 13, 2019

    This script does the following:
        Solve for the area of an irrgular polygon using for loops.
        
@author: maduong
"""

#==============================================================================
#                         Parameters
#==============================================================================
x = [1,3,4,3.5,2]
y = [1,1,2,5,4]
#inputs set up as a list

#==============================================================================
#                         Define functions
#==============================================================================
def X(x,y):
    for i in range(5):
       B = x[i-5]*y[i-4]+x[i-4]*y[i-3]+x[i-3]*y[i-2]+x[i-2]*y[i-1]+x[i-1]*y[i]
    return B
#the first set of terms added together and defined
def Y(x,y):
    for i in range(5):
        C = y[i-5]*x[i-4]+y[i-4]*x[i-3]+y[i-3]*x[i-2]+y[i-2]*x[i-1]+y[i-1]*x[i]
    return C
#the second set of terms added together and defined
A=.5*abs((X(x,y)-Y(x,y))) #the given equation for the area

#==============================================================================
#                         Print
#==============================================================================
print ('Area of the polygon', A)
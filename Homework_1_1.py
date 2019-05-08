#python2.7
"""
Created on Sat April 13, 2019

    This script does the following:
        Solve for the area of a rectangle 
        Solve for the area of a triangle
        
@author: maduong
"""

#================================================================
#                         Parameters
#================================================================
b = float(raw_input('What is the width of the triangle or rectangle?'))
c = float(raw_input('What is the height of the rectangle?'))
h = float(raw_input('What is the height of the triangle?'))
#Type in the values you want to put in for the functions

#================================================================
#                         Define functions
#================================================================
Rect_area = b*c   #This will solve for the area of a rectangle
Tri_area = .5*h*b #This will solve for the area of a triangle

#================================================================
#                         Computation and Print
#================================================================
print('Area of Rectangle', Rect_area) #Will type out area of the rectangle
print('Area of Triangle', Tri_area)  #Will type out area af the triangle
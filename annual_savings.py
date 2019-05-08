# -*- coding: utf-8 -*-
# anaconda2/python2.7
"""
- compute annual dollar amount on savings invested at 
10% over 30 years 
variables:
    i_Years = durations of investment
    f_interest = interest rate
    f_iniInvest = initial investment
"""
#import numpy, don't actually need it here

#======================================
#define variables
#======================================
i_Years = 30
f_interest = 0.1
f_iniInvest = 1e4

#======================================
#do computation - savings
#======================================
def annual_return(f_iniInvest, f_interest, i_Years):
    """
    -computing annual savings
    :input
        variables:
            i_Years = durations of investment
            f_interest = interest rate
            f_iniInvest = initial investment
    :output
        savings in last year (i_Years)
    """
    currInvest = f_iniInvest
    for i in range (i_Years):
        print ('Year', i+1, 'savings', currInvest, 'interest per year', 'fGrowth')
        fGrowth = currInvest*f_interest
        currInvest += fGrowth
    return currInvest
# add a function call
print (annual_return(f_iniInvest, f_interest, i_Years))

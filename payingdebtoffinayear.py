# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:53:55 2018

@author: leder
"""

balance = 999999
annualInterestRate = 0.18
monthlyPaymentRate = 0.04



def getBalanceinr(b0, r, p, m):
    i = 1
    while i <= m:
        ub = b0 - (b0*p)
        b0 = ub + (r/12)*ub
        i += 1
    return round(b0,2)

def getLowestPayment(b0, r, m = 12):
    balance = b0
    test = 0 
    while b0 > 0:
        b0 = balance
        test += 10        
        i = 1
        while i <= m:
            ub = b0 - test
            b0 = ub + ((r/12)*ub)
            i += 1
    return test

def getLowestPaymentbisector(b0, r, m = 12):
    balance = b0
    high = (b0 * ((1 + (r/12))**12))/12
    low = b0/12
    while abs(b0) > 0.01:
        b0 = balance
        test = (high + low)/2     
        i = 1
        while i <= m:
            ub = b0 - test
            b0 = ub + ((r/12)*ub)
            i += 1
        if b0 < 0:
            high = test
        else:
            low = test
    return round(test,2)
        
print('Original Balance: ', balance)  
print('Interest Rate: ', annualInterestRate)  
print('Monthly Interest Rate: ', annualInterestRate/12)
print('Remaining balance (if you paid the minimum monthly payment): ', getBalanceinr(balance,annualInterestRate,monthlyPaymentRate, 12))
print('Lowest payment to pay it off in a year (to the $10): ', getLowestPayment(balance, annualInterestRate))
print('Lowest payment to pay it off in a year (to the cent): ', getLowestPaymentbisector(balance, annualInterestRate))
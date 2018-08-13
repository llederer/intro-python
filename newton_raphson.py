# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:12:36 2018

@author: leder
"""
#Newton-Raphson Algorithm for Finding Roots

epsilon = 0.01
y = float(input('Enter a number to find the approximate square root: '))
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y)/(2 * guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
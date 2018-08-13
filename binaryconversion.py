# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:55:20 2018

@author: leder
"""

# Converting from Decimal to Binary

num = int(input("input number: "))

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = "-" + result

print("Binary is: "+ result)
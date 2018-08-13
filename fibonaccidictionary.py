# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 13:03:32 2018

@author: leder

This code is just playing with efficiency of finding a Fibonacci number
   
Both functions (fib and fib_efficient) use recursion to find the Fibonacci
    number, but fib_efficient stores Fibonacci numbers in a dictionary as it calculates.
    
This drastically reduces the number of calls we have to recursively make to the function

We store the number of calls to the function in a variable called numFibCalls
    
"""

#Fibonacci Standard
def fib(n):
    global numFibCalls
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#Fibonacci with a Dictionary
def fib_efficient(n, d):
    global numFibCalls
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


reset = {1:1, 2:1}
d = reset

test = int(input("Find the Fibonacci number: "))

numFibCalls = 0
print("Fibonnaci Number (calculated efficiently): ", fib_efficient(test, d))
print("     Number of function calls:", numFibCalls)

if (numFibCalls > 70):
    print("Standard Calculation would take significantly longer to perform")
    print("To keep the program short, the calculation will not be performed")
else:
    numFibCalls = 0
    print("Fibonacci Number (standard calculation): ", fib(test))
    print("     Number of function calls", numFibCalls)

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:55:35 2018

@author: leder
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
                
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))

test = input("What would you like to test: ")

print("")
print("%s: "% test, isPalindrome(test))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:24:06 2020

@author: amirfeizi
"""

 
# driver code
def isPowerOfThree(n):
    for x in range(1,n):
        if  x*x*x==n : 
            return True
        else:
            return False


isPowerOfThree(27)
            

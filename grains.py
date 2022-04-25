# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:28:16 2022

@author: smenco
"""

def square(number):
    
    if number not in range(1, 65): raise ValueError("square must be between 1 and 64")
    
    return 2 ** (number - 1)

def total():
    return (2 ** 64) - 1
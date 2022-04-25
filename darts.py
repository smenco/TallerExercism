# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:48:18 2022

@author: smenco
"""

from math import sqrt

def score(x, y):
    rad = sqrt (x**2 + y**2)

    if rad > 10 :
        return 0

    if rad > 5 :
        return 1

    if rad > 1 :
        return 5

    return 10
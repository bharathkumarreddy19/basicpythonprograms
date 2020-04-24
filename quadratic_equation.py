# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:09:41 2020

@author: bhara_5sejtsc
"""

import cmath

def quadratic_eq(a,b,c):
	d = (b**2) - (4*a*c)
	return d

a = float(input("First coefficient: "))
b = float(input("Second coefficient: "))
c = float(input("Third coefficient: "))

d = (b**2) - (4*a*c)
x1 = ((-b) + (cmath.sqrt(d)))/(2 * a)
x2 = ((-b) - (cmath.sqrt(d)))/(2 * a)

print("Roots of the equation are {0} and {1}".format(x1,x2))

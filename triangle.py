# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:47:25 2020

@author: bhara_5sejtsc
"""

from math import sqrt

def periscalene(a,b,c):
	return (a + b + c)

def areascalene(s,a,b,c):
	s = (a + b + c)/2
	return (sqrt(s * (s - a) * (s - b) * (s - c)))

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

print("Perimeter of triangle is ", periscalene(a,b,c))
print("Area of triangle is " , areascalene(s,a,b,c)) 
	
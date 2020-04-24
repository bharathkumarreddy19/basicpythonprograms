# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:04:25 2020

@author: bhara_5sejtsc
"""

def areaRectangle(l, b): 
	return (l * b) 

def perimeterRectangle(l, b): 
	return (2 * (l + b)) 


l = int(input("length = ")); 
b = int(input("breadth = ")); 

print ("Area = ", areaRectangle(l, b)) 
print ("Perimeter = ", perimeterRectangle(l, b)) 



# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:02:27 2020

@author: bhara_5sejtsc
"""

def addition(a,b):
	return (a + b)

def subtraction(a,b):
	return (a - b)

def multiplication(a,b):
	return (a * b)

def division(a,b):
	return (a/b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition of two numbers is ",addition(a,b))
print("Subtraction of two numbers is ",subtraction(a,b))
print("Multiplication of two numbers is ",multiplication(a,b))
print("Division of two numbers is ",division(a,b))
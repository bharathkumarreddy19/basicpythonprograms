# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 20:22:13 2020

@author: bhara_5sejtsc
"""

import calendar;  


def calenderofmonth(yy,mm):
	cal = calendar.month(yy,mm)
	return cal 
 
def calenderofyear(yy):
	cal1=calendar.prcal(yy)
	return cal1

yy = int(input("Year: "))
mm = int(input("month: "))

print("Month calender: ",calenderofmonth(yy,mm))
print("Year calender: ",calenderofyear(yy))


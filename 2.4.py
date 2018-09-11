# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:49:16 2017

@author: ZHENGHAN ZHANG
"""

#Get the numbers from the user as strings first
#And deal with the whitespaces
a=str(input('Please enter the first number: '))
b=str(input('Please enter the second number: '))
c=str(input('Please enter the third number: '))
d=str(input('Please enter the fourth number: '))
a=a.strip(' ')
b=b.strip(' ')
c=c.strip(' ')
d=d.strip(' ')


#concatenate the numbers
x=int(a+b)
y=int(c+d)
#calculate
print(x+y)
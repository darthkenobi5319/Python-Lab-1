# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:58:45 2017

@author: ZHENGHAN ZHANG
"""

#Obtain the date
print('Please enter the date')
day=int(input('day: '))
month=int(input('month: '))
year=int(input('year: '))
#get the date for today
import datetime
today=datetime.datetime.today()
anotherDate=datetime.datetime(year,month,day)
#find the difference
diff=today-anotherDate
#convert into seconds
seconds=int(diff.total_seconds())
#convert into days
diffDays=seconds//60//60//24
#print the days
if diffDays == 1:
    print('The date you entered is',diffDays,"day away from today")
else:
    print('The date you entered is',diffDays,"days away from today")
#!/usr/bin/python3
#coding:utf-8
import random
first = random.randint(1,255)
second = random.randint(0,255)
third = random.randint(0,255)
last = random.randint(1,255)
a = "%d.%d.%d.%d" %(first,second,third,last)
print(type(a))
# a = str(first) + '.' + str(second) + '.' +str(third) + '.' + str(last)
# print(a)
# print(type(a))
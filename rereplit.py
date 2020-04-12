#!/usr/bin/python3
#coding:utf-8
import re
a = 'n m    k-f'
b = re.split('\s+|-',a)
print(b)

c = r'a\\b\c\\\f/d'
print(re.split(r'\\+|/',c))

d = r'ab c\c\\dd\\\eee   s'
print(d.replace('b','c'))
print(re.sub(r'\s+|\\+','-',d))
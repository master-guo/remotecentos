#!/usr/bin/python3
#coding:utf-8
import re
a = 'n m    k-f'
b = re.split('\s+|-',a)
print(b)

c = r'a\\b\c\\\f/d'
print(re.split(r'\\+|/',c))
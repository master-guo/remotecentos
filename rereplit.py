#!/usr/bin/python3
#coding:utf-8
import re,os
a = 'n m    k-f'
b = re.split('\s+|-',a)
print(b)

c = r'a\\b\c\\\f/d'
print(re.split(r'\\+|/',c))

d = r'ab c\c\\dd\\\eee   s'
print(d.replace('b','c'))
print(re.sub(r'\s+|\\+','-',d))

k = os.popen('ifconfig ens33')
m = 'inet 192.168.18.128  netmask 255.255.255.0  broadcast 192.168.18.255'
for i in k:
    try:
        n = re.match('\s{0,}\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',i).groups()
        print(n)
    except:
        pass


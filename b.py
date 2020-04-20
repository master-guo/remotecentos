#!/usr/bin/python3
#coding:utf-8
import random
choose = []
zs = int(input('input int range 1~1000: '))
while zs>0:
    choose.append(random.randint(1,1000))
    zs-=1
print(choose)
print(choose.__len__())
m = set(choose)
k = list(m)
k.sort()
print(k)
print(k.__len__())
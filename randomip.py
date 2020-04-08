#!/usr/bin/python3
#coding:utf-8
import random
first = random.randint(1,255)
second = random.randint(0,255)
third = random.randint(0,255)
last = random.randint(1,255)
a = "%d.%d.%d.%d" %(first,second,third,last)
print(a)
# a = str(first) + '.' + str(second) + '.' +str(third) + '.' + str(last)
# print(a)
# print(type(a))

mask = input('input mask : ')
k = a.split('.')
# print(k)
# m = ip.split('.')
seck = '1' * int(mask) + (32 - int(mask)) * '0'
# print(seck[0:9],seck[9:17],seck[17:25],seck[25:])
s = bin(int(bin(int(k[0])),2) & int(bin(int(seck[0:8],2)),2))
j = bin(int(bin(int(k[1])),2) & int(bin(int(seck[8:16],2)),2))
u = bin(int(bin(int(k[2])),2) & int(bin(int(seck[16:24],2)),2))
p = bin(int(bin(int(k[3])),2) & int(bin(int(seck[24:],2)),2))
# print(s,j,u,p)

print(str(int(s,2)) + '.' + str(int(j,2)) + '.' + str(int(u,2)) + '.' + str(int(p,2)))




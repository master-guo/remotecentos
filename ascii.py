#!/usr/bin/python3
#coding:utf-8
a = input("Please input some character: ")
b = ''
for i in range(len(a)):
    b = str(ord(a[i])) + b
print("ascii of " + a + " is " + b)
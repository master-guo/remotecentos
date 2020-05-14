#!/usr/bin/python3
#coding:utf-8
a = input('Input the first character: ')
b = input('Input the second character: ')
def df(x,y):
    k = []
    for i in x:
        if i in y:
            k.append(i)
    return k
print(df(a,b))

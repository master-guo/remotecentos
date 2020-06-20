#!/usr/bin/python3
#coding:utf-8
def test(**args):
    return args
print(test(a=1,b=2))

def test1(a,b,c):
    return a,b,c
print(test1(**{'a':1,'b':2,'c':3}))
print(test1(*[1,2,3]))

def test2(*args):
    return args
print(list(test2(*['a','b']))[0])
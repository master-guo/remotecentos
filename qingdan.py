#!/usr/bin/python3
#coding:utf-8
List1 = ['aaa',111,(4,5),2.01]
List2 = ['bbb',333,111,3.14,(4,5)]

for i in List1:
    for o in List2:
        if i == o:
            print(i)
#!/usr/bin/python3
#coding:utf-8
shuru = input('请输入字符： ')
n = 0
m = 0
for i in shuru:
    if i.isdecimal():
        n += 1
    elif i.isalpha():
        m += 1
    else :
        pass
print('数字有：%d个，字母有%d个。'%(n,m))
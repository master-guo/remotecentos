#!/usr/bin/python3
#coding:utf-8
a = input("Please input some character: ")
b = ""
for i in range(len(a)):
    b = b + str(hex(ord(a[i])))
    print(ord(a[i]))
print(b)
c = b.replace(r"0x",r"\x")
print("ascii of " + a + " is " + c)

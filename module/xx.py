#!/usr/bin/python3
#coding:utf-8
from module_ping import *
from prm import *
def ping_and_ssh(ip,username,password,cmd):
    if ping(ip):
        print("%s is ok."%(ip))
        print("login"+' '+ip+' '+'now'+':')
        print(guo_ssh(ip,username,password,22,cmd))
    else:
        print("%s is bad." % (ip))
if __name__ =="__main__":
    while True:
        a = input('please input a ip: ')
        if a != 'quit' or a != 'q':
            ping_and_ssh(a,username='masterguo',password='redhat',cmd='ls')

#!/usr/bin/python3
#coding:utf-8
import os,sys,re,time
b = 0
while True:
    time.sleep(2)
    print('monitor port 80 stat!')
    k = os.popen("netstat -tunl",'r').read()
    f = re.findall('(:\d+)',k)
    if ':80' in f:
        print('httpd startup!')
        break


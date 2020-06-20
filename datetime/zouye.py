#!/usr/bin/python3
#coding:utf-8
import os,datetime
a = datetime.datetime.now()
b = a.strftime("%Y-%m-%d_%H-%M-%S")
c = a - datetime.timedelta(days = 5)
d = c.strftime("%Y-%m-%d_%H-%M-%S")
fileName = 'save_fivedaysago_time_' + b + '.txt'

os.chdir('/tmp')
fp = open(fileName,'w+')
fp.write(str(d)+'\r\n')
fp.close()


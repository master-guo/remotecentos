#!/usr/bin/python3
#coding:utf-8
s = 'TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247,idle 0:00:00 bytes 74,flags UIO'
import re
f = re.match('\w+\s+\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5})\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5})\,\w+\s\d+\:\d+\:\d+\s\w+\s+(\d{1,})',s).groups()
print(f)
d = {(f[0],f[1]):f[2]}
print(d)